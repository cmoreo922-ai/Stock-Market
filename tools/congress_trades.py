#!/usr/bin/env python3
"""Browse US House stock-trade disclosures (STOCK Act Periodic Transaction Reports).

Downloads the official yearly filing index from the House Clerk
(disclosures-clerk.house.gov), filters to Periodic Transaction Reports —
the filings that disclose stock trades — and prints who filed, when, and a
direct link to the PDF containing the actual trades (tickers, dates,
amount ranges).

No API key needed; this is public government data. Uses only the standard
library. The index is cached next to this script for a day.

Usage:
  python congress_trades.py latest              # 15 most recent PTR filings
  python congress_trades.py latest -n 40        # more of them
  python congress_trades.py latest --year 2025  # a different year
  python congress_trades.py member pelosi       # filings matching a name

Senate filings live at efdsearch.senate.gov (interactive search only);
capitoltrades.com merges both chambers for free.
"""

import argparse
import io
import json
import sys
import time
import urllib.request
import zipfile
from datetime import datetime
from pathlib import Path

INDEX_URL = "https://disclosures-clerk.house.gov/public_disc/financial-pdfs/{year}FD.zip"
PTR_PDF_URL = "https://disclosures-clerk.house.gov/public_disc/ptr-pdfs/{year}/{docid}.pdf"
CACHE_DIR = Path(__file__).resolve().parent / ".congress_cache"
CACHE_TTL_SECONDS = 24 * 3600

# FilingType codes in the index; P = Periodic Transaction Report (trades).
FILING_TYPES = {
    "P": "PTR (trades)",
    "A": "Annual report",
    "C": "Candidate report",
    "T": "Termination",
    "X": "Extension",
    "W": "Withdrawal",
}


def fetch_index(year):
    """Return the raw index text for a year, from cache or the Clerk's site."""
    CACHE_DIR.mkdir(exist_ok=True)
    cache_file = CACHE_DIR / f"{year}FD.txt"
    if cache_file.exists() and time.time() - cache_file.stat().st_mtime < CACHE_TTL_SECONDS:
        return cache_file.read_text(encoding="utf-8", errors="replace")

    url = INDEX_URL.format(year=year)
    try:
        with urllib.request.urlopen(url, timeout=60) as resp:
            payload = resp.read()
    except Exception as e:
        if cache_file.exists():
            print(f"(download failed: {e}; using stale cache)", file=sys.stderr)
            return cache_file.read_text(encoding="utf-8", errors="replace")
        sys.exit(
            f"Could not download the {year} index from {url}\n({e})\n"
            "Check your connection, or try an earlier --year."
        )

    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        txt_name = next(n for n in zf.namelist() if n.endswith(".txt"))
        text = zf.read(txt_name).decode("utf-8", errors="replace")
    cache_file.write_text(text, encoding="utf-8")
    return text


def parse_index(text, year):
    """Parse the tab-separated index into a list of filing dicts."""
    lines = [ln.rstrip("\r") for ln in text.splitlines() if ln.strip()]
    header = lines[0].split("\t")
    col = {name: i for i, name in enumerate(header)}
    filings = []
    for line in lines[1:]:
        parts = line.split("\t")
        if len(parts) < len(header):
            continue

        def field(name):
            return parts[col[name]].strip()

        raw_date = field("FilingDate")
        try:
            filed = datetime.strptime(raw_date, "%m/%d/%Y")
        except ValueError:
            filed = None
        filings.append(
            {
                "last": field("Last"),
                "first": field("First"),
                "district": field("StateDst"),
                "type": field("FilingType"),
                "filed": filed,
                "filed_raw": raw_date,
                "docid": field("DocID"),
                "year": year,
            }
        )
    return filings


def pdf_url(f):
    return PTR_PDF_URL.format(year=f["year"], docid=f["docid"])


def print_filings(filings, ptr_only=True):
    if ptr_only:
        filings = [f for f in filings if f["type"] == "P"]
    if not filings:
        print("No matching filings.")
        return
    for f in filings:
        name = f"{f['first']} {f['last']}".strip()
        kind = FILING_TYPES.get(f["type"], f["type"])
        print(f"{f['filed_raw']:>10}  {name} ({f['district']})  [{kind}]")
        if f["type"] == "P":
            print(f"            trades PDF: {pdf_url(f)}")
    print(
        f"\n{len(filings)} filings shown. PDFs list each trade's ticker, "
        "date, buy/sell, and amount range."
    )
    print("Reminder: disclosures lag trades by up to 45 days (see Module 12).")


def sort_by_date(filings):
    return sorted(
        filings,
        key=lambda f: f["filed"] or datetime.min,
        reverse=True,
    )


def cmd_latest(args):
    filings = parse_index(fetch_index(args.year), args.year)
    ptrs = sort_by_date([f for f in filings if f["type"] == "P"])
    print_filings(ptrs[: args.count])


def cmd_member(args):
    query = args.name.lower()
    filings = parse_index(fetch_index(args.year), args.year)
    hits = [
        f
        for f in filings
        if query in f["last"].lower() or query in f["first"].lower()
    ]
    print_filings(sort_by_date(hits), ptr_only=not args.all_types)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="filing year to search (default: current year)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_latest = sub.add_parser("latest", help="most recent trade filings")
    p_latest.add_argument("-n", "--count", type=int, default=15)
    p_latest.set_defaults(func=cmd_latest)

    p_member = sub.add_parser("member", help="filings matching a name")
    p_member.add_argument("name")
    p_member.add_argument(
        "--all-types",
        action="store_true",
        help="include annual reports etc., not just trade filings",
    )
    p_member.set_defaults(func=cmd_member)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

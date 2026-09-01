# Stock-Market repo guide

Self-paced stock-market education repo. No build system, no dependencies
beyond optional `yfinance` for live prices in the paper trader.

## Layout

- `curriculum/01-07` — core course (foundations → written strategy), read in order
- `curriculum/08-13` — advanced: day trading, bear markets, global markets,
  strategy playbook, congressional trades, automation/broker APIs
- `curriculum/GLOSSARY.md` — term definitions
- `tools/paper_trader.py` — stdlib-only paper-trading CLI; state persists in
  `tools/portfolio.json` (gitignored)
- `tools/congress_trades.py` — stdlib-only CLI pulling House STOCK Act filing
  indexes from disclosures-clerk.house.gov; caches in `tools/.congress_cache/`
  (gitignored)
- `journal/TEMPLATE.md` — per-trade journal template

## Conventions

- Curriculum voice: plain English, honest about base rates and risk, ends each
  module with a Checkpoint and a link to the next module. Keep new modules in
  that style and add them to the README table.
- Tools are standard-library Python 3 with graceful degradation when the
  network or optional deps are unavailable. Test manually before committing
  (`--price` flag makes paper_trader testable offline).
- Never present anything in this repo as financial advice; education only.
- The owner's long-term goal: eventually build a guardrail-first automated
  trading setup (see Module 13) — paper trading via Alpaca first, hard
  fail-safes (position caps, daily loss limits, kill switch), never unofficial
  Robinhood APIs, and Claude never holds live brokerage credentials.

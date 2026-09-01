# Module 12: Tracking Congressional Trades

Yes, you can legally see what members of Congress trade, and yes, people run
"mirror the politicians" strategies. Here's how the system works, where the
data lives, what the evidence actually shows, and how to use it without
fooling yourself.

## The legal basis: the STOCK Act (2012)

The **Stop Trading on Congressional Knowledge Act** requires members of
Congress (and senior staff) to:

- Publicly disclose any stock/bond/option/crypto transaction over **$200**
- Within **30 days of becoming aware, max 45 days after the trade**
- Via **Periodic Transaction Reports (PTRs)** — public documents

Key limitations baked into the system:

- **Amounts are ranges, not exact**: "$1,001–$15,000", "$15,001–$50,000",
  up to "over $50,000,000". You never know the true size.
- **The 45-day lag is an eternity** in markets. By the time you see the
  trade, the stock has already reacted to whatever they may have known.
- Many filings are by **spouse or dependent**, or made by an outside
  manager the member claims not to direct.
- **Enforcement is weak**: the standard late-filing fine is $200. Members
  file late constantly.
- Periodic proposals to ban congressional stock trading have so far not
  passed — as of now, this data stream exists and keeps flowing.

## Where the data lives

**Primary (official, free):**

- House: `disclosures-clerk.house.gov` — searchable database + a yearly
  index file listing every filing (this repo's
  `tools/congress_trades.py` pulls this directly).
- Senate: `efdsearch.senate.gov` — searchable electronic filing system.

**Aggregators (parse the PDFs for you):**

- **Capitol Trades** (capitoltrades.com) — free, clean, searchable by
  politician/ticker.
- **Quiver Quantitative** (quiverquant.com) — free tier + paid; also tracks
  the derived ETFs.
- **Unusual Whales** — paid; congressional + options-flow tracking.

**Investable products that do the mirroring for you:**

- **NANC** — ETF tracking trades disclosed by Democratic members' households.
- **KRUZ** — same for Republican members' households.
  Both launched 2023, run by Subversive/Unusual Whales, holding ~100–500
  positions rebuilt from disclosures.

## What the evidence actually says

- A famous 2004 study (Ziobrowski) found Senators' portfolios beat the
  market by ~10%/yr in the 1990s — **pre-STOCK Act**. This study is why the
  strategy has such a strong reputation.
- Post-2012 academic work mostly finds **little to no aggregate
  outperformance** once disclosure and attention arrived. The *average*
  member is not a market wizard; many are just wealthy people holding index
  funds and AAPL/MSFT like everyone else.
- **But the distribution has a fat tail**: specific members — especially
  those on committees overseeing the sectors they trade (armed services →
  defense stocks, health committees → pharma, banking → banks) — have
  produced eyebrow-raising, well-timed trades repeatedly. Aggregators
  exist precisely because a handful of filers are worth watching.
- The mirror ETFs (NANC/KRUZ) have roughly tracked the S&P 500 since
  launch, with NANC ahead of it in some periods largely due to being
  overweight the same mega-cap tech an index investor already owns.

Honest synthesis: **mirroring "Congress" wholesale ≈ owning an expensive,
lagged, tech-tilted index fund. Watching *selected* filers as an
idea-generation signal has more going for it.**

## If you run this strategy anyway, run it well

1. **Follow filers, not the institution.** Build a shortlist: members with
   committee seats relevant to their trades, a history of large single-stock
   purchases (not fund shuffling), and decent past timing. Aggregators let
   you view per-member track records.
2. **Weight purchases over sales** (sales happen for boring reasons — taxes,
   houses, divorces). A large, unusual *buy* in a committee-adjacent stock
   is the interesting event.
3. **Mind the lag**: check what the stock did since the trade date. If it
   already moved 30%, the signal is spent.
4. **Treat it as a screen, not an order**: a hit feeds your Module 4
   checklist ("why is the market wrong?" gains the answer "someone with
   committee-level information is buying") — it doesn't skip it.
5. **Position-size like any explore trade**: Module 6 rules apply. No
   politician's disclosure justifies breaking your 5% cap.
6. **Log it in the journal** with "source: congressional disclosure" so you
   can audit, after 20 trades, whether this signal is actually paying *you*.

## The tool in this repo

```bash
python tools/congress_trades.py latest          # most recent House PTR filings
python tools/congress_trades.py latest -n 30    # last 30
python tools/congress_trades.py member pelosi   # filings by name match
python tools/congress_trades.py latest --year 2026
```

It downloads the official House Clerk yearly index, filters to PTRs (the
stock-trade filings), and prints who filed, when, and the direct PDF link to
the actual trade report. Read the PDFs for tickers, dates, and amount ranges
— then do your own analysis. (Senate filings require an interactive session
on efdsearch.senate.gov; use Capitol Trades for a merged view.)

## Ethics & reality check

Nothing here is inside information — these are mandatory public disclosures,
and trading on them is exactly what the STOCK Act intended to enable
(sunlight as disinfectant). Just remember the structural truth: you are the
*last* person in this information chain. The member traded up to 45 days
ago; algorithms parsed the filing within seconds of posting; the ETFs
rebalanced. Whatever edge survives all that is thin — use it as one input,
never as a religion.

## Checkpoint

- What does a PTR disclose, and what does it deliberately blur?
- Why are congressional *buys* more informative than sells?
- Why does the 45-day lag matter less for a long-term thesis than a trade?
- Run the tool, pick one real recent filing, and take its PDF through the
  Module 4 checklist as an exercise.

**Next:** [Module 13 – Automation, Broker APIs & Fail-safes](13-automation-and-broker-apis.md)

# Module 8: Day Trading & Swing Trading

You asked for it, so here it is — the complete, honest picture. Short-term
trading is a real discipline with real practitioners. It is also the area of
the market where retail participants lose the most money, so this module is
half mechanics, half armor.

## Definitions

- **Day trading** — positions opened and closed within the same session.
  Nothing held overnight. Profits come from intraday moves of 0.5–3%.
- **Swing trading** — positions held days to weeks, riding a single "swing"
  of a trend. The middle ground between day trading and investing.
- **Scalping** — dozens of trades per day for tiny moves. Requires speed,
  low costs, and full-time attention. Effectively competing with algorithms.

## The statistics you must know before starting

Large academic studies (Brazil day-trader study 2019, Taiwan full-market
study, US retail brokerage data) consistently find:

- **~97% of people who day trade for more than 300 days lose money.**
- Fewer than 1% of day traders earn more than minimum wage from it after costs.
- Performance is persistent in the wrong direction: most losing traders keep
  losing, because the losses come from structural costs, not bad luck.
- The profitable minority are effectively running a full-time job with
  professional discipline, tooling, and years of screen time.

Nobody is exempt from these numbers by enthusiasm. If you day trade, do it
knowing the base rate, with money sized so total loss is acceptable tuition.

## Rules and mechanics (US)

- **Pattern Day Trader (PDT) rule:** 4+ day trades within 5 business days in
  a **margin** account flags you as a PDT, requiring **$25,000 minimum
  equity**. Below that, your account gets restricted.
  - Cash accounts are exempt from PDT, but you can only trade **settled**
    cash (T+1) — trading with unsettled funds causes good-faith violations.
- **Wash sales** (Module 2) get messy fast with frequent trading — every
  loss re-entered within 30 days is disallowed for tax purposes.
- **All short-term profits are taxed as ordinary income** — up to 37%
  federal. A day trader must beat the market by a wide margin just to match
  an index investor after tax.

## How day traders actually operate

The profitable ones share a common skeleton:

1. **A written setup** — one or two specific, repeatable patterns they trade
   (e.g., opening-range breakout, VWAP reclaim, gap-and-go on news). They
   skip everything else. Beginners lose by trading everything that moves.
2. **Pre-market preparation** — a watchlist of 3–5 candidates with unusual
   volume or news, levels marked before the open.
3. **Fixed risk per trade** — typically 0.5–1% of account, stop set before
   entry, position size derived from the stop distance (Module 6 math).
4. **A daily loss limit** — e.g., down 3% on the day = shut the laptop.
   This single rule is what separates survivors from blowups.
5. **Time windows** — most trade only the first 60–90 minutes and sometimes
   the last 30. Midday is chop that eats accounts.
6. **Journal + review** — every trade logged, weekly review of what setup,
   what execution error, what emotional error.

## Swing trading — the saner middle path

Swing trading fits around a day job, needs no $25k, and has lower cost drag.
A typical rule-based swing system:

- **Universe:** liquid stocks/ETFs above their 200-day MA (trade with the
  long-term trend only).
- **Entry:** pullback to the 20-day or 50-day MA that holds, or a breakout
  from a multi-week base on above-average volume.
- **Stop:** below the pullback low / breakout level; risk 1% of account.
- **Exit:** trail a stop under higher lows, or sell half at 2× risk and
  trail the rest.
- **Hold:** days to weeks. No adding to losers, ever.

The edge, if any, comes from cutting losses fast and letting winners run —
the *average winner must be larger than the average loser*, because your win
rate will hover near 50%.

## What actually kills trading accounts

In rough order of body count:

1. **No daily loss limit** — one tilted afternoon undoes three good months.
2. **Oversizing** — a "sure thing" position 10× normal size.
3. **Averaging down** on losers ("it can't go lower" — it can).
4. **Revenge trading** after a loss.
5. **Strategy hopping** — abandoning each system at its first drawdown, so
   no system's edge (if any) ever gets time to show up.
6. **Trading illiquid junk** — penny stocks and meme spikes where spreads
   and slippage are the house edge against you.

## The only responsible on-ramp

1. Paper trade a **single written setup** for 3 months minimum
   (`tools/paper_trader.py` + journal). Track win rate, average win/loss,
   and whether you followed rules.
2. If (and only if) the paper record is profitable **and** disciplined, go
   live with an amount whose total loss would not change your life.
3. Keep your index core (Module 3) untouched throughout. Trading money and
   wealth-building money live in different accounts, physically.
4. Re-evaluate honestly every quarter against "what if I'd just bought VTI?"

## Checkpoint

- What is the PDT rule and how do cash accounts differ?
- Why do taxes alone put day traders at a structural disadvantage?
- What's a daily loss limit and why is it the single most protective rule?
- Design (on paper) one swing setup: universe, entry, stop, exit, risk %.

**Next:** [Module 9 – Bear Markets & Market Cycles](09-bear-markets-and-cycles.md)

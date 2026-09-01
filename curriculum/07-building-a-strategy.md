# Module 7: Building a Strategy

Knowledge without a written system produces impulse trades with extra steps.
This module turns Modules 1–6 into a plan you can actually follow — and a
process for improving it.

## Why written?

Because future-you, watching a position drop 20% or spike 40%, is a different,
dumber person than present-you reading this calmly. The plan is a contract
with that person. If it isn't written, it doesn't exist.

## The Investment Policy Statement (IPS)

Write yours in one page. Template:

```
GOALS
- What is this money for, and when will I need it?

CONTRIBUTIONS
- I invest $___ per month, automatically, on the ___ of the month.

ALLOCATION
- Core (index funds): ___%   [suggested: 90%+ while learning]
- Explore (stock picks): ___%  [suggested: ≤10%]
- Target mix within core: __% US / __% international / __% bonds
- Rebalance: every ___ [e.g., January], back to targets.

RULES FOR STOCK PICKS
- Max single position: __% of total portfolio.
- I buy only after completing the Module 4 checklist in writing,
  including "why is the market wrong?"
- Exit triggers: I sell if ______ (thesis broken / price target /
  stop level) — decided BEFORE buying.

CRASH CLAUSE
- When the market drops 30%+, I will: ______
  [suggested: change nothing; continue scheduled buys]

FORBIDDEN
- Margin, shorting, options [until ___], crypto leverage, buying
  anything the same day I first heard of it.

REVIEW
- I review this document and my journal every ___ months.
- I change this document only during a scheduled review, never
  during a market event.
```

That last line is the most important one in this course.

## The trade journal

For every explore-bucket trade, log (template in `journal/TEMPLATE.md`):

1. Date, ticker, size, entry price
2. **Thesis** — why, in two sentences, and why the market is wrong
3. **Exit plan** — price/condition for taking profit and for cutting loss
4. Emotional state (seriously — patterns will emerge)
5. On exit: outcome, and *was the process followed?*

Judge trades by **process, not outcome**. A disciplined trade that lost money
is a good trade; a reckless one that made money is a bad trade that will
teach you the wrong lesson expensively.

## Backtesting and paper trading

Before risking money on any active strategy:

1. **Backtest** the idea against history where possible — but distrust rosy
   results: overfitting, survivorship bias, and ignored costs flatter every
   backtest.
2. **Paper trade** it live for a meaningful stretch — real prices, fake money
   (use `tools/paper_trader.py`). It won't replicate real-money emotions, but
   it filters out strategies that can't even beat the index on paper.
3. **Benchmark honestly**: your competition is buying VTI and going fishing.
   Track your explore bucket vs. the S&P 500, after estimated taxes. Most
   people discover their picks lag the index — discovering it with 10% of
   your money is cheap tuition.

## Archetype strategies (pick one lane while learning)

- **Index + chill (the default):** automate monthly buys; skip everything
  else. Beats ~90% of alternatives with ~0 hours/week.
- **Quality compounders:** buy 10–20 wide-moat, high-ROE businesses at
  reasonable prices; hold for years; add on broad selloffs. Fundamentals-heavy.
- **Value:** buy statistically cheap stocks after checking they're not value
  traps; sell when they re-rate to fair value. Requires patience and strong
  accounting skills.
- **Trend/momentum trading:** rule-based entries on breakouts/trends with
  strict stops and 1–2% risk sizing. Highest effort, highest failure rate,
  fastest feedback. Paper trade for 6+ months first.

Mixing lanes mid-trade ("my breakout failed but it's a value play now") is
the classic way to lose in two styles at once. The lane is chosen before entry.

## Your first 12 months, concretely

1. **Month 0:** Emergency fund funded. Accounts opened (Roth IRA first if
   eligible). Automatic monthly index purchase running. IPS written.
2. **Months 1–3:** Finish this curriculum. Start paper trading. Read one 10-K
   of a company you admire, cover to cover.
3. **Months 3–12:** Paper trade your chosen lane with journal discipline.
   Read: *The Psychology of Money* (Housel), *A Random Walk Down Wall Street*
   (Malkiel), *One Up on Wall Street* (Lynch); *The Intelligent Investor*
   (Graham, ch. 8 and 20 at minimum).
4. **Month 12:** Review the journal. If your paper results beat the index
   *and* you followed your process, fund the explore bucket with ≤10%. If not
   — you've lost nothing, learned plenty, and your index core compounded the
   whole time.

There is no rush. The market will still be there next year. Missed
opportunities are invisible and painless; blown-up accounts are neither.

## Checkpoint

- Write your IPS. Actually write it — this is the course's final exam.
- Set up the paper trader and make your first three journal-logged trades.
- Schedule the Month-12 review on your calendar now.

**Back to:** [README](../README.md) · [Glossary](GLOSSARY.md)

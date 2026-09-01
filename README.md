# Stock-Market

This repo will help with skill building for making money in the stock market.

It's organized as a self-paced course: read the modules in order, use the glossary
when a term is unfamiliar, keep a trade journal, and practice with the included
paper-trading simulator before ever risking real money.

## How to use this repo

1. **Read the curriculum in order.** Each module builds on the last.
2. **Practice with fake money first.** Use `tools/paper_trader.py` to simulate
   buying and selling. Treat it seriously — log why you made each trade.
3. **Keep a journal.** Copy `journal/TEMPLATE.md` for every trade you make
   (paper or real). Reviewing your own decisions is the fastest way to improve.
4. **Only then consider real money** — starting small, in a diversified index
   fund, per Module 3.

## Curriculum

| Module | Topic |
|--------|-------|
| [01 – Foundations](curriculum/01-foundations.md) | What stocks are, how markets work, how you actually make money |
| [02 – Accounts & Mechanics](curriculum/02-accounts-and-mechanics.md) | Brokerages, order types, fees, taxes |
| [03 – Index Investing First](curriculum/03-index-investing.md) | Why low-cost index funds beat most professionals |
| [04 – Fundamental Analysis](curriculum/04-fundamental-analysis.md) | Reading financial statements, valuation ratios |
| [05 – Technical Analysis](curriculum/05-technical-analysis.md) | Charts, trends, indicators — and their limits |
| [06 – Risk Management](curriculum/06-risk-management.md) | Position sizing, diversification, stop losses, psychology |
| [07 – Building a Strategy](curriculum/07-building-a-strategy.md) | Putting it together into a written plan you can follow |
| [Glossary](curriculum/GLOSSARY.md) | Plain-English definitions of common terms |

### Advanced modules

| Module | Topic |
|--------|-------|
| [08 – Day Trading & Swing Trading](curriculum/08-day-trading-and-swing-trading.md) | How short-term trading works, the PDT rule, and the brutal statistics |
| [09 – Bear Markets & Cycles](curriculum/09-bear-markets-and-cycles.md) | Corrections, crashes, recessions — history and what to actually do |
| [10 – Foreign & Global Markets](curriculum/10-foreign-and-global-markets.md) | World exchanges, ADRs, emerging markets, currency risk |
| [11 – The Strategy Playbook](curriculum/11-strategy-playbook.md) | Value, growth, momentum, dividends, event-driven, copy trading — evidence and fit |
| [12 – Congressional Trades](curriculum/12-congressional-trades.md) | The STOCK Act, tracking politicians' trades, and mirroring honestly |
| [13 – Automation & Broker APIs](curriculum/13-automation-and-broker-apis.md) | Bots, the Robinhood reality, Alpaca paper trading, and fail-safe design |

## Tools

- **`tools/paper_trader.py`** — a command-line paper-trading simulator with live
  prices (via `yfinance` when installed, manual price entry otherwise). Tracks
  cash, positions, and profit/loss across sessions.
- **`tools/congress_trades.py`** — browses official US House stock-trade
  disclosures (STOCK Act filings) straight from disclosures-clerk.house.gov,
  with direct links to each trade report PDF. No API key needed.
- **`journal/TEMPLATE.md`** — trade journal template.

```bash
# Optional, for live prices:
pip install yfinance

python tools/paper_trader.py buy AAPL 10
python tools/paper_trader.py portfolio
python tools/paper_trader.py sell AAPL 5
python tools/paper_trader.py history

python tools/congress_trades.py latest          # recent congressional trade filings
python tools/congress_trades.py member pelosi   # filings by member name
```

## Important disclaimer

Nothing in this repo is financial advice. Markets involve real risk, including
losing everything you invest. Most active traders underperform simple index
funds. The goal here is education: understand what you're doing and why before
you do it with money you can't afford to lose.

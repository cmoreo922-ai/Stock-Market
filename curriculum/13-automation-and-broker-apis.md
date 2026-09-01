# Module 13: Automation, Broker APIs & Fail-safes

The question behind this module: *"Can an AI (or a bot) execute trades for me
through Robinhood-style apps — with fail-safes so it can't bankrupt me?"*

Short answer: **yes, automated trading is real and accessible — but not
through Robinhood, and the fail-safes are the most important code in the
whole system.** Here's the full picture.

## The Robinhood reality

- Robinhood has **no official public API for stock trading**. (It launched an
  official API for *crypto* in 2024; equities remain app-only.)
- Unofficial libraries (e.g., `robin_stocks`) reverse-engineer the private
  app API. Using them: violates Robinhood's terms of service (account
  restriction/closure risk), breaks without warning when Robinhood changes
  endpoints, and requires storing your real login + 2FA secrets in scripts —
  a security hazard on top of everything else.
- **Verdict: don't automate against Robinhood.** Keep it (or any app) for
  manual trades if you like the interface.

## Brokers with real, official APIs

| Broker | API | Paper trading | Notes |
|--------|-----|---------------|-------|
| **Alpaca** | First-class REST/WebSocket, official Python SDK | **Yes — free, built-in** | Built *for* API trading; commission-free stocks/ETFs. The standard beginner choice. |
| **Interactive Brokers** | Full API (TWS / IB Gateway, Web API) | Yes | Most powerful; global markets; steeper learning curve. |
| **TradeStation** | Official REST API | Yes (simulated) | Trader-oriented. |
| **Charles Schwab** | Official Trader API (individual access) | Limited | Successor to the old TD Ameritrade API. |
| **Tradier** | Brokerage-as-API | Yes (sandbox) | Developer-focused. |

The sane path: **Alpaca's paper-trading mode** — a real API, real market
data, fake money. You can build and run the exact bot you'd run live, flip
a single URL to go live later, and until then your maximum possible loss is
$0.

## What an automated strategy actually looks like

```
[Data feed] → [Signal logic] → [Risk checks] → [Order submission] → [Logging/alerts]
```

1. **Data**: prices via the broker API or a data provider.
2. **Signal**: your *written* rules from Module 7/11, in code. If you can't
   write the rule precisely enough to code it, you don't have a rule yet —
   automation exposes vague strategies instantly (a feature, not a bug).
3. **Risk checks (the fail-safes)**: every order passes through a gate that
   can reject it. Details below — this layer is the whole ballgame.
4. **Execution**: limit orders via API, with idempotency (never double-send
   on a retry).
5. **Logging**: every decision, order, fill, and rejection logged; alerts
   (email/text) on anything unusual.

## The fail-safe layer ("don't bankrupt me" — codified)

These are the standard guardrails in professional and hobbyist systems
alike. **Every** order must pass **all** of them:

| Guardrail | Example setting | What it prevents |
|-----------|----------------|------------------|
| Kill switch | one command/file flips bot to liquidate-only or halt | runaway anything |
| Max position size | ≤ 5% of equity per symbol | concentration blowups |
| Max order size | ≤ $X per single order | fat-finger / logic-bug orders |
| Daily loss limit | halt all new orders at −2% equity day | death by a thousand cuts, or one bad day |
| Max drawdown limit | full stop + alert at −10% from peak | strategy rot continuing silently |
| Order rate limit | ≤ N orders/hour | infinite-loop bugs (classic bot killer) |
| Symbol whitelist | only pre-approved liquid tickers | penny-stock/fat-tail garbage |
| Notional cap | bot may only ever touch $Y total | ...bankrupting you. The bot literally cannot exceed this. |
| No margin, no shorting, no options | account-level settings at the broker | unlimited-loss exposure |
| Market-hours check | no orders outside regular hours | illiquid after-hours fills |
| Human confirmation mode | bot proposes, you approve each trade | full autonomy before trust is earned |
| Heartbeat + dead-man switch | if bot stops reporting, cancel open orders | crashed bot leaving stale orders |

Two design principles:

- **Fail closed.** Any error, any ambiguity, any failed check → do nothing
  and alert a human. A bot that misses a trade costs opportunity; a bot that
  trades wrongly costs capital.
- **Defense in depth.** Set limits in *code* AND at the *broker* (account
  without margin approval, cash-only, small funded balance). The money the
  bot can access is your true maximum loss — so only fund the bot's account
  with the explore bucket (Module 3), never the core.

## The honest expectations paragraph

Automation improves **discipline** (no fear, no FOMO, no revenge trades) and
**consistency**. It does not create an edge. A mediocre strategy automated
is a mediocre strategy executed faster. Retail algo traders lose for the
same reason retail day traders do — the strategy, not the plumbing. This is
why the pipeline is: **paper-trade the strategy by hand (Modules 7–8) →
code it → run it on Alpaca paper for months → compare honestly to the index
→ only then, small real money behind the full guardrail stack.**

Also know the sharp edges: bugs (the #1 cause of retail algo losses),
overfit backtests that die on live data, API outages mid-position, and taxes
on high turnover. Log everything; assume the first version is wrong.

## What Claude can and can't do here

- **Can:** teach all of this; write and review the bot code, the guardrail
  layer, the backtests; analyze your journal and results; help you set up
  Alpaca paper trading and build the whole system step by step.
- **Won't/shouldn't:** hold your live brokerage credentials, or be wired to
  autonomously fire real-money trades. The right architecture keeps *you*
  as the key-holder: code runs on your machine/server with your API keys,
  guardrails are yours, and anything real-money starts in
  propose-and-confirm mode.

## Checkpoint

- Why is automating against Robinhood specifically a bad idea?
- What does "fail closed" mean, and why is it the right default?
- Which guardrail creates a hard ceiling on total possible loss?
- Design your own guardrail table with numbers you'd actually accept, and
  put it in your IPS before any bot exists.

**Back to:** [README](../README.md) · [Module 7 – Building a Strategy](07-building-a-strategy.md)

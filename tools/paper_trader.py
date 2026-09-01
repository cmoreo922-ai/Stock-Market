#!/usr/bin/env python3
"""Paper-trading simulator: practice buying and selling stocks with fake money.

State is stored in portfolio.json next to this script, so it persists between
runs. Prices come from Yahoo Finance via the optional `yfinance` package
(pip install yfinance); without it, pass the price yourself with --price.

Usage:
  python paper_trader.py buy AAPL 10            # buy 10 shares at market
  python paper_trader.py buy AAPL 10 --price 230.50
  python paper_trader.py sell AAPL 5
  python paper_trader.py portfolio              # positions, cash, P/L
  python paper_trader.py history                # every trade you've made
  python paper_trader.py reset                  # start over with $100,000
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path(__file__).resolve().parent / "portfolio.json"
STARTING_CASH = 100_000.00


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"cash": STARTING_CASH, "positions": {}, "history": []}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def fetch_price(ticker):
    """Return the latest price from Yahoo Finance, or None if unavailable."""
    try:
        import yfinance as yf
    except ImportError:
        return None
    try:
        data = yf.Ticker(ticker).history(period="1d")
        if data.empty:
            return None
        return float(data["Close"].iloc[-1])
    except Exception:
        return None


def resolve_price(ticker, cli_price):
    if cli_price is not None:
        if cli_price <= 0:
            sys.exit("Price must be positive.")
        return cli_price
    price = fetch_price(ticker)
    if price is None:
        sys.exit(
            f"Could not fetch a live price for {ticker}.\n"
            "Install yfinance (pip install yfinance) or supply one manually, "
            f"e.g.: --price 123.45"
        )
    return price


def record(state, action, ticker, shares, price):
    state["history"].append(
        {
            "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "action": action,
            "ticker": ticker,
            "shares": shares,
            "price": round(price, 4),
            "total": round(shares * price, 2),
            "cash_after": round(state["cash"], 2),
        }
    )


def cmd_buy(state, args):
    ticker = args.ticker.upper()
    price = resolve_price(ticker, args.price)
    cost = args.shares * price
    if cost > state["cash"]:
        sys.exit(
            f"Not enough cash: need ${cost:,.2f}, have ${state['cash']:,.2f}."
        )
    pos = state["positions"].get(ticker, {"shares": 0, "cost_basis": 0.0})
    pos["cost_basis"] = (
        pos["cost_basis"] * pos["shares"] + cost
    ) / (pos["shares"] + args.shares)
    pos["shares"] += args.shares
    state["positions"][ticker] = pos
    state["cash"] -= cost
    record(state, "BUY", ticker, args.shares, price)
    save_state(state)
    print(
        f"Bought {args.shares} {ticker} @ ${price:,.2f} "
        f"(total ${cost:,.2f}). Cash: ${state['cash']:,.2f}"
    )


def cmd_sell(state, args):
    ticker = args.ticker.upper()
    pos = state["positions"].get(ticker)
    if not pos or pos["shares"] < args.shares:
        held = pos["shares"] if pos else 0
        sys.exit(f"You hold {held} shares of {ticker}; can't sell {args.shares}.")
    price = resolve_price(ticker, args.price)
    proceeds = args.shares * price
    realized = (price - pos["cost_basis"]) * args.shares
    pos["shares"] -= args.shares
    if pos["shares"] == 0:
        del state["positions"][ticker]
    state["cash"] += proceeds
    record(state, "SELL", ticker, args.shares, price)
    save_state(state)
    sign = "+" if realized >= 0 else ""
    print(
        f"Sold {args.shares} {ticker} @ ${price:,.2f} "
        f"(total ${proceeds:,.2f}). Realized P/L: {sign}${realized:,.2f}. "
        f"Cash: ${state['cash']:,.2f}"
    )


def cmd_portfolio(state, args):
    print(f"Cash: ${state['cash']:,.2f}\n")
    if not state["positions"]:
        print("No open positions.")
        return
    header = f"{'Ticker':<8}{'Shares':>8}{'Avg cost':>12}{'Price':>12}{'Value':>14}{'P/L':>14}"
    print(header)
    print("-" * len(header))
    total_value = state["cash"]
    priced_all = True
    for ticker, pos in sorted(state["positions"].items()):
        price = fetch_price(ticker)
        if price is None:
            priced_all = False
            print(
                f"{ticker:<8}{pos['shares']:>8}{pos['cost_basis']:>12,.2f}"
                f"{'n/a':>12}{'n/a':>14}{'n/a':>14}"
            )
            continue
        value = pos["shares"] * price
        pl = (price - pos["cost_basis"]) * pos["shares"]
        total_value += value
        sign = "+" if pl >= 0 else ""
        print(
            f"{ticker:<8}{pos['shares']:>8}{pos['cost_basis']:>12,.2f}"
            f"{price:>12,.2f}{value:>14,.2f}{sign}{pl:>13,.2f}"
        )
    if priced_all:
        overall = total_value - STARTING_CASH
        sign = "+" if overall >= 0 else ""
        print("-" * len(header))
        print(
            f"Total account value: ${total_value:,.2f}  "
            f"({sign}${overall:,.2f} vs. ${STARTING_CASH:,.0f} start)"
        )
    else:
        print(
            "\n(Install yfinance for live prices and total account value: "
            "pip install yfinance)"
        )


def cmd_history(state, args):
    if not state["history"]:
        print("No trades yet.")
        return
    for h in state["history"]:
        print(
            f"{h['time']}  {h['action']:<4} {h['ticker']:<6} "
            f"{h['shares']:>6} @ ${h['price']:>10,.2f}  "
            f"total ${h['total']:>12,.2f}  cash ${h['cash_after']:>12,.2f}"
        )


def cmd_reset(state, args):
    if STATE_FILE.exists():
        STATE_FILE.unlink()
    print(f"Portfolio reset. Starting cash: ${STARTING_CASH:,.2f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    for name in ("buy", "sell"):
        p = sub.add_parser(name)
        p.add_argument("ticker")
        p.add_argument("shares", type=int)
        p.add_argument(
            "--price",
            type=float,
            help="use this price instead of fetching a live quote",
        )
    sub.add_parser("portfolio")
    sub.add_parser("history")
    sub.add_parser("reset")

    args = parser.parse_args()
    if args.command in ("buy", "sell") and args.shares <= 0:
        sys.exit("Shares must be a positive whole number.")

    state = load_state()
    {
        "buy": cmd_buy,
        "sell": cmd_sell,
        "portfolio": cmd_portfolio,
        "history": cmd_history,
        "reset": cmd_reset,
    }[args.command](state, args)


if __name__ == "__main__":
    main()

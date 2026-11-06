"""Blocking price audit for AEGIS stock ideas.

Every published idea must use the latest close from the project's market API,
not a remembered or invented level. The audit is deterministic and fails closed:
an unreachable API or unknown ticker blocks publication rather than passing.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from datetime import date

from freshness_policy import trading_days_between

API_BASE = "https://api.138.2.69.165.sslip.io"


def fetch_latest(ticker: str, timeout: float = 10.0) -> dict | None:
    """Return the latest verified equity row, or None when unavailable."""
    url = "%s/equities/latest/%s" % (API_BASE, urllib.parse.quote(str(ticker)))
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            payload = json.load(response)
    except Exception:
        return None
    data = payload.get("data") if isinstance(payload, dict) else None
    return data if isinstance(data, dict) else None


def audit_ideas(ideas, lookup=fetch_latest, tolerance_pct: float = 3.0,
                entry_tolerance_pct: float = 25.0, warnings: list | None = None,
                max_lag_trading_days: int = 2) -> list[str]:
    """Return blocking failures; normal one-day ingestion lag is a warning only."""
    fails: list[str] = []
    for i, idea in enumerate(ideas or []):
        if not isinstance(idea, dict):
            continue
        ticker = str(idea.get("ticker") or "").strip().upper()
        if not ticker:
            continue
        data = lookup(ticker)
        if not data:
            fails.append(
                "stock_ideas[%d] %s: no verified latest price from the market API"
                % (i, ticker)
            )
            continue
        try:
            close = float(data["close"])
            close_date = str(data.get("date") or "").strip()
        except (KeyError, TypeError, ValueError):
            fails.append(
                "stock_ideas[%d] %s: market API row has no usable close/date"
                % (i, ticker)
            )
            continue
        if close <= 0:
            fails.append("stock_ideas[%d] %s: verified close is not positive" % (i, ticker))
            continue
        try:
            current = float(idea.get("current_price"))
            entry = float(idea.get("entry_price"))
        except (TypeError, ValueError):
            continue  # structural validator reports the missing numeric field
        claimed_date = str(idea.get("price_date") or "").strip()
        try:
            claimed_dt = date.fromisoformat(claimed_date[:10]) if claimed_date else None
            close_dt = date.fromisoformat(close_date[:10]) if close_date else None
        except ValueError:
            claimed_dt = close_dt = None
        lag = 0
        if claimed_dt and close_dt:
            if claimed_dt > close_dt:
                fails.append("stock_ideas[%d] %s: price_date %s is newer than the verified close %s"
                             % (i, ticker, claimed_date, close_date))
            else:
                lag = trading_days_between(claimed_dt, close_dt)
                if lag > max_lag_trading_days:
                    fails.append("stock_ideas[%d] %s: price_date %s is %d trading days behind the "
                                 "verified close %s (limit %d)"
                                 % (i, ticker, claimed_date, lag, close_date, max_lag_trading_days))
                elif lag >= 1 and warnings is not None:
                    warnings.append("stock_ideas[%d] %s: using close %s, %d trading day(s) behind "
                                    "the latest verified close %s (expected ingestion lag)"
                                    % (i, ticker, claimed_date, lag, close_date))
        elif claimed_dt is None:
            fails.append("stock_ideas[%d] %s: price_date is missing or invalid" % (i, ticker))
        elif close_dt is None:
            fails.append("stock_ideas[%d] %s: market API row has no usable close date" % (i, ticker))

        diff = abs(current / close - 1.0) * 100.0
        effective_tol = tolerance_pct if lag == 0 else max(tolerance_pct, 6.0)
        if diff > effective_tol:
            fails.append(
                "stock_ideas[%d] %s: current_price %.2f != verified close %.2f "
                "on %s (diff %.1f%%)"
                % (i, ticker, current, close, close_date, diff)
            )
        entry_diff = abs(entry / close - 1.0) * 100.0
        if entry_diff > entry_tolerance_pct:
            fails.append(
                "stock_ideas[%d] %s: entry_price %.2f is %.1f%% away from the "
                "verified close %.2f (limit %.0f%%)"
                % (i, ticker, entry, entry_diff, close, entry_tolerance_pct)
            )
    return fails

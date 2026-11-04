"""Blocking price audit for AEGIS stock ideas.

Every published idea must use the latest close from the project's market API,
not a remembered or invented level. The audit is deterministic and fails closed:
an unreachable API or unknown ticker blocks publication rather than passing.
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

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
                entry_tolerance_pct: float = 25.0) -> list[str]:
    """Return blocking failures for stale, invented or unverifiable prices."""
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
        diff = abs(current / close - 1.0) * 100.0
        if diff > tolerance_pct:
            fails.append(
                "stock_ideas[%d] %s: current_price %.2f != verified close %.2f "
                "on %s (diff %.1f%%)"
                % (i, ticker, current, close, close_date, diff)
            )
        claimed_date = str(idea.get("price_date") or "").strip()
        if close_date and claimed_date != close_date:
            fails.append(
                "stock_ideas[%d] %s: price_date %s != verified close date %s"
                % (i, ticker, claimed_date or "<empty>", close_date)
            )
        entry_diff = abs(entry / close - 1.0) * 100.0
        if entry_diff > entry_tolerance_pct:
            fails.append(
                "stock_ideas[%d] %s: entry_price %.2f is %.1f%% away from the "
                "verified close %.2f (limit %.0f%%)"
                % (i, ticker, entry, entry_diff, close, entry_tolerance_pct)
            )
    return fails

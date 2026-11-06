"""Dataset-specific freshness policy.

Normal ingestion latency is not a QC failure. Each dataset has an expected lag
derived from its schedule and the US trading calendar; only abnormal staleness
blocks publication.
"""
from __future__ import annotations

from datetime import date, datetime

try:
    import pandas_market_calendars as mcal
except Exception:  # pragma: no cover - optional dependency
    mcal = None

# lag units: trading days for prices, business days for macro, calendar days otherwise
THRESHOLDS = {
    "equity_price": {"expected": 1, "warn": 2, "block": 3, "unit": "trading"},
    "macro": {"expected": 2, "warn": 3, "block": 5, "unit": "business"},
    "news": {"expected": 1, "warn": 2, "block": 7, "unit": "calendar"},
    "fundamentals": {"expected": 120, "warn": 180, "block": 365, "unit": "calendar"},
}


def _as_date(value) -> date | None:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def trading_days_between(start: date, end: date) -> int:
    """NYSE sessions in (start, end]; weekends/holidays excluded."""
    if end <= start:
        return 0
    if mcal is not None:
        try:
            cal = mcal.get_calendar("NYSE")
            sched = cal.schedule(start_date=start.isoformat(), end_date=end.isoformat())
            return max(0, len(sched.index) - 1)
        except Exception:
            pass
    days = 0
    cur = start
    while cur < end:
        cur = date.fromordinal(cur.toordinal() + 1)
        if cur.weekday() < 5:
            days += 1
    return days


def business_days_between(start: date, end: date) -> int:
    days = 0
    cur = start
    while cur < end:
        cur = date.fromordinal(cur.toordinal() + 1)
        if cur.weekday() < 5:
            days += 1
    return days


def lag_for(dataset: str, observation, as_of=None) -> int | None:
    cfg = THRESHOLDS.get(dataset)
    obs = _as_date(observation)
    now = _as_date(as_of) or date.today()
    if cfg is None or obs is None:
        return None
    if cfg["unit"] == "trading":
        return trading_days_between(obs, now)
    if cfg["unit"] == "business":
        return business_days_between(obs, now)
    return max(0, (now - obs).days)


def classify(dataset: str, observation, as_of=None) -> dict:
    """Return {status, lag, expected, warn, block, unit}.

    status: FRESH | EXPECTED_LAG | WARN | BLOCK | INVALID_DATE
    """
    cfg = THRESHOLDS.get(dataset)
    obs = _as_date(observation)
    now = _as_date(as_of) or date.today()
    if cfg is None:
        return {"status": "UNKNOWN_DATASET", "lag": None}
    if obs is None:
        return {"status": "INVALID_DATE", "lag": None, **cfg}
    lag = lag_for(dataset, obs, now)
    if lag is None:
        return {"status": "INVALID_DATE", "lag": None, **cfg}
    if lag <= cfg["expected"]:
        status = "FRESH" if lag == 0 else "EXPECTED_LAG"
    elif lag <= cfg["warn"]:
        status = "WARN"
    else:
        status = "BLOCK" if lag >= cfg["block"] else "WARN"
    return {"status": status, "lag": lag, **cfg}

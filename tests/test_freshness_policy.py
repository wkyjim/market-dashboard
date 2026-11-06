"""Freshness policy and price-audit lag tests (no network)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from freshness_policy import classify
from idea_price_audit import audit_ideas


def test_price_fresh_same_day():
    assert classify("equity_price", "2026-11-04", "2026-11-04")["status"] == "FRESH"


def test_price_one_day_is_expected_lag():
    out = classify("equity_price", "2026-11-03", "2026-11-04")
    assert out["status"] == "EXPECTED_LAG"
    assert out["lag"] == 1


def test_price_two_days_warns():
    assert classify("equity_price", "2026-11-02", "2026-11-04")["status"] == "WARN"


def test_price_three_days_blocks():
    assert classify("equity_price", "2026-10-30", "2026-11-04")["status"] == "BLOCK"


def test_macro_has_longer_expected_lag():
    assert classify("macro", "2026-11-03", "2026-11-05")["status"] in ("FRESH", "EXPECTED_LAG")


def test_invalid_date():
    assert classify("equity_price", "not-a-date", "2026-11-04")["status"] == "INVALID_DATE"


def _idea(date="2026-11-03", price=100.0):
    return {"ticker": "AAPL", "current_price": price, "price_date": date, "entry_price": price}


def test_audit_accepts_one_day_lag_with_warning():
    warns = []
    fails = audit_ideas([_idea()], lookup=lambda t: {"close": 100.0, "date": "2026-11-04"},
                        warnings=warns)
    assert fails == []
    assert warns and "1 trading day" in warns[0]


def test_audit_blocks_three_day_stale_price():
    fails = audit_ideas([_idea(date="2026-10-30")],
                        lookup=lambda t: {"close": 100.0, "date": "2026-11-04"})
    assert any("trading days behind" in f for f in fails)


def test_audit_blocks_future_date():
    fails = audit_ideas([_idea(date="2026-11-05")],
                        lookup=lambda t: {"close": 100.0, "date": "2026-11-04"})
    assert any("newer than" in f for f in fails)


def test_audit_blocks_missing_date():
    fails = audit_ideas([_idea(date="")],
                        lookup=lambda t: {"close": 100.0, "date": "2026-11-04"})
    assert any("missing or invalid" in f for f in fails)


def test_audit_allows_larger_move_when_lagging():
    fails = audit_ideas([_idea(price=105.0)],
                        lookup=lambda t: {"close": 100.0, "date": "2026-11-04"})
    assert fails == []

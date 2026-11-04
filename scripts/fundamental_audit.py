"""Deterministic SEC XBRL audit for stock-idea EPS inputs.

The report's valuation arithmetic can be internally consistent while the
underlying EPS is wrong (a single quarter presented as TTM, a stale pre-split
figure, or a full-year estimate below already-reported H1). This module
recomputes TTM and H1 diluted EPS from SEC company facts and blocks mismatches.

Fail closed: an unreachable SEC endpoint or unknown CIK is a blocking failure,
not a pass.
"""
from __future__ import annotations

import json
import urllib.request
from datetime import date

SEC_URL = "https://data.sec.gov/api/xbrl/companyconcept/CIK%s/us-gaap/EarningsPerShareDiluted.json"
USER_AGENT = "Hermes PM research contact@example.com"


def _days(start: str, end: str) -> int:
    try:
        return (date.fromisoformat(end) - date.fromisoformat(start)).days
    except Exception:
        return 0


def fetch_eps(cik: str, timeout: float = 15.0) -> dict | None:
    """Return {'quarters': [...], 'annual': [...]} for a 10-digit CIK."""
    cik = str(cik or "").strip().zfill(10)
    if not cik.isdigit():
        return None
    try:
        req = urllib.request.Request(SEC_URL % cik, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            payload = json.load(response)
    except Exception:
        return None
    rows = (payload.get("units") or {}).get("USD/shares") or []
    quarters, annual = [], []
    for row in rows:
        start, end, val = row.get("start"), row.get("end"), row.get("val")
        if not start or not end or not isinstance(val, (int, float)):
            continue
        span = _days(start, end)
        item = {"start": start, "end": end, "val": float(val), "form": row.get("form")}
        if 80 <= span <= 100:
            quarters.append(item)
        elif span >= 300:
            annual.append(item)
    def _dedupe(rows):
        seen = {}
        for row in rows:
            seen[(row["start"], row["end"])] = row
        return list(seen.values())

    return {"quarters": _dedupe(quarters), "annual": _dedupe(annual)}


def _q4_from_annual(annual: list, quarters: list) -> list:
    """Derive missing Q4 values as annual EPS minus the year's first three quarters."""
    out = []
    for a in sorted(annual, key=lambda x: x["end"])[-2:]:
        inside = {}
        for q in quarters:
            if a["start"] <= q["start"] and q["end"] <= a["end"]:
                inside[q["end"]] = q
        ordered = sorted(inside.values(), key=lambda q: q["end"])
        if len(ordered) == 3:
            out.append({"start": ordered[-1]["end"], "end": a["end"],
                        "val": round(a["val"] - sum(q["val"] for q in ordered), 4),
                        "form": "derived-Q4"})
    return out


def ttm_eps(facts: dict) -> float | None:
    quarters = list(facts.get("quarters") or [])
    quarters += _q4_from_annual(facts.get("annual") or [], quarters)
    quarters = sorted({(q["end"], q["val"]) for q in quarters})
    if len(quarters) < 4:
        return None
    return round(sum(v for _, v in quarters[-4:]), 4)


def h1_eps(facts: dict, fiscal_year_end: str | None = None) -> float | None:
    """Sum the first two quarters of the latest fiscal year present in the facts."""
    quarters = sorted(facts.get("quarters") or [], key=lambda q: q["end"])
    if len(quarters) < 2:
        return None
    if fiscal_year_end:
        year = [q for q in quarters if q["end"] <= fiscal_year_end]
        if len(year) >= 2:
            return round(year[0]["val"] + year[1]["val"], 4)
    return round(quarters[-2]["val"] + quarters[-1]["val"], 4)


def audit_fundamentals(ideas, lookup=fetch_eps, tolerance_pct: float = 2.0) -> list[str]:
    """Block TTM/H1 EPS that disagree with SEC XBRL."""
    fails: list[str] = []
    for i, idea in enumerate(ideas or []):
        if not isinstance(idea, dict):
            continue
        ticker = str(idea.get("ticker") or "").strip().upper()
        cik = str(idea.get("sec_cik") or "").strip()
        if not cik:
            fails.append("stock_ideas[%d] %s: sec_cik is required for SEC verification" % (i, ticker))
            continue
        facts = lookup(cik)
        if not facts:
            fails.append("stock_ideas[%d] %s: SEC XBRL unavailable for CIK %s" % (i, ticker, cik))
            continue
        sec_ttm = ttm_eps(facts)
        claimed_ttm = idea.get("ttm_eps_diluted")
        if sec_ttm is None:
            fails.append("stock_ideas[%d] %s: SEC facts do not contain four quarters" % (i, ticker))
        elif isinstance(claimed_ttm, (int, float)):
            if abs(float(claimed_ttm) - sec_ttm) > max(0.10, abs(sec_ttm) * tolerance_pct / 100.0):
                fails.append("stock_ideas[%d] %s: TTM EPS %.2f != SEC XBRL %.2f"
                             % (i, ticker, float(claimed_ttm), sec_ttm))
        claimed_h1 = idea.get("h1_eps_reported")
        if isinstance(claimed_h1, (int, float)):
            sec_h1 = h1_eps(facts)
            if sec_h1 is None:
                fails.append("stock_ideas[%d] %s: SEC facts do not contain H1 quarters" % (i, ticker))
            elif abs(float(claimed_h1) - sec_h1) > max(0.10, abs(sec_h1) * tolerance_pct / 100.0):
                fails.append("stock_ideas[%d] %s: H1 EPS %.2f != SEC XBRL %.2f"
                             % (i, ticker, float(claimed_h1), sec_h1))
    return fails

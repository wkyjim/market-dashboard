"""Immutable, versioned report-data object.

Every number that appears in the HTML is derived here once. The renderer and
validators consume the normalized copies, so a stale value from an earlier
run cannot leak into one section while another section uses a newer value.
"""
from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone

from financial_calc import valuation_object


@dataclass(frozen=True)
class ReportData:
    version: str
    run_id: str
    source_sha: str
    generated_at: str
    ai_score: float | None
    source_score: float | None
    factors: tuple
    sectors: tuple
    ideas: tuple
    allocation: tuple
    events: tuple

    def to_dict(self) -> dict:
        return asdict(self)


def _ai_score(adjustments: dict) -> float | None:
    scores = adjustments.get("factor_scores") or {}
    weights = adjustments.get("weights") or {}
    if not scores or set(scores) != set(weights):
        return None
    total = 0.0
    for key, score in scores.items():
        total += float(score) * float(weights[key])
    return round(total / 100.0, 4)


def _hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def build(d: dict, narrative: dict, adjustments: dict) -> ReportData:
    """Freeze regime, factors, sectors, ideas, allocation and events."""
    nv = narrative or {}
    adj = adjustments or {}
    source_score = (d.get("regime") or {}).get("score")
    ai_score = _ai_score(adj)

    factors = []
    for name, source_score_i in (d.get("regime_factors") or {}).items():
        factors.append({
            "name": name,
            "source_score": source_score_i,
            "source_weight": (d.get("regime_weights") or {}).get(name),
            "ai_score": (adj.get("factor_scores") or {}).get(name),
            "ai_weight": (adj.get("weights") or {}).get(name),
        })

    sectors = []
    for row in d.get("sectors") or []:
        sectors.append({
            "name": row.get("name"),
            "source_score": row.get("score"),
            "ai_score": (adj.get("sector_scores") or {}).get(row.get("name")),
            "rationale": (adj.get("sector_rationale") or {}).get(row.get("name")),
        })

    ideas = []
    for row in (nv.get("sections") or {}).get("stock_ideas") or []:
        if not isinstance(row, dict):
            continue
        canonical = valuation_object(row)
        frozen = {
            "ticker": row.get("ticker"),
            "recommendation": row.get("recommendation"),
            "current_price": row.get("current_price"),
            "price_date": row.get("price_date"),
            "fy2026_eps_consensus": row.get("fy2026_eps_consensus"),
            "fy2027_eps_consensus": row.get("fy2027_eps_consensus"),
            "fy2028_eps_consensus": row.get("fy2028_eps_consensus"),
            "ttm_eps_diluted": row.get("ttm_eps_diluted"),
            "valuation": canonical,
        }
        ideas.append(frozen)

    allocation = [
        {
            "horizon": r.get("horizon"),
            "sector": r.get("sector"),
            "benchmark_weight": r.get("benchmark_weight"),
            "portfolio_weight": r.get("portfolio_weight"),
            "active_weight": r.get("active_weight"),
        }
        for r in (nv.get("sections") or {}).get("sector_allocation") or []
        if isinstance(r, dict)
    ]

    events = [
        {"event": e.get("event"), "date": e.get("date"), "source": e.get("source")}
        for e in (nv.get("sections") or {}).get("economic_calendar") or []
        if isinstance(e, dict)
    ]

    payload = {
        "run_id": d.get("run_id"),
        "source_sha": (nv.get("source") or {}).get("latest_report_sha256"),
        "ai_score": ai_score,
        "source_score": source_score,
        "factors": factors,
        "sectors": sectors,
        "ideas": ideas,
        "allocation": allocation,
        "events": events,
    }
    return ReportData(
        version=_hash(payload),
        run_id=str(d.get("run_id") or ""),
        source_sha=str(payload["source_sha"] or ""),
        generated_at=datetime.now(timezone.utc).isoformat(),
        ai_score=ai_score,
        source_score=source_score,
        factors=tuple(payload["factors"]),
        sectors=tuple(payload["sectors"]),
        ideas=tuple(payload["ideas"]),
        allocation=tuple(payload["allocation"]),
        events=tuple(payload["events"]),
    )


def normalize_narrative(narrative: dict, data: ReportData) -> dict:
    """Replace every computed idea field with the canonical value."""
    out = copy.deepcopy(narrative)
    by_ticker = {str(i["ticker"]).upper(): i for i in data.ideas if i.get("ticker")}
    for row in (out.get("sections") or {}).get("stock_ideas") or []:
        if not isinstance(row, dict):
            continue
        frozen = by_ticker.get(str(row.get("ticker") or "").upper())
        if not frozen:
            continue
        for key, value in (frozen.get("valuation") or {}).items():
            if value is not None:
                row[key] = value
    return out


def normalize_adjustments(adjustments: dict, data: ReportData) -> dict:
    out = copy.deepcopy(adjustments or {})
    if data.ai_score is not None:
        out["regime_score"] = data.ai_score
    for factor in data.factors:
        if factor.get("ai_score") is not None:
            out.setdefault("factor_scores", {})[factor["name"]] = factor["ai_score"]
        if factor.get("ai_weight") is not None:
            out.setdefault("weights", {})[factor["name"]] = factor["ai_weight"]
    for sector in data.sectors:
        if sector.get("ai_score") is not None:
            out.setdefault("sector_scores", {})[sector["name"]] = sector["ai_score"]
    return out


def normalize_evidence(d: dict, data: ReportData) -> dict:
    out = copy.deepcopy(d)
    if data.source_score is not None:
        out.setdefault("regime", {})["score"] = data.source_score
    return out


def write(path: str, data: ReportData) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data.to_dict(), fh, indent=2, default=str)

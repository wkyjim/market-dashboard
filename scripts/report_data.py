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
    schema_version: str
    version: str
    run_id: str
    source_sha: str
    generated_at: str
    cutoff: str
    provenance: tuple
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


def _num(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _pe(price, eps):
    p, e = _num(price), _num(eps)
    if p is None or e is None:
        return "N/A"
    if e <= 0:
        return "N/M"
    return round(p / e, 4)


def _pe_block(row: dict) -> dict:
    price = row.get("current_price")
    return {
        "ttm_gaap_pe": _pe(price, row.get("ttm_eps_diluted")),
        "ttm_adjusted_pe": "N/A",
        "forward_gaap_pe_2027": _pe(price, row.get("fy2027_eps_consensus")),
        "forward_gaap_pe_2028": _pe(price, row.get("fy2028_eps_consensus")),
        "forward_adjusted_pe_2027": "N/A",
        "forward_adjusted_pe_2028": "N/A",
        "eps_basis": "GAAP",
        "forward_basis": "CONSENSUS",
        "price_observation_date": row.get("price_date"),
        "share_adjustment_basis": "SPLIT_ADJUSTED",
    }


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
            "pe": _pe_block(row),
            "sector": row.get("sector"),
            "research": {
                k: row.get(k) for k in (
                    "thesis", "review", "assumptions", "valuation_assumptions",
                    "peer_comparison", "sector_context", "catalysts", "risks",
                    "conclusion", "decision_rationale",
                )
            },
            "scenario": {
                "bull": {"eps": row.get("bull_eps"), "pe": row.get("bull_pe"),
                          "target": row.get("bull_target"), "prob": row.get("bull_prob"),
                          "rationale": row.get("bull_rationale")},
                "base": {"eps": row.get("base_eps"), "pe": row.get("base_pe"),
                          "target": row.get("base_target"), "prob": row.get("base_prob"),
                          "rationale": row.get("base_rationale")},
                "bear": {"eps": row.get("bear_eps"), "pe": row.get("bear_pe"),
                          "target": row.get("bear_target"), "prob": row.get("bear_prob"),
                          "rationale": row.get("bear_rationale")},
                "expected_price": row.get("expected_price"),
                "expected_return_pct": row.get("expected_return_pct"),
            },
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
        "schema_version": "1.0",
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
        schema_version="1.0",
        version=_hash(payload),
        run_id=str(d.get("run_id") or ""),
        source_sha=str(payload["source_sha"] or ""),
        generated_at=datetime.now(timezone.utc).isoformat(),
        cutoff=str(nv.get("cutoff") or d.get("data_cutoff") or ""),
        provenance=tuple(
            {"label": x.get("label"), "url": x.get("url"), "date": x.get("date")}
            for x in (nv.get("sources") or []) if isinstance(x, dict)
        ),
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
        for key, value in (frozen.get("pe") or {}).items():
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


def _md_escape(value) -> str:
    return str(value if value is not None else "N/A").replace("|", "\\|")


def write_markdown(path: str, data: ReportData) -> None:
    """Human-readable mirror of report-data.json; never a second source."""
    lines = [
        "# Report Data %s" % data.version,
        "",
        "- Schema: %s" % data.schema_version,
        "- Run ID: %s" % data.run_id,
        "- Generated: %s" % data.generated_at,
        "- Cutoff: %s" % (data.cutoff or "N/A"),
        "- AI score: %s / Source score: %s" % (data.ai_score, data.source_score),
        "",
        "## Stock ideas",
        "",
        "| Ticker | Rec | Price | TTM GAAP P/E | Fwd GAAP P/E 2027 | Fwd GAAP P/E 2028 |",
        "|---|---|---|---|---|---|",
    ]
    for idea in data.ideas:
        pe = idea.get("pe") or {}
        lines.append("| %s | %s | %s | %s | %s | %s |" % (
            _md_escape(idea.get("ticker")), _md_escape(idea.get("recommendation")),
            _md_escape(idea.get("current_price")), _md_escape(pe.get("ttm_gaap_pe")),
            _md_escape(pe.get("forward_gaap_pe_2027")), _md_escape(pe.get("forward_gaap_pe_2028"))))
    lines += ["", "## Allocation", "", "| Horizon | Sector | Benchmark | Portfolio | Active |", "|---|---|---|---|---|"]
    for row in data.allocation:
        lines.append("| %s | %s | %s | %s | %s |" % (
            _md_escape(row.get("horizon")), _md_escape(row.get("sector")),
            _md_escape(row.get("benchmark_weight")), _md_escape(row.get("portfolio_weight")),
            _md_escape(row.get("active_weight"))))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

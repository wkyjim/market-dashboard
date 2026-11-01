"""Narrative layer for the market-intelligence HTML report.

The deterministic builder (``generate_final_report.py``) owns every number in the
report.  This module lets an AI/agent add *prose* on top of those numbers without
being able to change them:

* ``build_evidence_pack(d, source_path)`` freezes the parsed numbers plus the
  source file's sha256.  The agent reads this pack, does its research, and writes
  a narrative JSON that references it.
* ``validate_narrative(narrative, evidence)`` rejects a narrative whose source
  hash does not match (stale narrative), whose sections are unknown, whose prose
  contains raw HTML, or whose numeric claims disagree with the evidence pack.
* ``render_narrative(narrative)`` turns the validated JSON into HTML fragments
  that the builder splices into fixed slots.  All text is escaped.

Design rule: prose may interpret numbers, never introduce them.  A narrative that
mentions a figure absent from the evidence pack fails validation and the run HALTs
before any file is written.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "aegis-narrative-v1"

# Sections the agent may author.  Order here is the render order.
ALLOWED_SECTIONS = (
    "exec_summary",          # list[str] -> <p> per paragraph, replaces the compact summary
    "cio_dashboard",         # str/list  -> paragraph under CIO Dashboard
    "what_matters",          # list[str] -> ordered list under #what-matters
    "risk_opportunity",      # str/list  -> Risk / Opportunity Balance
    "historical_analogs",    # str/list  -> Historical Analogs and Lessons
    "scorecard",             # str/list  -> Regime Scorecard commentary
    "scenarios_narrative",   # str/list  -> Scenarios commentary
    "macro_narrative",       # str/list  -> Macro View commentary
    "cross_asset_narrative", # str/list  -> Cross-Asset View commentary
    "equities_view",         # str/list  -> Broad US Equities View
    "price_action",          # str/list  -> Price Action / Breadth / Momentum
    "flows_narrative",       # str/list  -> Flows & Positioning commentary
    "portfolio_posture",     # str/list  -> Recommended Portfolio Posture
    "sector_narrative",      # str/list  -> Sector Rankings commentary
    "themes_narrative",      # str/list  -> Theme Rankings commentary
    "style_rotation",        # str/list  -> Style Rotation
    "factor_style",          # str/list  -> Factor & Style
    "trades_narrative",      # str/list  -> Trade Ideas rationale
    "heat_st_narrative",     # str/list  -> ST heat map commentary
    "heat_lt_narrative",     # str/list  -> LT heat map commentary
    "catalysts_narrative",   # str/list  -> Catalyst Watchlist commentary
    "risk_narrative",        # str/list  -> Key Risk Analysis commentary
    "conclusions",           # str/list  -> Highest-Conviction Conclusions
)

# Every section must be present for the full 24-section report. A missing slot
# renders an empty section and fails validation, so a weak run cannot silently
# degrade the structure.
REQUIRED_SECTIONS = ALLOWED_SECTIONS

MAX_SECTION_CHARS = 2000
MAX_TOTAL_CHARS = 24000


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _sha256_file(path: str | Path) -> str:
    return _sha256_text(Path(path).read_text(encoding="utf-8"))


def _flatten(d: dict, prefix: str = "") -> dict:
    """Flatten nested dicts into dotted paths, keeping only scalars."""
    out: dict = {}
    for key, value in d.items():
        name = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, dict):
            out.update(_flatten(value, name))
        elif isinstance(value, (int, float, str, bool)) or value is None:
            out[name] = value
    return out


def build_evidence_pack(d: dict, source_path: str | Path) -> dict:
    """Freeze the builder's parsed numbers with provenance for the narrative layer."""
    src = Path(source_path)
    raw = src.read_text(encoding="utf-8")
    metrics = _flatten(
        {
            "regime": d.get("regime") or {},
            "cio": {k: v for k, v in (d.get("cio") or {}).items() if k != "components"},
            "scenarios": d.get("scenarios") or {},
            "heat": d.get("heat") or {},
            "macro": d.get("macro") or {},
            "regime_factors": d.get("regime_factors") or {},
        }
    )
    # Components are flattened by name so prose can cite a component score.
    for comp in (d.get("cio") or {}).get("components") or []:
        if isinstance(comp, dict) and comp.get("name"):
            metrics[f"cio.components.{comp['name']}.score"] = comp.get("score")
            metrics[f"cio.components.{comp['name']}.weight"] = comp.get("weight")
            metrics[f"cio.components.{comp['name']}.contrib"] = comp.get("contrib")
    sectors = d.get("sectors") or []
    for row in sectors:
        if isinstance(row, dict) and row.get("name"):
            metrics[f"sectors.{row['name']}.score"] = row.get("score")
            metrics[f"sectors.{row['name']}.breadth_50"] = row.get("breadth_50")
            metrics[f"sectors.{row['name']}.positive_20d"] = row.get("positive_20d")
    themes = d.get("themes") or []
    for row in themes:
        if isinstance(row, dict) and row.get("name"):
            metrics[f"themes.{row['name']}.score"] = row.get("score")

    return {
        "schema": "aegis-evidence-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_path": str(src),
        "source_sha256": _sha256_text(raw),
        "source_mtime_utc": datetime.fromtimestamp(src.stat().st_mtime, timezone.utc).isoformat(timespec="seconds"),
        "data_cutoff": d.get("data_cutoff"),
        "data_cutoff_time": d.get("data_cutoff_time"),
        "run_id": d.get("run_id"),
        "sector_count": len(sectors),
        "theme_count": len(themes),
        "metrics": metrics,
    }


def load_narrative(path: str | Path) -> dict:
    """Load and structurally check a narrative JSON file."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("narrative must be a JSON object")
    return data


def _as_text_list(value) -> list[str] | None:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(v, str) for v in value):
        return value
    return None


def validate_narrative(narrative: dict, evidence: dict, tolerance: float = 0.02) -> list[str]:
    """Return a list of failures. Empty list means the narrative is safe to render."""
    fails: list[str] = []

    if narrative.get("schema") != SCHEMA:
        fails.append(f"schema mismatch: expected {SCHEMA!r}, got {narrative.get('schema')!r}")

    src = narrative.get("source") or {}
    expected = evidence.get("source_sha256")
    got = src.get("latest_report_sha256")
    if not expected:
        fails.append("evidence pack has no source_sha256; cannot verify narrative provenance")
    elif got != expected:
        fails.append(
            "narrative was written against a different latest-report.md "
            f"(narrative={got}, current={expected}); regenerate the narrative"
        )

    sections = narrative.get("sections")
    if not isinstance(sections, dict) or not sections:
        fails.append("sections missing or empty")
        sections = {}

    total = 0
    for name, value in sections.items():
        if name not in ALLOWED_SECTIONS:
            fails.append(f"unknown narrative section: {name!r}")
            continue
        texts = _as_text_list(value)
        if texts is None:
            fails.append(f"section {name!r} must be a string or list of strings")
            continue
        for text in texts:
            total += len(text)
            if not text.strip():
                fails.append(f"section {name!r} contains an empty entry")
            if "<" in text or ">" in text:
                fails.append(f"section {name!r} contains raw HTML angle brackets; prose must be plain text")
            if len(text) > MAX_SECTION_CHARS:
                fails.append(f"section {name!r} exceeds {MAX_SECTION_CHARS} chars in one entry")
    for name in REQUIRED_SECTIONS:
        if not (_as_text_list(sections.get(name)) or []):
            fails.append(f"required section {name!r} missing or empty")
    if total > MAX_TOTAL_CHARS:
        fails.append(f"narrative total length {total} exceeds {MAX_TOTAL_CHARS} chars")

    metrics = evidence.get("metrics") or {}
    claims = narrative.get("claims") or []
    if not isinstance(claims, list):
        fails.append("claims must be a list")
        claims = []
    for i, claim in enumerate(claims):
        if not isinstance(claim, dict):
            fails.append(f"claim[{i}] is not an object")
            continue
        path = claim.get("path")
        value = claim.get("value")
        if not path or path not in metrics:
            fails.append(f"claim[{i}] references unknown evidence path {path!r}")
            continue
        actual = metrics[path]
        if isinstance(actual, (int, float)) and isinstance(value, (int, float)):
            if abs(float(actual) - float(value)) > max(tolerance, abs(float(actual)) * tolerance):
                fails.append(
                    f"claim[{i}] {path}: narrative says {value}, evidence says {actual}"
                )
        elif actual != value:
            fails.append(f"claim[{i}] {path}: narrative says {value!r}, evidence says {actual!r}")

    # AI re-rating layer. latest-report.md carries facts (market/macro/econ/
    # technical data) plus rule-based judgment scores. The model may re-examine
    # and adjust the JUDGMENT scores from its own research; facts stay frozen.
    # Adjusted values are disclosed beside the source values (§54A §16).
    adj = narrative.get("adjustments")
    if adj is None:
        fails.append("adjustments is required: AI must re-rate regime_score and all 11 sector_scores")
        adj = {}
    elif not isinstance(adj, dict):
        fails.append("adjustments must be an object")
        adj = {}
    elif not adj:
        fails.append("adjustments is empty: AI must re-rate regime_score and all 11 sector_scores")
    adj_values: list = []
    if adj:
        rat = adj.get("rationale")
        if not isinstance(rat, str) or len(rat) < 80 or len(rat) > 2000:
            fails.append("adjustments.rationale must be a string between 80 and 2000 chars")

        rs = adj.get("regime_score")
        if rs is None:
            fails.append("adjustments.regime_score is required: AI must state its own regime judgment")
        elif not isinstance(rs, (int, float)) or not (0 <= float(rs) <= 100):
            fails.append("adjustments.regime_score must be a number in 0-100")
        else:
            adj_values.append(float(rs))
            src = metrics.get("regime.score")
            if isinstance(src, (int, float)) and abs(float(rs) - float(src)) > 25:
                fails.append(
                    "adjustments.regime_score %.2f is more than 25 points from source %.2f"
                    % (float(rs), float(src)))

        rl = adj.get("regime_label")
        if rl is not None and (not isinstance(rl, str) or len(rl) > 60):
            fails.append("adjustments.regime_label must be a string of at most 60 chars")

        ss = adj.get("sector_scores")
        if ss is not None:
            if not isinstance(ss, dict) or not ss:
                fails.append("adjustments.sector_scores must be a non-empty object")
            else:
                known = {k.split(".")[1] for k in metrics
                         if k.startswith("sectors.") and k.endswith(".score")}
                for name, val in ss.items():
                    if name not in known:
                        fails.append("adjustments.sector_scores unknown sector %r" % name)
                        continue
                    if not isinstance(val, (int, float)) or not (0 <= float(val) <= 100):
                        fails.append("adjustments.sector_scores[%r] must be a number in 0-100" % name)
                        continue
                    adj_values.append(float(val))
                    src = metrics.get("sectors.%s.score" % name)
                    if isinstance(src, (int, float)) and abs(float(val) - float(src)) > 30:
                        fails.append(
                            "adjustments.sector_scores[%r] %.2f is more than 30 points from source %.2f"
                            % (name, float(val), float(src)))
                missing = sorted(known - set(ss.keys()))
                if missing:
                    fails.append("adjustments.sector_scores missing sectors: " + ", ".join(missing))

    # Every decimal in the prose must trace to the evidence pack, an explicit
    # claim, or an AI-adjusted score.
    numeric_mentions = set()
    for text in sections.values():
        for t in (_as_text_list(text) or []):
            numeric_mentions.update(re.findall(r"\b\d+\.\d+\b", t))
    metric_values = [float(v) for v in metrics.values() if isinstance(v, (int, float))]
    claim_values = [float(c.get("value")) for c in claims
                    if isinstance(c, dict) and isinstance(c.get("value"), (int, float))]
    allowed_values = metric_values + claim_values + adj_values
    unclaimed = []
    for tok in sorted(numeric_mentions):
        try:
            d = float(tok)
        except ValueError:
            continue
        if any(abs(d - v) <= max(tolerance, abs(v) * tolerance) for v in allowed_values):
            continue
        unclaimed.append(tok)
    if unclaimed:
        fails.append(
            "prose contains numbers not found in the evidence pack (add each to claims[] with its path): "
            + ", ".join(unclaimed[:15])
        )

    return fails


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_narrative(narrative: dict) -> dict:
    """Render validated narrative sections into HTML fragments keyed by slot."""
    sections = narrative.get("sections") or {}
    out: dict = {}

    exec_texts = _as_text_list(sections.get("exec_summary")) or []
    if exec_texts:
        out["exec_summary"] = "\n".join(f"<p>{_esc(t)}</p>" for t in exec_texts)

    matters = _as_text_list(sections.get("what_matters")) or []
    if matters:
        items = "".join(f"<li>{_esc(t)}</li>" for t in matters)
        out["what_matters"] = f"<ol>{items}</ol>"

    for key in ALLOWED_SECTIONS:
        if key in ("exec_summary", "what_matters"):
            continue
        texts = _as_text_list(sections.get(key)) or []
        if texts:
            out[key] = "\n".join(f"<p>{_esc(t)}</p>" for t in texts)

    return out

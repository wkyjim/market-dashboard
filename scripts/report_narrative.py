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
import os
import re

from financial_calc import compare_valuation, qc_probabilities, target_price as calc_target_price
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

OPTIONAL_IDEA_FIELDS = {
    "revenue_ttm", "operating_margin_pct", "ps_ratio", "pb_ratio",
    "fy2027_revenue_consensus", "fy2028_revenue_consensus",
    "revenue_growth_2027_2028_pct", "fundamentals_source", "decision_rationale",
    "ttm_gaap_pe", "ttm_adjusted_pe", "forward_gaap_pe_2027", "forward_gaap_pe_2028",
    "forward_adjusted_pe_2027", "forward_adjusted_pe_2028", "forward_basis",
    "price_observation_date", "share_adjustment_basis",
}

SCHEMA = "aegis-narrative-v1"

# Sections the agent may author.  Order here is the render order.
ALLOWED_SECTIONS = (
    "exec_summary",          # list[str] -> <p> per paragraph, replaces the compact summary
    "what_matters",          # list[str] -> ordered list under #what-matters
    "risk_opportunity",      # str/list  -> Risk / Opportunity Balance
    "historical_analogs",    # str/list  -> Historical Analogs and Lessons
    "scorecard",             # str/list  -> AI Regime Scorecard commentary
    "forward_signal",        # str/list  -> 5D/20D/60D forward-signal restatement
    "scenarios_narrative",   # str/list  -> Scenarios commentary
    "macro_narrative",       # str/list  -> Macro View commentary
    "macro_outlook",         # rows      -> forward macro view table (1-3M / 6-12M)
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
    "candidate_screen",      # rows      -> 8-15 candidate discovery table
    "stock_ideas",           # rows      -> high-conviction single-stock ideas
    "heat_st_narrative",     # str/list  -> ST heat map commentary
    "heat_lt_narrative",     # str/list  -> LT heat map commentary
    "catalysts_narrative",   # str/list  -> Catalyst Watchlist commentary
    "risk_narrative",        # str/list  -> Key Risk Analysis commentary
    "portfolio_risk",        # rows      -> portfolio risk / correlation / sizing table
    "sector_allocation",     # rows      -> 11 GICS benchmark/portfolio/active weights
    "conclusions",           # str/list  -> Highest-Conviction Conclusions
)

# Every section must be present for the full 24-section report. A missing slot
# renders an empty section and fails validation, so a weak run cannot silently
# degrade the structure.
REQUIRED_SECTIONS = ALLOWED_SECTIONS

MAX_SECTION_CHARS = 2000
MAX_TOTAL_CHARS = 24000

# External citations. Unlike prose sections these are structured records, so the
# renderer can emit real <a href> links. The whole point of the citation block is
# to show the reader WHICH outside sources informed the narrative — an AI report
# that only cites latest-report.md is just restating the rule engine.
MAX_SOURCES = 40
SOURCE_FIELDS = ("label", "url", "note")
# A narrative that cites only latest-report.md is restating the rule engine, not
# doing independent research. Require real outside sources so the citation block
# proves the model actually looked beyond the pipeline snapshot.
#
# 10 URLs is the breadth floor the operator set: 4 example categories in the old
# prompt produced exactly 4 citations, so the floor has to be high enough that
# hitting it is itself evidence of research. MIN_DOMAINS stops ten pages from one
# institution counting as breadth.
MIN_SOURCES = 10
MIN_DOMAINS = 4

# Second-level labels that usually sit directly under a public suffix. Used only
# to keep "federalreserve.gov" and "api.federalreserve.gov" in the same bucket.
_MULTI_PART_SUFFIXES = {"co", "com", "gov", "org", "ac", "net", "edu", "go"}


def _registered_domain(url: str) -> str:
    """Return the registrable domain for a URL, or '' when it cannot be parsed.

    Deliberately heuristic: no public-suffix list dependency. Good enough to keep
    bls.gov / bea.gov / federalreserve.gov / treasury.gov in separate buckets.
    """
    try:
        host = urlsplit(url.strip()).netloc.lower()
    except ValueError:
        return ""
    host = host.split("@")[-1].split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    labels = [p for p in host.split(".") if p]
    if len(labels) < 2:
        return host
    if len(labels) >= 3 and labels[-2] in _MULTI_PART_SUFFIXES:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:])


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


def _previous_idea_tickers() -> list[str]:
    """Tickers of the currently published idea cards (for reassessment honesty)."""
    try:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        html = ""
        try:
            out = subprocess.run(
                ["git", "-C", root, "show", "HEAD:data/market-intelligence-report.html"],
                capture_output=True, text=True, timeout=10,
            )
            if out.returncode == 0:
                html = out.stdout
        except Exception:
            html = ""
        if not html:
            path = os.path.join(root, "data", "market-intelligence-report.html")
            if not os.path.exists(path):
                return []
            with open(path, encoding="utf-8") as fh:
                html = fh.read()
        return sorted({t.upper() for t in re.findall(
            r'<div class="idea-card">\s*<h3>([A-Z][A-Z0-9.\-]*)', html)})
    except Exception:
        return []


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

    # Source (rule-based) regime weights in points, and the source engine's
    # forward-signal calibration. Both are frozen inputs the AI layer may only
    # quote or diverge from within the documented bounds.
    for factor, weight in (d.get("regime_weights") or {}).items():
        if isinstance(weight, (int, float)):
            metrics[f"regime_weights.{factor}"] = float(weight)
    for row in d.get("forward_signal") or []:
        if isinstance(row, dict) and row.get("horizon"):
            h = str(row["horizon"])
            metrics[f"forward_signal.{h}.mean_pct"] = row.get("mean_pct")
            metrics[f"forward_signal.{h}.bucket"] = row.get("bucket")
            metrics[f"forward_signal.{h}.n"] = row.get("n")
            metrics[f"forward_signal.{h}.direction"] = row.get("direction")

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
        "previous_ideas": _previous_idea_tickers(),
        "metrics": metrics,
    }


def load_narrative(path: str | Path) -> dict:
    """Load and structurally check a narrative JSON file."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("narrative must be a JSON object")
    return data


HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")


def _has_html_tag(text: str) -> bool:
    """True only for real HTML tags. Comparison operators like 'Breadth < 60%'
    are plain text and must pass — the renderer escapes them to &lt; anyway."""
    return bool(HTML_TAG_RE.search(text))


def _as_text_list(value) -> list[str] | None:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(v, str) for v in value):
        return value
    return None


# Structured table sections. When the narrative supplies a list of dicts for one
# of these keys, the renderer emits a real <table> matching the c62d023 layout
# instead of a paragraph block. A plain string or list[str] still falls back to
# paragraphs, so older narratives keep rendering.
TABLE_SECTIONS = {
    "risk_opportunity": (
        ("label", "Opportunity / Risk"),
        ("why", "Why it exists"),
        ("priced", "What appears priced"),
        ("view", "Our view"),
        ("expression", "Portfolio expression"),
        ("changes_view", "What changes the view"),
    ),
    "factor_style": (
        ("factor", "Factor"),
        ("signal", "Signal"),
        ("exposure", "Exposure"),
        ("notes", "Notes"),
    ),
    "macro_outlook": (
        ("factor", "Factor"),
        ("view_1_3m", "1-3M view"),
        ("view_6_12m", "6-12M view"),
        ("drivers", "Drivers"),
        ("invalidation", "Invalidation"),
    ),
    "candidate_screen": (
        ("ticker", "Ticker"),
        ("name", "Name"),
        ("sector", "Sector"),
        ("signal", "Signal"),
        ("verdict", "Verdict"),
        ("reason", "Why selected / rejected"),
    ),
    "sector_allocation": (
        ("horizon", "Horizon"),
        ("sector", "GICS sector"),
        ("benchmark_weight", "Benchmark wt %"),
        ("portfolio_weight", "Portfolio wt %"),
        ("active_weight", "Active wt %"),
        ("rationale", "Sizing rationale"),
    ),
    "portfolio_risk": (
        ("risk", "Risk"),
        ("exposure", "Exposure"),
        ("correlation", "Correlation"),
        ("sizing", "Sizing"),
        ("hedge", "Hedge"),
        ("notes", "Notes"),
    ),
}

# Single-stock ideas are rendered as cards, not a wide table: each idea carries
# a thesis, explicit assumptions, three price scenarios and an invalidation.
CARD_SECTIONS = {
    "stock_ideas": (
        "ticker", "name", "sector", "security_type", "recommendation", "horizon",
        "current_price", "price_date", "entry_price", "base_target", "bull_target", "bear_target",
        "upside_pct", "downside_pct", "return_from_current_pct", "risk_reward",
        "thesis", "review", "assumptions", "why_vs_alternatives", "contrary",
        "peer_comparison", "sector_context", "conclusion", "decision_rationale",
        "catalysts", "risks", "entry_condition", "exit", "invalidation",
        "opposing", "reassess", "verification", "sources",
        # --- valuation block (P0) ---
        "ttm_eps_diluted", "ttm_pe",
        "fy2026_eps_consensus", "fy2027_eps_consensus", "fy2028_eps_consensus",
        "fwd_pe_2027", "fwd_pe_2028",
        "eps_growth_2026_2028_pct", "eps_revision_pct",
        "pe_3y_median", "pe_3y_min", "pe_3y_max", "pe_3y_percentile",
        "pe_5y_median", "pe_5y_min", "pe_5y_max", "pe_5y_percentile",
        "fwd_pe_premium_vs_median_pct",
        "bull_eps", "bull_pe", "base_eps", "base_pe", "bear_eps", "bear_pe",
        "bull_rationale", "base_rationale", "bear_rationale",
        "bull_prob", "base_prob", "bear_prob", "expected_price", "expected_return_pct",
        "probability_basis", "override_reason",
        "valuation_method", "valuation_assumptions",
        # --- fundamental data integrity (P0) ---
        "sec_cik", "eps_basis", "ttm_period", "ttm_eps_quarters", "split_adjusted",
        "revenue_ttm", "operating_margin_pct", "ps_ratio", "pb_ratio",
        "fy2027_revenue_consensus", "fy2028_revenue_consensus", "revenue_growth_2027_2028_pct",
        "fundamentals_source",
        "ttm_eps_source", "consensus_source", "pe_history_source",
        "pe_history_years", "pe_history_basis", "eps_revision_source",
        "fy2027_eps_method", "fy2028_eps_method",
        "h1_eps_reported", "h2_eps_forecast", "h2_rationale",
        "fy_revenue", "fy_net_margin_pct", "fy_tax_rate_pct", "fy_diluted_shares",
        "valuation_provenance",
    ),
}


def _render_table_rows(rows: list, columns: tuple) -> str | None:
    """Render a list of dicts as a <table>. Returns None when rows are unusable."""
    if not isinstance(rows, list) or not rows:
        return None
    if not all(isinstance(r, dict) for r in rows):
        return None
    head = "".join(f"<th>{_esc(title)}</th>" for _, title in columns)
    body = []
    for row in rows:
        cells = []
        for key, _ in columns:
            raw = row.get(key)
            if raw is None:
                cells.append("<td></td>")
                continue
            text = str(raw).strip()
            cls = ""
            if key == "exposure":
                try:
                    num = float(text.rstrip("%"))
                    cls = ' class="pos"' if num >= 0 else ' class="neg"'
                except ValueError:
                    cls = ""
            cells.append(f"<td{cls}>{_esc(text)}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    return (
        "<table><thead><tr>" + head + "</tr></thead><tbody>\n"
        + "\n".join(body)
        + "\n</tbody></table>"
    )


def compute_ai_regime_score(adj: dict | None) -> float | None:
    """Return Σ(factor_score × weight)/100 for a two-step AI adjustment.

    The AI regime score is never taken from the model as a bare assertion: it is
    computed from the two auditable inputs the model supplies. Returns None when
    either input set is missing or does not cover the same factors, so a partial
    adjustment cannot masquerade as a complete one.
    """
    if not isinstance(adj, dict):
        return None
    scores = adj.get("factor_scores")
    weights = adj.get("weights")
    if not isinstance(scores, dict) or not isinstance(weights, dict) or not scores or not weights:
        return None
    if set(scores) != set(weights):
        return None
    total = 0.0
    for key in scores:
        score, weight = scores[key], weights[key]
        if not isinstance(score, (int, float)) or not isinstance(weight, (int, float)):
            return None
        total += float(score) * float(weight)
    return round(total / 100.0, 2)


def _parse_report_date(evidence: dict):
    """Parse the evidence pack's human date (e.g. '3 November 2026') to datetime."""
    raw = str((evidence or {}).get("data_cutoff") or "").strip()
    for fmt in ("%d %B %Y", "%d %b %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue
    return None


def _validate_candidate_screen(rows, stock_tickers: set, fails: list[str]) -> None:
    """Validate the 8-15 candidate discovery table and its link to selected ideas."""
    if not isinstance(rows, list) or not rows:
        fails.append("candidate_screen must be a non-empty list of candidate rows")
        return
    if not (8 <= len(rows) <= 15):
        fails.append("candidate_screen must contain 8-15 candidates (got %d)" % len(rows))
    verdicts = {"Selected", "Watchlist", "Rejected", "No-Trade"}
    tickers: set = set()
    selected: set = set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            fails.append("candidate_screen[%d] is not an object" % i)
            continue
        missing = [k for k in ("ticker", "name", "sector", "signal", "verdict", "reason")
                   if k not in row]
        if missing:
            fails.append("candidate_screen[%d] missing fields: %s" % (i, ", ".join(missing)))
            continue
        ticker = str(row.get("ticker") or "").strip()
        verdict = str(row.get("verdict") or "").strip()
        reason = str(row.get("reason") or "").strip()
        if not ticker:
            fails.append("candidate_screen[%d].ticker is empty" % i)
        elif ticker in tickers:
            fails.append("candidate_screen[%d].ticker duplicated: %s" % (i, ticker))
        else:
            tickers.add(ticker)
        if verdict not in verdicts:
            fails.append("candidate_screen[%d].verdict must be one of %s" % (i, sorted(verdicts)))
        if verdict == "Selected":
            selected.add(ticker)
        if not reason:
            fails.append("candidate_screen[%d].reason is empty" % i)
        elif len(reason) > 300:
            fails.append("candidate_screen[%d].reason exceeds 300 chars" % i)
    if not (3 <= len(selected) <= 5):
        fails.append("candidate_screen must mark 3-5 candidates as Selected (got %d)" % len(selected))
    if stock_tickers and selected != stock_tickers:
        fails.append("candidate_screen Selected tickers %s do not match stock_ideas tickers %s"
                     % (sorted(selected), sorted(stock_tickers)))


def _num_or_none(value):
    """Parse a numeric field; N/M, N/A and blanks return None."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip().replace(",", "")
        if text.upper() in ("N/M", "N/A", "NA", ""):
            return None
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _validate_assumption_labels(row: dict, i: int) -> list[str]:
    """Catch EPS-period label shifts and wrong multiple-direction prose."""
    fails: list[str] = []
    text = " ".join(str(row.get(k) or "") for k in ("valuation_assumptions", "assumptions"))
    if not text.strip():
        return fails
    for year, field in ((2026, "fy2026_eps_consensus"), (2027, "fy2027_eps_consensus"),
                        (2028, "fy2028_eps_consensus")):
        actual = _num_or_none(row.get(field))
        short = str(year)[2:]
        if actual is None:
            if re.search(r"(?:FY%s|FY%s)[^.]{0,30}?EPS" % (year, short), text):
                fails.append("stock_ideas[%d].valuation_assumptions claims FY%s EPS but the "
                             "FY%s field is N/A (period shift)" % (i, year, year))
            continue
        for m in re.finditer(r"(?:FY%s|FY%s)\s*(?:EPS)?\s*\$?([0-9]+\.[0-9]+)"
                             % (year, short), text):
            claimed = float(m.group(1))
            if abs(claimed - actual) > max(0.05, abs(actual) * 0.01):
                fails.append("stock_ideas[%d].valuation_assumptions labels %.2f as FY%s EPS, "
                             "but canonical FY%s EPS is %.2f (period shift)"
                             % (i, claimed, year, year, actual))
    for year, field in ((2027, "fwd_pe_2027"), (2028, "fwd_pe_2028")):
        actual = _num_or_none(row.get(field))
        if actual is None:
            continue
        m = re.search(r"([0-9]+\.[0-9]+)x\s*on\s*FY%s" % year, text, re.I)
        if m and abs(float(m.group(1)) - actual) > max(0.1, actual * 0.02):
            fails.append("stock_ideas[%d].valuation_assumptions says %.1fx on FY%s, "
                         "but Forward P/E is %.2f" % (i, float(m.group(1)), year, actual))
    base_eps = _num_or_none(row.get("base_eps"))
    base_pe = _num_or_none(row.get("base_pe"))
    bm = re.search(r"base[^(]{0,80}?\(([0-9.]+)\s*x\s*([0-9.]+)x\)", text, re.I)
    if bm and base_eps and base_pe:
        if abs(float(bm.group(1)) - base_eps) > max(0.05, abs(base_eps) * 0.01) or \
                abs(float(bm.group(2)) - base_pe) > max(0.1, abs(base_pe) * 0.02):
            fails.append("stock_ideas[%d].valuation_assumptions base line %.2f x %.2fx != scenario "
                         "base %.2f x %.2fx" % (i, float(bm.group(1)), float(bm.group(2)), base_eps, base_pe))
    m = re.search(r"compression[^.]{0,80}?from\s*([0-9.]+)x?\s*to\s*([0-9.]+)x", text, re.I)
    if m and float(m.group(2)) > float(m.group(1)):
        fails.append("stock_ideas[%d].valuation_assumptions calls %.1fx -> %.1fx "
                     "'compression' but the multiple expands" % (i, float(m.group(1)), float(m.group(2))))
    return fails


def _validate_valuation(row: dict, i: int, fails: list[str], global_sources: dict) -> None:
    """Deterministic valuation reconciliation: EPS x P/E = target, P/E math, ranges."""
    cur = _num_or_none(row.get("current_price"))
    method = str(row.get("valuation_method") or "").strip()
    if method not in ("P/E", "EV/EBITDA", "FCF yield", "DCF", "SOTP", "Other"):
        fails.append("stock_ideas[%d].valuation_method must be one of P/E, EV/EBITDA, "
                     "FCF yield, DCF, SOTP, Other" % i)
    if not str(row.get("valuation_assumptions") or "").strip():
        fails.append("stock_ideas[%d].valuation_assumptions is empty" % i)

    ttm_eps = _num_or_none(row.get("ttm_eps_diluted"))
    ttm_pe = _num_or_none(row.get("ttm_pe"))
    if ttm_eps is None:
        qs = row.get("ttm_eps_quarters")
        if isinstance(qs, list) and len(qs) == 4 and all(_num_or_none(q) is not None for q in qs):
            fails.append("stock_ideas[%d].ttm_eps_diluted must be numeric when four quarters are provided" % i)
        if str(row.get("ttm_pe") or "").strip().upper() not in ("N/M", "N/A"):
            fails.append("stock_ideas[%d].ttm_pe must be N/M or N/A when TTM EPS is unavailable" % i)
    elif ttm_eps <= 0:
        if str(row.get("ttm_pe") or "").strip().upper() != "N/M":
            fails.append("stock_ideas[%d]: nonpositive TTM EPS requires ttm_pe='N/M'" % i)
    elif cur and ttm_pe is not None:
        expected = cur / ttm_eps
        if abs(ttm_pe / expected - 1.0) > 0.02:
            fails.append("stock_ideas[%d].ttm_pe %.2f != current_price/TTM EPS %.2f"
                         % (i, ttm_pe, expected))

    for year, eps_key, pe_key in (
        ("2027", "fy2027_eps_consensus", "fwd_pe_2027"),
        ("2028", "fy2028_eps_consensus", "fwd_pe_2028"),
    ):
        eps = _num_or_none(row.get(eps_key))
        pe = _num_or_none(row.get(pe_key))
        if eps is None:
            continue
        if eps <= 0:
            if str(row.get(pe_key) or "").strip().upper() != "N/M":
                fails.append("stock_ideas[%d]: nonpositive FY%s EPS requires %s='N/M'"
                             % (i, year, pe_key))
        elif cur and pe is not None:
            expected = cur / eps
            if abs(pe / expected - 1.0) > 0.02:
                fails.append("stock_ideas[%d].%s %.2f != current_price/FY%s EPS %.2f"
                             % (i, pe_key, pe, year, expected))

    e26 = _num_or_none(row.get("fy2026_eps_consensus"))
    e28 = _num_or_none(row.get("fy2028_eps_consensus"))
    growth = _num_or_none(row.get("eps_growth_2026_2028_pct"))
    if e26 and e28 and e26 > 0 and e28 > 0 and growth is not None:
        expected = (e28 / e26 - 1.0) * 100.0
        if abs(growth - expected) > 0.5:
            fails.append("stock_ideas[%d].eps_growth_2026_2028_pct %.2f != (FY28/FY26-1)*100 %.2f"
                         % (i, growth, expected))

    r27 = _num_or_none(row.get("fy2027_revenue_consensus"))
    r28 = _num_or_none(row.get("fy2028_revenue_consensus"))
    rg = _num_or_none(row.get("revenue_growth_2027_2028_pct"))
    if r27 and r28 and r27 > 0 and rg is not None:
        expected = (r28 / r27 - 1.0) * 100.0
        if abs(rg - expected) > 0.5:
            fails.append("stock_ideas[%d].revenue_growth_2027_2028_pct %.2f != "
                         "(FY28/FY27-1)*100 %.2f" % (i, rg, expected))
    missing_fund = [k for k in ("revenue_ttm", "operating_margin_pct", "ps_ratio",
                                 "pb_ratio", "fy2027_revenue_consensus")
                    if _num_or_none(row.get(k)) is None]
    if missing_fund:
        fails.append("stock_ideas[%d]: CMC/Yahoo fundamentals must be populated (%s); "
                     "run scripts/fundamentals_web.py --ticker <T>"
                     % (i, ", ".join(missing_fund)))
    fund_src = str(row.get("fundamentals_source") or "")
    if any(_num_or_none(row.get(k)) is not None for k in
           ("revenue_ttm", "operating_margin_pct", "ps_ratio", "pb_ratio")):
        if "companiesmarketcap.com" not in fund_src:
            fails.append("stock_ideas[%d].fundamentals_source must cite companiesmarketcap.com" % i)
    if (r27 is not None or r28 is not None) and "finance.yahoo.com" not in str(row.get("consensus_source") or ""):
        fails.append("stock_ideas[%d]: revenue consensus requires consensus_source citing finance.yahoo.com" % i)

    for prefix in ("pe_3y", "pe_5y"):
        med = _num_or_none(row.get(prefix + "_median"))
        lo = _num_or_none(row.get(prefix + "_min"))
        hi = _num_or_none(row.get(prefix + "_max"))
        pct = _num_or_none(row.get(prefix + "_percentile"))
        if None not in (med, lo, hi) and not (lo <= med <= hi):
            fails.append("stock_ideas[%d].%s range is not min <= median <= max" % (i, prefix))
        if pct is not None and not (0 <= pct <= 100):
            fails.append("stock_ideas[%d].%s_percentile must be 0-100" % (i, prefix))

    fpe = _num_or_none(row.get("fwd_pe_2027"))
    med5 = _num_or_none(row.get("pe_5y_median"))
    premium = _num_or_none(row.get("fwd_pe_premium_vs_median_pct"))
    if fpe and med5 and premium is not None:
        expected = (fpe / med5 - 1.0) * 100.0
        if abs(premium - expected) > 0.5:
            fails.append("stock_ideas[%d].fwd_pe_premium_vs_median_pct %.2f != "
                         "(fwd P/E / 5Y median - 1)*100 %.2f" % (i, premium, expected))

    # --- fundamental data integrity (P0) ---
    basis = str(row.get("eps_basis") or "").strip()
    if basis not in ("GAAP", "non-GAAP"):
        fails.append("stock_ideas[%d].eps_basis must be GAAP or non-GAAP" % i)
    period = str(row.get("ttm_period") or "").strip()
    if not period:
        fails.append("stock_ideas[%d].ttm_period is empty" % i)
    elif not (("TTM" in period.upper()) or ("Q" in period.upper() and "-" in period)):
        fails.append("stock_ideas[%d].ttm_period must describe four quarters "
                     "(e.g. 'Q4 2025-Q3 2026'), not a single quarter" % i)
    if row.get("split_adjusted") is not True:
        fails.append("stock_ideas[%d].split_adjusted must be true for TTM/forward EPS" % i)

    quarters = row.get("ttm_eps_quarters")
    if not isinstance(quarters, list) or len(quarters) != 4:
        fails.append("stock_ideas[%d].ttm_eps_quarters must be a list of 4 quarterly EPS values" % i)
    else:
        vals = [_num_or_none(q) for q in quarters]
        if any(v is None for v in vals):
            fails.append("stock_ideas[%d].ttm_eps_quarters must all be numeric" % i)
        elif ttm_eps is not None and ttm_eps > 0:
            total = sum(vals)
            if abs(total - ttm_eps) > max(0.05, abs(ttm_eps) * 0.005):
                fails.append("stock_ideas[%d].ttm_eps_diluted %.2f != sum(ttm_eps_quarters) %.2f"
                             % (i, ttm_eps, total))

    def _src_ok(url, need=()):
        u = str(url or "").strip()
        if not u or u.upper() == "N/A" or u not in global_sources:
            return False
        note = global_sources[u].lower()
        return any(k in note for k in need) if need else True

    if not _src_ok(row.get("ttm_eps_source"),
                   ("10-q", "10-k", "earnings", "filing", "results")):
        fails.append("stock_ideas[%d].ttm_eps_source must be a dated filing/earnings URL "
                     "listed in global sources" % i)
    if _num_or_none(row.get("pe_5y_median")) is not None:
        if not _src_ok(row.get("pe_history_source")):
            fails.append("stock_ideas[%d].pe_history_source required when 5Y P/E stats are provided" % i)
        yrs = _num_or_none(row.get("pe_history_years"))
        if yrs is None or yrs < 5:
            fails.append("stock_ideas[%d].pe_history_years must be >= 5 when 5Y P/E stats are provided" % i)
    if _num_or_none(row.get("eps_revision_pct")) is not None:
        if not _src_ok(row.get("eps_revision_source")):
            fails.append("stock_ideas[%d].eps_revision_source required when eps_revision_pct is provided" % i)

    h1 = _num_or_none(row.get("h1_eps_reported"))
    h2 = _num_or_none(row.get("h2_eps_forecast"))
    fy27 = _num_or_none(row.get("fy2027_eps_consensus"))
    if h1 is not None and fy27 is not None:
        if h2 is None:
            fails.append("stock_ideas[%d].h2_eps_forecast required when h1_eps_reported and "
                         "FY2027 EPS are provided" % i)
        elif abs((h1 + h2) - fy27) > max(0.05, abs(fy27) * 0.02):
            fails.append("stock_ideas[%d]: FY2027 EPS %.2f != H1 reported %.2f + H2 forecast %.2f"
                         % (i, fy27, h1, h2))
        elif h1 > 0 and h2 < 0.5 * h1 and not str(row.get("h2_rationale") or "").strip():
            fails.append("stock_ideas[%d]: H2 forecast %.2f is below half of H1 %.2f; "
                         "provide h2_rationale (e.g. export restriction, one-off charge)"
                         % (i, h2, h1))

    if str(row.get("fy2027_eps_method") or "").strip() == "AI_FORECAST":
        rev = _num_or_none(row.get("fy_revenue"))
        margin = _num_or_none(row.get("fy_net_margin_pct"))
        tax = _num_or_none(row.get("fy_tax_rate_pct"))
        shares = _num_or_none(row.get("fy_diluted_shares"))
        if None in (rev, margin, tax, shares) or shares <= 0:
            fails.append("stock_ideas[%d]: AI_FORECAST requires fy_revenue, fy_net_margin_pct, "
                         "fy_tax_rate_pct and fy_diluted_shares" % i)
        elif fy27 is not None:
            implied = (rev * (margin / 100.0) * (1.0 - tax / 100.0)) / shares
            if abs(implied - fy27) > max(0.05, abs(fy27) * 0.05):
                fails.append("stock_ideas[%d]: FY2027 AI EPS %.2f != "
                             "(revenue*margin*(1-tax))/shares %.2f" % (i, fy27, implied))

    prov = row.get("valuation_provenance")
    required = ("ttm_eps_diluted", "ttm_pe", "fy2027_eps_consensus", "fy2028_eps_consensus",
                "pe_5y_median", "eps_revision_pct", "base_target", "bull_target", "bear_target")
    labels = {"VERIFIED_FACT", "CONSENSUS", "AI_FORECAST", "UNAVAILABLE"}
    if not isinstance(prov, dict):
        fails.append("stock_ideas[%d].valuation_provenance must be an object" % i)
    else:
        missing = [k for k in required if k not in prov]
        if missing:
            fails.append("stock_ideas[%d].valuation_provenance missing: %s"
                         % (i, ", ".join(missing)))
        bad = [k for k, v in prov.items() if str(v).strip() not in labels]
        if bad:
            fails.append("stock_ideas[%d].valuation_provenance has invalid labels: %s"
                         % (i, ", ".join(bad)))
        for key in ("fy2027_eps_consensus", "fy2028_eps_consensus"):
            if str(prov.get(key, "")).strip() == "CONSENSUS" and not _src_ok(row.get("consensus_source")):
                fails.append("stock_ideas[%d].%s is labelled CONSENSUS but consensus_source is not a "
                             "real URL in global sources; cite a consensus source or use AI_FORECAST"
                             % (i, key))
        if str(row.get("verification") or "").strip() == "Verified":
            weak = [k for k in required
                    if str(prov.get(k, "")).strip() in ("AI_FORECAST", "UNAVAILABLE")]
            if weak:
                fails.append("stock_ideas[%d].verification=Verified but provenance is "
                             "AI_FORECAST/UNAVAILABLE for: %s" % (i, ", ".join(weak)))

    if method == "P/E":
        for name, target_key in (("bull", "bull_target"), ("base", "base_target"),
                                 ("bear", "bear_target")):
            eps = _num_or_none(row.get(name + "_eps"))
            pe = _num_or_none(row.get(name + "_pe"))
            target = _num_or_none(row.get(target_key))
            if eps is None or pe is None or target is None:
                fails.append("stock_ideas[%d].%s scenario needs %s_eps, %s_pe and %s"
                             % (i, name, name, name, target_key))
                continue
            rationale = str(row.get(name + "_rationale") or "").strip()
            if len(rationale) < 40:
                fails.append("stock_ideas[%d].%s scenario needs a rationale of at least 40 chars"
                             % (i, name))
            if eps <= 0 or pe <= 0:
                fails.append("stock_ideas[%d].%s scenario EPS and P/E must be positive for P/E method"
                             % (i, name))
                continue
            if name == "base":
                f27 = _num_or_none(row.get("fy2027_eps_consensus"))
                f28 = _num_or_none(row.get("fy2028_eps_consensus"))
                if f27 and f28 and min(abs(eps - f27), abs(eps - f28)) > max(0.02, abs(eps) * 0.01):
                    fails.append("stock_ideas[%d] base scenario EPS %.2f is neither FY2027 %.2f nor FY2028 %.2f"
                                 % (i, eps, f27, f28))
                fpe = _num_or_none(row.get("fwd_pe_2027")) if f27 and abs(eps - f27) < 0.02 else _num_or_none(row.get("fwd_pe_2028"))
                if fpe and abs(pe / fpe - 1.0) > 0.25:
                    fails.append("stock_ideas[%d] base scenario P/E %.2f is more than 25%% from forward P/E %.2f"
                                 % (i, pe, fpe))
            implied = calc_target_price(eps, pe)
            tolerance = max(0.5, abs(target) * 0.005)
            if abs(implied - target) > tolerance:
                fails.append("stock_ideas[%d] %s: %.2f EPS x %.2f P/E = %.2f != target %.2f"
                             % (i, name, eps, pe, implied, target))

    # --- Part 4: scenario probabilities and probability-weighted outputs ---
    probs = [_num_or_none(row.get(k)) for k in ("bull_prob", "base_prob", "bear_prob")]
    if any(p is None for p in probs):
        fails.append("stock_ideas[%d]: bull_prob, base_prob and bear_prob are required" % i)
    else:
        perr = qc_probabilities(probs)
        if perr:
            fails.append("stock_ideas[%d]: %s" % (i, perr))
        else:
            targets = [_num_or_none(row.get(k)) for k in
                       ("bull_target", "base_target", "bear_target")]
            if all(t is not None for t in targets):
                exp = sum(p * t for p, t in zip(probs, targets))
                claim = _num_or_none(row.get("expected_price"))
                if claim is None or abs(claim - exp) > max(0.05, abs(exp) * 0.005):
                    fails.append("stock_ideas[%d].expected_price %s != probability-weighted "
                                 "target %.2f" % (i, claim, exp))
                if cur:
                    claim_ret = _num_or_none(row.get("expected_return_pct"))
                    exp_ret = (exp / cur - 1.0) * 100.0
                    if claim_ret is None or abs(claim_ret - exp_ret) > 0.5:
                        fails.append("stock_ideas[%d].expected_return_pct %s != "
                                     "probability-weighted return %.2f%%" % (i, claim_ret, exp_ret))
            basis = str(row.get("probability_basis") or "").strip().upper()
            if "UNCALIBRATED" not in basis:
                fails.append("stock_ideas[%d].probability_basis must label AI probabilities "
                             "as UNCALIBRATED" % i)

    # --- Part 4: action vs valuation / reward-risk ---
    rec = str(row.get("recommendation") or "").strip()
    base_t = _num_or_none(row.get("base_target"))
    override = str(row.get("override_reason") or "").strip()
    if override.upper() in ("", "N/A", "NA", "NONE"):
        override = ""
    if cur and base_t is not None:
        if rec in ("Buy", "Add"):
            if base_t <= cur and not override:
                fails.append("stock_ideas[%d]: %s base target %.2f must exceed current %.2f "
                             "(or provide override_reason)" % (i, rec, base_t, cur))
            rr = _num_or_none(row.get("risk_reward"))
            if rr is not None and rr < 1.0 and not override:
                fails.append("stock_ideas[%d]: %s reward/risk %.2f is below 1.0 "
                             "(or provide override_reason)" % (i, rec, rr))
        if rec in ("Buy", "Add"):
            exp_price = _num_or_none(row.get("expected_price"))
            exp_ret = ((exp_price / cur - 1.0) * 100.0) if (cur and exp_price) else _num_or_none(row.get("expected_return_pct"))
            if exp_ret is not None and exp_ret < 0 and not override:
                fails.append("stock_ideas[%d]: %s has a negative probability-weighted return "
                             "%.2f%% (downgrade or provide override_reason)" % (i, rec, exp_ret))
        if rec in ("Reduce", "Sell"):
            if base_t >= cur and not override:
                fails.append("stock_ideas[%d]: %s base target %.2f must be below current %.2f "
                             "(or provide override_reason)" % (i, rec, base_t, cur))
        elif rec == "Hold" and abs(base_t / cur - 1.0) > 0.15 and not override:
            fails.append("stock_ideas[%d]: Hold base target is more than 15%% from current "
                         "price (or provide override_reason)" % i)

    fails.extend(compare_valuation(row, i))
    fails.extend(_validate_assumption_labels(row, i))
    fails.extend(_validate_decision(row, i))
    fails.extend(_validate_pe_samples(row, i))
    fails.extend(_validate_fy_duplicate(row, i))


def _validate_source_notes(rows, sources: dict, fails: list[str]) -> None:
    """Source notes must not label EPS in a different fiscal year than the idea row."""
    for i, row in enumerate(rows):
        ticker = str(row.get("ticker") or "").strip()
        if not ticker:
            continue
        for note in sources.values():
            low = str(note or "")
            if ticker.lower() not in low.lower():
                continue
            for year, field in ((2026, "fy2026_eps_consensus"), (2027, "fy2027_eps_consensus"),
                                (2028, "fy2028_eps_consensus")):
                m = re.search(r"FY%s[^.]{0,30}?EPS\s*\$?([0-9]+\.[0-9]+)" % year, low)
                if not m:
                    continue
                actual = _num_or_none(row.get(field))
                claimed = float(m.group(1))
                if actual is None or abs(claimed - actual) > max(0.05, abs(actual) * 0.01):
                    fails.append("stock_ideas[%d] %s source note labels %.2f as FY%s EPS, "
                                 "but the row has %s" % (i, ticker, claimed, year,
                                                          "N/A" if actual is None else "%.2f" % actual))


def _validate_decision(row: dict, i: int) -> list[str]:
    """Buy with weak asymmetry needs an explicit rationale; exits explain the position."""
    fails: list[str] = []
    rec = str(row.get("recommendation") or "").strip()
    rr = _num_or_none(row.get("risk_reward"))
    exp_ret = _num_or_none(row.get("expected_return_pct"))
    rationale = str(row.get("decision_rationale") or "").strip()
    if rec in ("Buy", "Add") and ((rr is not None and rr < 1.0) or (exp_ret is not None and exp_ret < 0)):
        if len(rationale) < 80:
            fails.append("stock_ideas[%d]: %s has weak asymmetry (R/R %s, expected return %s) "
                         "without a decision_rationale of at least 80 chars — downgrade or explain"
                         % (i, rec, rr, exp_ret))
    if rec in ("Reduce", "Sell") and rationale:
        if not re.search(r"existing|position|trim|reduce|long", rationale, re.I):
            fails.append("stock_ideas[%d]: %s must state how existing long exposure changes"
                         % (i, rec))
    return fails


def _validate_cross_ticker(rows, fails: list[str]) -> None:
    """Research text must belong to its own ticker and sector."""
    tickers = [str(r.get("ticker") or "").upper() for r in rows if isinstance(r, dict)]
    sectors = {str(r.get("ticker") or "").upper(): str(r.get("sector") or "") for r in rows if isinstance(r, dict)}
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            continue
        own = str(row.get("ticker") or "").upper()
        sector = str(row.get("sector") or "")
        for field in ("thesis", "sector_context", "conclusion", "review", "catalysts", "peer_comparison"):
            text = str(row.get(field) or "")
            for other in tickers:
                if other and other != own and re.search(r"\b%s\b" % re.escape(other), text):
                    if field != "peer_comparison" or ("Energy" in sectors.get(other, "") and "Energy" not in sector):
                        fails.append("stock_ideas[%d] %s.%s mentions %s (cross-ticker contamination)"
                                     % (i, own, field, other))
            if "Energy" not in sector and re.search(r"\b(OPEC|oil|crude|refinery|energy beta)\b", text, re.I):
                fails.append("stock_ideas[%d] %s.%s contains energy/oil research for a %s company"
                             % (i, own, field, sector or "non-energy"))
        review = str(row.get("review") or "")
        rec = str(row.get("recommendation") or "")
        if rec in ("Buy", "Add") and re.search(r"\b(downgrade|trim|reduce|sell)\b", review, re.I):
            fails.append("stock_ideas[%d] %s review says downgrade/trim but recommendation is %s"
                         % (i, own, rec))
        if rec in ("Reduce", "Sell") and re.search(r"\b(upgrade|add|buy)\b", review, re.I):
            fails.append("stock_ideas[%d] %s review says upgrade/add but recommendation is %s"
                         % (i, own, rec))


def _validate_templates(rows, fails: list[str]) -> None:
    """Reject near-identical research text across different tickers."""
    fields = ("thesis", "peer_comparison", "catalysts", "risks", "conclusion")
    norm = lambda t: re.sub(r"[^a-z0-9 ]", "", str(t or "").lower()).strip()
    for a in range(len(rows)):
        for b in range(a + 1, len(rows)):
            ra, rb = rows[a], rows[b]
            if not isinstance(ra, dict) or not isinstance(rb, dict):
                continue
            for field in fields:
                ta, tb = norm(ra.get(field)), norm(rb.get(field))
                if len(ta) < 40 or len(tb) < 40:
                    continue
                if ta == tb:
                    fails.append("stock_ideas[%d]/[%d].%s are identical (template text)"
                                 % (a, b, field))
                    continue
                sa, sb = set(ta.split()), set(tb.split())
                if sa and sb and len(sa & sb) / len(sa | sb) > 0.95:
                    fails.append("stock_ideas[%d]/[%d].%s are near-duplicates (template text)"
                                 % (a, b, field))


def _validate_pe_samples(row: dict, i: int) -> list[str]:
    """3Y and 5Y P/E statistics must not be the same sample dressed twice."""
    keys = ("pe_3y_median", "pe_3y_min", "pe_3y_max", "pe_5y_median", "pe_5y_min", "pe_5y_max")
    vals = [_num_or_none(row.get(k)) for k in keys]
    if any(v is None for v in vals):
        return []
    if vals[0] == vals[3] and vals[1] == vals[4] and vals[2] == vals[5]:
        return ["stock_ideas[%d]: 3Y and 5Y P/E statistics are identical — the 5Y sample "
                "must be genuinely longer/distinct" % i]
    return []


def _validate_fy_duplicate(row: dict, i: int) -> list[str]:
    """FY2026 must not be a copy of FY2027 when current-year consensus is absent."""
    a = _num_or_none(row.get("fy2026_eps_consensus"))
    b = _num_or_none(row.get("fy2027_eps_consensus"))
    if a is not None and b is not None and abs(a - b) < 0.005:
        return ["stock_ideas[%d]: FY2026 EPS %.2f duplicates FY2027 %.2f; use N/A when the "
                "current-year consensus is unavailable" % (i, a, b)]
    return []


def _validate_stock_ideas(rows, narrative: dict, fails: list[str], evidence: dict) -> set:
    """Validate idea cards: fields, arithmetic, freshness, provenance. Returns tickers."""
    tickers: set = set()
    prev = {str(t).upper() for t in (evidence.get("previous_ideas") or [])}
    if not isinstance(rows, list) or not rows:
        fails.append("stock_ideas must be a non-empty list of idea objects")
        return tickers
    if len(rows) != 5:
        fails.append("stock_ideas must contain exactly 5 ideas (got %d)" % len(rows))
    global_sources = {str(s.get("url") or "").strip(): str(s.get("note") or "")
                      for s in (narrative.get("sources") or []) if isinstance(s, dict)}
    _validate_source_notes(rows, global_sources, fails)
    report_dt = _parse_report_date(evidence)
    recs = {"Buy", "Add", "Hold", "Reduce", "Sell"}
    horizons = {"1-3M", "6-12M", "12M+"}
    reassess_vals = {"NEW", "KEEP", "UPGRADE", "DOWNGRADE", "EXIT", "REPLACE"}
    verification_vals = {"Verified", "Estimate", "Unverified"}
    bearish = False
    stock_count = 0
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            fails.append("stock_ideas[%d] is not an object" % i)
            continue
        missing = [k for k in CARD_SECTIONS["stock_ideas"]
                   if k not in row and k not in OPTIONAL_IDEA_FIELDS]
        if missing:
            fails.append("stock_ideas[%d] missing fields: %s" % (i, ", ".join(missing)))
            continue
        ticker = str(row.get("ticker") or "").strip()
        rec = str(row.get("recommendation") or "").strip()
        hor = str(row.get("horizon") or "").strip()
        sec_type = str(row.get("security_type") or "").strip()
        if not ticker:
            fails.append("stock_ideas[%d].ticker is empty" % i)
        elif ticker in tickers:
            fails.append("stock_ideas[%d].ticker duplicated: %s" % (i, ticker))
        else:
            tickers.add(ticker)
        if sec_type not in ("Stock", "ETF"):
            fails.append("stock_ideas[%d].security_type must be 'Stock' or 'ETF'" % i)
        if sec_type == "Stock":
            stock_count += 1
        if rec not in recs:
            fails.append("stock_ideas[%d].recommendation must be one of %s" % (i, sorted(recs)))
        if hor not in horizons:
            fails.append("stock_ideas[%d].horizon must be one of %s" % (i, sorted(horizons)))
        if rec in ("Sell", "Reduce", "Hold"):
            bearish = True
        reassess = str(row.get("reassess") or "").strip()
        verification = str(row.get("verification") or "").strip()
        if reassess not in reassess_vals:
            fails.append("stock_ideas[%d].reassess must be one of %s" % (i, sorted(reassess_vals)))
        else:
            if prev:
                if ticker.upper() in prev and reassess == "NEW":
                    fails.append("stock_ideas[%d] %s was in the previous report; reassess must be "
                                 "KEEP/UPGRADE/DOWNGRADE/EXIT/REPLACE, not NEW" % (i, ticker))
                elif ticker.upper() not in prev and reassess != "NEW":
                    fails.append("stock_ideas[%d] %s is new; reassess must be NEW" % (i, ticker))
        if verification not in verification_vals:
            fails.append("stock_ideas[%d].verification must be one of %s" % (i, sorted(verification_vals)))
        nums = {}
        for key in ("current_price", "entry_price", "base_target", "bull_target",
                    "bear_target", "upside_pct", "downside_pct",
                    "return_from_current_pct", "risk_reward"):
            val = row.get(key)
            if not isinstance(val, (int, float)):
                fails.append("stock_ideas[%d].%s must be numeric" % (i, key))
            else:
                nums[key] = float(val)
        price_date = str(row.get("price_date") or "").strip()
        parsed = None
        for fmt in ("%Y-%m-%d", "%d %B %Y", "%d %b %Y"):
            try:
                parsed = datetime.strptime(price_date, fmt)
                break
            except ValueError:
                continue
        if parsed is None:
            fails.append("stock_ideas[%d].price_date must be YYYY-MM-DD or 'D Month YYYY'" % i)
        elif report_dt is not None:
            age = (report_dt - parsed).days
            if age > 7 or age < -1:
                fails.append("stock_ideas[%d].price_date is stale (%d days from report date %s)"
                             % (i, age, evidence.get("data_cutoff")))
        if len(nums) == 9:
            cur = nums["current_price"]
            entry = nums["entry_price"]
            base = nums["base_target"]
            bull = nums["bull_target"]
            bear = nums["bear_target"]
            if min(cur, entry, base, bull, bear) <= 0:
                fails.append("stock_ideas[%d] prices must be positive" % i)
            else:
                if abs(entry / cur - 1.0) > 0.25:
                    fails.append("stock_ideas[%d].entry_price deviates more than 25%% from current_price" % i)
                up = (base / entry - 1.0) * 100.0
                down = (bear / entry - 1.0) * 100.0
                from_cur = (base / cur - 1.0) * 100.0
                if abs(up - nums["upside_pct"]) > 0.5:
                    fails.append("stock_ideas[%d].upside_pct %.2f != (base/entry-1)*100 %.2f"
                                 % (i, nums["upside_pct"], up))
                if abs(down - nums["downside_pct"]) > 0.5:
                    fails.append("stock_ideas[%d].downside_pct %.2f != (bear/entry-1)*100 %.2f"
                                 % (i, nums["downside_pct"], down))
                if abs(from_cur - nums["return_from_current_pct"]) > 0.5:
                    fails.append("stock_ideas[%d].return_from_current_pct %.2f != (base/current-1)*100 %.2f"
                                 % (i, nums["return_from_current_pct"], from_cur))
                if abs(down) > 0.01:
                    rr = up / abs(down)
                    if abs(rr - nums["risk_reward"]) > 0.1:
                        fails.append("stock_ideas[%d].risk_reward %.2f != upside/|downside| %.2f"
                                     % (i, nums["risk_reward"], rr))
                if rec in ("Buy", "Add"):
                    if not (base > cur and bull > base and bear < cur):
                        fails.append("stock_ideas[%d] Buy/Add requires base > current, bull > base and bear < current" % i)
                elif rec in ("Sell", "Reduce"):
                    if not (base < cur and bear < base and bull > cur):
                        fails.append("stock_ideas[%d] Sell/Reduce requires bull > current > base > bear" % i)
                else:
                    if not (bull > base > bear):
                        fails.append("stock_ideas[%d] Hold requires bull > base > bear" % i)
        for key in ("thesis", "review", "assumptions", "why_vs_alternatives", "contrary",
                    "peer_comparison", "sector_context", "conclusion",
                    "catalysts", "risks", "entry_condition", "exit", "invalidation", "opposing"):
            text = row.get(key)
            if not isinstance(text, str) or not text.strip():
                fails.append("stock_ideas[%d].%s must be a non-empty string" % (i, key))
            elif len(text) > 900:
                fails.append("stock_ideas[%d].%s exceeds 900 chars" % (i, key))
        for key, minimum in (("thesis", 160), ("review", 40), ("peer_comparison", 100),
                             ("sector_context", 100), ("conclusion", 80),
                             ("contrary", 80), ("catalysts", 40)):
            text = str(row.get(key) or "")
            if len(text.strip()) < minimum:
                fails.append("stock_ideas[%d].%s is too thin (%d chars; minimum %d) — "
                             "restore substantive research" % (i, key, len(text.strip()), minimum))
        if len(re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2}|20\d\d-\d\d-\d\d", str(row.get("catalysts") or ""))) < 2:
            fails.append("stock_ideas[%d].catalysts must list at least two dated events" % i)
        basis = str(row.get("eps_basis") or "").strip()
        pe_basis = str(row.get("pe_history_basis") or "").strip()
        if pe_basis != basis:
            fails.append("stock_ideas[%d].pe_history_basis %r must match eps_basis %r "
                         "(historical and forward P/E only on consistent EPS)" % (i, pe_basis, basis))
        assumptions = str(row.get("assumptions") or "").lower()
        if not any(k in assumptions for k in ("eps", "p/e", "multiple", "fcf", "dcf", "ebitda", "revenue")):
            fails.append("stock_ideas[%d].assumptions must state an explicit valuation basis "
                         "(EPS, P/E, multiple, FCF, DCF, EBITDA or revenue)" % i)
        _validate_valuation(row, i, fails, global_sources)
        srcs = row.get("sources")
        if not isinstance(srcs, list) or not srcs:
            fails.append("stock_ideas[%d].sources must be a non-empty list of URLs" % i)
        else:
            research_source = False
            fund_kw = ("earnings", "10-q", "10-k", "8-k", "guidance", "revenue", "fcf",
                       "filing", "results", "investor", "margin", "eps", "factsheet",
                       "holdings", "outlook")
            for u in srcs:
                if not isinstance(u, str) or u.strip() not in global_sources:
                    fails.append("stock_ideas[%d].sources contains a URL not in the global sources list: %r"
                                 % (i, u))
                    continue
                low = u.strip().lower()
                if "api.138.2.69.165.sslip.io" in low or low.endswith("/openapi.json"):
                    continue  # price provenance, never a fundamental citation
                note = global_sources.get(u.strip(), "").lower()
                names = ticker.lower() in note or str(row.get("name") or "").lower() in note
                deep_link = any(k in low for k in (
                    "sec.gov", "10-q", "10-k", "8-k", "earnings", "quarterly",
                    "results", "press-release", "news-release", "financial-results"))
                dated = re.search(r"\b20\d{2}\b", note) is not None
                if names and any(k in note for k in fund_kw) and deep_link and dated:
                    research_source = True
            if not research_source:
                fails.append("stock_ideas[%d] needs at least one dated, company-specific filing/results "
                             "source (SEC/10-Q/10-K/8-K, earnings release or results page); an IR "
                             "homepage or the market API is not sufficient" % i)
            if verification == "Verified" and not research_source:
                fails.append("stock_ideas[%d].verification is 'Verified' but no dated filing/results "
                             "source supports it" % i)
    if prev and len(rows) >= 3:
        new_selected = [t for t in tickers if t.upper() not in prev]
        if len(new_selected) < 1:
            print("NARRATIVE WARNING: no NEW selected idea versus the previous report; "
                  "carryovers are allowed but the screen is static")
    if not bearish:
        fails.append("stock_ideas must include at least one Sell, Reduce or Hold idea")
    if stock_count < 3:
        fails.append("stock_ideas must include at least 3 individual stocks "
                     "(security_type='Stock'), not only ETFs")
    return tickers


def _has_metric_basis(text: str) -> bool:
    """True when a rationale cites a metric (score with decimal, or a multiple like 18x)."""
    if re.search(r"\d+(?:\.\d+)?\s*x\b", text, re.I):
        return True
    return any("." in n for n in re.findall(r"\d+(?:\.\d+)?", text))


def _validate_sector_allocation(rows, fails: list[str]) -> None:
    """ST and LT portfolios: 11 unique GICS each, weights sum to 100, active sums to 0."""
    if not isinstance(rows, list) or len(rows) != 22:
        fails.append("sector_allocation must contain 22 rows (11 ST + 11 LT); got %s"
                     % (len(rows) if isinstance(rows, list) else 0))
        return
    groups: dict[str, list] = {"ST": [], "LT": []}
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            fails.append("sector_allocation[%d] is not an object" % i)
            continue
        horizon = str(row.get("horizon") or "").strip().upper()
        if horizon not in groups:
            fails.append("sector_allocation[%d].horizon must be ST or LT (got %r)" % (i, horizon))
            continue
        groups[horizon].append(row)
    for horizon, group in groups.items():
        if len(group) != 11:
            fails.append("sector_allocation %s must contain exactly 11 sectors (got %d)"
                         % (horizon, len(group)))
            continue
        names = [str(r.get("sector") or "").strip() for r in group]
        if len(set(names)) != 11:
            fails.append("sector_allocation %s sector names must be 11 unique GICS sectors" % horizon)
        bench = port = active = 0.0
        for i, row in enumerate(group):
            try:
                b = float(row.get("benchmark_weight"))
                p = float(row.get("portfolio_weight"))
                a = float(row.get("active_weight"))
            except (TypeError, ValueError):
                fails.append("sector_allocation %s row %d weights must be numeric" % (horizon, i))
                continue
            if abs((p - b) - a) > 0.1:
                fails.append("sector_allocation %s row %d active %.2f != portfolio %.2f - benchmark %.2f"
                             % (horizon, i, a, p, b))
            rationale = str(row.get("rationale") or "").strip()
            if len(rationale) < 8:
                fails.append("sector_allocation %s row %d needs a sizing rationale" % (horizon, i))
            elif not _has_metric_basis(rationale):
                fails.append("sector_allocation %s row %d rationale must cite a specific metric "
                             "(sector score or valuation multiple), not only the active weight"
                             % (horizon, i))
            if re.search(r"\bneutral\b", rationale, re.I) and abs(a) > 0.1:
                fails.append("sector_allocation %s row %d says neutral but active is %+.1fpp"
                             % (horizon, i, a))
            m = re.search(r"(overweight|underweight|neutral)[^.]{0,40}?([0-9.]+)\s*pp", rationale, re.I)
            if m:
                word, claimed = m.group(1).lower(), float(m.group(2))
                if word == "neutral":
                    if abs(a) > 0.1:
                        fails.append("sector_allocation %s row %d says neutral but active is %+.1fpp"
                                     % (horizon, i, a))
                elif abs(claimed - abs(a)) > 0.1:
                    fails.append("sector_allocation %s row %d says %s %.1fpp but active is %+.1fpp"
                                 % (horizon, i, word, claimed, a))
            bench += b
            port += p
            active += a
        if abs(bench - 100.0) > 0.2:
            fails.append("sector_allocation %s benchmark weights must sum to 100 (got %.2f)"
                         % (horizon, bench))
        if abs(port - 100.0) > 0.2:
            fails.append("sector_allocation %s portfolio weights must sum to 100 (got %.2f)"
                         % (horizon, port))
        if abs(active) > 0.2:
            fails.append("sector_allocation %s active weights must sum to 0 (got %.2f)"
                         % (horizon, active))
        rationales = [str(r.get("rationale") or "").strip() for r in group]
        if len(set(rationales)) < 6:
            fails.append("sector_allocation %s needs at least 6 distinct sizing rationales" % horizon)


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
        # Card sections accept a list of row dicts; their fields are validated
        # separately below (arithmetic + provenance).
        if name in CARD_SECTIONS and isinstance(value, list) and value \
                and all(isinstance(v, dict) for v in value):
            for i, row in enumerate(value):
                unknown = [k for k in row
                           if k not in CARD_SECTIONS[name]
                           and not (name == "stock_ideas" and k in OPTIONAL_IDEA_FIELDS)]
                if unknown:
                    fails.append(
                        f"section {name!r} row {i} has unknown keys: {', '.join(unknown)}"
                    )
            continue
        # Table sections accept a list of row dicts as well as prose.
        if name in TABLE_SECTIONS and isinstance(value, list) and value \
                and all(isinstance(v, dict) for v in value):
            columns = TABLE_SECTIONS[name]
            for i, row in enumerate(value):
                unknown = [k for k in row if k not in dict(columns)]
                if unknown:
                    fails.append(
                        f"section {name!r} row {i} has unknown keys: {', '.join(unknown)}"
                    )
                for key, _ in columns:
                    cell = row.get(key)
                    if cell is None:
                        continue
                    text = str(cell)
                    if _has_html_tag(text):
                        fails.append(
                            f"section {name!r} row {i}.{key} contains raw HTML; keep it plain text"
                        )
                    if len(text) > MAX_SECTION_CHARS:
                        fails.append(
                            f"section {name!r} row {i}.{key} exceeds {MAX_SECTION_CHARS} chars"
                        )
            continue
        texts = _as_text_list(value)
        if texts is None:
            fails.append(f"section {name!r} must be a string or list of strings")
            continue
        for text in texts:
            total += len(text)
            if not text.strip():
                fails.append(f"section {name!r} contains an empty entry")
            if _has_html_tag(text):
                fails.append(f"section {name!r} contains raw HTML tags; prose must be plain text")
            if len(text) > MAX_SECTION_CHARS:
                fails.append(f"section {name!r} exceeds {MAX_SECTION_CHARS} chars in one entry")
    for name in REQUIRED_SECTIONS:
        value = sections.get(name)
        # Table/card sections may be a non-empty list of row dicts.
        if name in TABLE_SECTIONS or name in CARD_SECTIONS:
            if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
                continue
        if not (_as_text_list(value) or []):
            fails.append(f"required section {name!r} missing or empty")
    if total > MAX_TOTAL_CHARS:
        fails.append(f"narrative total length {total} exceeds {MAX_TOTAL_CHARS} chars")

    stock_tickers = _validate_stock_ideas(sections.get("stock_ideas"), narrative, fails, evidence)
    _validate_candidate_screen(sections.get("candidate_screen"), stock_tickers, fails)
    _validate_sector_allocation(sections.get("sector_allocation"), fails)
    _validate_templates(sections.get("stock_ideas") or [], fails)
    _validate_cross_ticker(sections.get("stock_ideas") or [], fails)

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
    # AI scoring layer. latest-report.md carries facts plus rule-based judgment
    # scores. The model may re-examine the judgment layer, but only in two
    # auditable steps: (1) its own 0-100 score for every regime factor, and
    # (2) its own factor weights in points summing to 100. The AI regime score
    # is COMPUTED as Σ(score × weight)/100 — never asserted as a free number.
    # Source factor scores and source weights stay in the evidence pack so every
    # input and every delta is traceable (§54A §16 Source vs AI attribution).
    adj = narrative.get("adjustments")
    if adj is None:
        fails.append("adjustments is required: AI must supply factor_scores and weights")
        adj = {}
    elif not isinstance(adj, dict):
        fails.append("adjustments must be an object")
        adj = {}
    elif not adj:
        fails.append("adjustments is empty: AI must supply factor_scores and weights")

    adj_values: list = []
    known_factors = sorted(
        k.split(".", 1)[1] for k in metrics if k.startswith("regime_factors.")
    )
    if adj:
        rat = adj.get("rationale")
        if not isinstance(rat, str) or len(rat) < 80 or len(rat) > 2000:
            fails.append("adjustments.rationale must be a string between 80 and 2000 chars")

        scores = adj.get("factor_scores")
        if not isinstance(scores, dict) or not scores:
            fails.append(
                "adjustments.factor_scores must be a non-empty object covering all "
                "%d regime factors" % len(known_factors))
            scores = {}
        else:
            for name, val in scores.items():
                if name not in known_factors:
                    fails.append("adjustments.factor_scores unknown factor %r" % name)
                    continue
                if not isinstance(val, (int, float)) or not (0 <= float(val) <= 100):
                    fails.append("adjustments.factor_scores[%r] must be a number in 0-100" % name)
                    continue
                adj_values.append(float(val))
                src = metrics.get("regime_factors.%s" % name)
                if isinstance(src, (int, float)) and abs(float(val) - float(src)) > 30:
                    fails.append(
                        "adjustments.factor_scores[%r] %.2f is more than 30 points from source %.2f"
                        % (name, float(val), float(src)))
            missing = sorted(set(known_factors) - set(scores.keys()))
            if missing:
                fails.append("adjustments.factor_scores missing factors: " + ", ".join(missing))

        weights = adj.get("weights")
        computed = None
        if not isinstance(weights, dict) or not weights:
            fails.append(
                "adjustments.weights must be a non-empty object covering all "
                "%d regime factors" % len(known_factors))
            weights = {}
        else:
            wsum = 0.0
            for name, val in weights.items():
                if name not in known_factors:
                    fails.append("adjustments.weights unknown factor %r" % name)
                    continue
                if not isinstance(val, (int, float)) or not (0 <= float(val) <= 100):
                    fails.append("adjustments.weights[%r] must be a number in 0-100 points" % name)
                    continue
                wsum += float(val)
                src_w = metrics.get("regime_weights.%s" % name)
                if isinstance(src_w, (int, float)) and abs(float(val) - float(src_w)) > 10:
                    fails.append(
                        "adjustments.weights[%r] %.2f is more than 10 points from source weight %.2f"
                        % (name, float(val), float(src_w)))
            if abs(wsum - 100.0) > 0.5:
                fails.append("adjustments.weights sum to %.2f; must be 100 +/- 0.5" % wsum)
            missing = sorted(set(known_factors) - set(weights.keys()))
            if missing:
                fails.append("adjustments.weights missing factors: " + ", ".join(missing))
            if not missing and abs(wsum - 100.0) <= 0.5 and set(scores) >= set(known_factors):
                computed = round(
                    sum(float(scores[k]) * float(weights[k]) for k in known_factors) / 100.0, 2)
                adj_values.append(computed)
                src_score = metrics.get("regime.score")
                if isinstance(src_score, (int, float)) and abs(computed - float(src_score)) > 25:
                    fails.append(
                        "computed AI regime score %.2f is more than 25 points from source %.2f"
                        % (computed, float(src_score)))
                claimed = adj.get("regime_score")
                if claimed is not None:
                    if not isinstance(claimed, (int, float)) or not (0 <= float(claimed) <= 100):
                        fails.append("adjustments.regime_score must be a number in 0-100")
                    elif abs(float(claimed) - computed) > 0.5:
                        fails.append(
                            "adjustments.regime_score %.2f does not equal "
                            "sum(factor_scores x weights)/100 = %.2f; the AI score must be computed"
                            % (float(claimed), computed))

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
                deltas = [float(ss[n]) - float(metrics["sectors.%s.score" % n])
                          for n in ss if isinstance(metrics.get("sectors.%s.score" % n), (int, float))]
                if len(deltas) >= 3 and (max(deltas) - min(deltas)) < 0.01:
                    fails.append(
                        "adjustments.sector_scores apply a uniform %.2f-point offset to every "
                        "sector; re-rate each sector on its own evidence" % deltas[0])

        sr = adj.get("sector_rationale")
        if sr is not None:
            if not isinstance(sr, dict):
                fails.append("adjustments.sector_rationale must be an object keyed by sector")
            else:
                known_sectors = {k.split(".")[1] for k in metrics
                                 if k.startswith("sectors.") and k.endswith(".score")}
                seen_reason: dict[str, str] = {}
                for name, text in sr.items():
                    if name not in known_sectors:
                        fails.append("adjustments.sector_rationale unknown sector %r" % name)
                    elif not isinstance(text, str) or len(text.strip()) < 40 or len(text) > 300:
                        fails.append(
                            "adjustments.sector_rationale[%r] must be a sector-specific string "
                            "of 40-300 chars" % name)
                    else:
                        key = " ".join(text.lower().split())
                        if key in seen_reason:
                            fails.append(
                                "adjustments.sector_rationale[%r] duplicates %r; each sector "
                                "must state its own evidence" % (name, seen_reason[key]))
                        else:
                            seen_reason[key] = name

    # Forward Signal slot (A): restate the source engine's 5D/20D/60D expected
    # returns, each with a percentage. Read-only calibration; it never feeds back
    # into the regime score (no look-ahead).
    fs_value = sections.get("forward_signal")
    fs_texts = _as_text_list(fs_value) or []
    if fs_texts:
        fs_text = " ".join(str(t) for t in fs_texts)
        for horizon in ("5D", "20D", "60D"):
            m = re.search(r"\b%s\b" % horizon, fs_text)
            if not m:
                fails.append("forward_signal must cite %s" % horizon)
                continue
            tail = fs_text[m.end():m.end() + 90]
            if "%" not in tail and not re.search(r"\d+(?:\.\d+)?\s*percent", tail, re.I):
                fails.append("forward_signal must give a percentage for %s" % horizon)

    # ---- External numeric claims --------------------------------------------
    # The numeric guard below only accepts figures that trace to the evidence
    # pack, a claims[] entry, or an AI-adjusted score. That makes genuinely
    # evidence-dense prose impossible: an official BLS CPI print or BEA GDP
    # figure does not exist in latest-report.md, so writing "September CPI 3.7%"
    # would fail validation while the vague "CPI near 4 percent" passes. That
    # asymmetry is what flattened the prose. external_claims[] closes the gap:
    # each entry declares an outside number together with the source that
    # supports it, so precision is allowed exactly where provenance exists.
    ext_claims = narrative.get("external_claims")
    ext_values: list = []
    if ext_claims is None:
        ext_claims = []
    if not isinstance(ext_claims, list):
        fails.append("external_claims must be a list of {value, text, source} objects")
        ext_claims = []
    else:
        if len(ext_claims) > 80:
            fails.append(f"external_claims has {len(ext_claims)} entries, max 80")
        for i, item in enumerate(ext_claims):
            if not isinstance(item, dict):
                fails.append(f"external_claims[{i}] is not an object")
                continue
            unknown = set(item) - {"value", "text", "source"}
            if unknown:
                fails.append(f"external_claims[{i}] has unknown fields: {', '.join(sorted(unknown))}")
            val = item.get("value")
            text = item.get("text")
            src_ref = item.get("source")
            if not isinstance(val, (int, float)):
                fails.append(f"external_claims[{i}].value must be a number")
                continue
            ext_values.append(float(val))
            if not isinstance(text, str) or not text.strip():
                fails.append(f"external_claims[{i}].text must describe the figure")
            elif len(text) > 300:
                fails.append(f"external_claims[{i}].text exceeds 300 chars")
            elif "<" in text or ">" in text:
                fails.append(f"external_claims[{i}].text contains raw HTML; keep it plain text")
            if not isinstance(src_ref, str) or not src_ref.strip():
                fails.append(f"external_claims[{i}].source must name the supporting source or URL")
            elif len(src_ref) > 300:
                fails.append(f"external_claims[{i}].source exceeds 300 chars")

    # Every decimal in the prose must trace to the evidence pack, an explicit
    # claim, an AI-adjusted score, or a declared external claim. Runs AFTER the
    # external_claims block so ext_values is populated before it is consulted.
    numeric_mentions = set()
    for text in sections.values():
        for t in (_as_text_list(text) or []):
            numeric_mentions.update(re.findall(r"\b\d+\.\d+\b", t))
    metric_values = [float(v) for v in metrics.values() if isinstance(v, (int, float))]
    claim_values = [float(c.get("value")) for c in claims
                    if isinstance(c, dict) and isinstance(c.get("value"), (int, float))]
    allowed_values = metric_values + claim_values + adj_values + ext_values
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
            "prose contains numbers not found in the evidence pack "
            "(add each to claims[] with its path, or to external_claims[] with its source): "
            + ", ".join(unclaimed[:15])
        )

    # ---- External citations -------------------------------------------------
    # These are the outside sources the model actually consulted (BLS, BEA, Fed,
    # Treasury, exchange data, news). Without them the citation block only lists
    # latest-report.md and the report cannot be distinguished from a mechanical
    # dump of the rule engine.
    sources = narrative.get("sources")
    if sources is None:
        sources = []
    if not isinstance(sources, list):
        fails.append("sources must be a list of {label, url, note} objects")
        sources = []
    elif len(sources) > MAX_SOURCES:
        fails.append(f"sources has {len(sources)} entries, max {MAX_SOURCES}")
    seen_urls: set[str] = set()
    for i, item in enumerate(sources):
        if not isinstance(item, dict):
            fails.append(f"sources[{i}] is not an object")
            continue
        unknown = set(item) - set(SOURCE_FIELDS)
        if unknown:
            fails.append(f"sources[{i}] has unknown fields: {', '.join(sorted(unknown))}")
        label = item.get("label")
        url = item.get("url")
        note = item.get("note")
        if not isinstance(label, str) or not label.strip():
            fails.append(f"sources[{i}].label must be a non-empty string")
        elif len(label) > 200:
            fails.append(f"sources[{i}].label exceeds 200 chars")
        elif "<" in label or ">" in label:
            fails.append(f"sources[{i}].label contains raw HTML; keep it plain text")
        if not isinstance(url, str) or not url.strip():
            fails.append(f"sources[{i}].url must be a non-empty string")
        elif not re.match(r"^https?://[^\s<>\"']+$", url.strip()):
            fails.append(f"sources[{i}].url must be an http(s) URL, got {url!r}")
        elif url.strip() in seen_urls:
            fails.append(f"sources[{i}].url is a duplicate: {url.strip()}")
        else:
            seen_urls.add(url.strip())
        if note is not None:
            if not isinstance(note, str):
                fails.append(f"sources[{i}].note must be a string")
            elif len(note) > 400:
                fails.append(f"sources[{i}].note exceeds 400 chars")
            elif "<" in note or ">" in note:
                fails.append(f"sources[{i}].note contains raw HTML; keep it plain text")

    # A narrative run must show independent research, not a restatement of the
    # rule engine. Enforce floors on distinct external citations AND on how many
    # separate institutions those citations represent: ten pages from one domain
    # is not breadth.
    if sections and len(seen_urls) < MIN_SOURCES:
        fails.append(
            "sources must cite at least %d distinct external URLs "
            "(found %d); a report citing only latest-report.md is not independent research"
            % (MIN_SOURCES, len(seen_urls))
        )
    if sections:
        domains = {_registered_domain(u) for u in seen_urls}
        domains.discard("")
        if len(domains) < MIN_DOMAINS:
            fails.append(
                "sources must span at least %d distinct domains (found %d: %s); "
                "several pages from one institution do not count as breadth"
                % (MIN_DOMAINS, len(domains), ", ".join(sorted(domains)) or "none")
            )

    return fails


def _esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )



def _fmt2(value):
    try:
        return "%.2f" % float(value)
    except (TypeError, ValueError):
        return "N/A"


def _pct100(value):
    try:
        return "%.0f" % (float(value) * 100.0)
    except (TypeError, ValueError):
        return "N/A"

def _render_stock_ideas(rows) -> str | None:
    """Render single-stock ideas as cards (current/entry/scenarios/risk)."""
    if not isinstance(rows, list) or not rows:
        return None
    cards = []
    for r in rows:
        if not isinstance(r, dict):
            continue
        def e(key):
            return _esc(str(r.get(key) if r.get(key) is not None else ""))
        def v(key):
            return _esc(str(r.get(key) if r.get(key) is not None else "N/A"))

        def f2(key):
            try:
                return "%.2f" % float(r.get(key))
            except (TypeError, ValueError):
                return v(key)

        def e2(key):
            try:
                return "%.2f" % float(r.get(key))
            except (TypeError, ValueError):
                return e(key)

        def money(key):
            try:
                x = float(r.get(key))
            except (TypeError, ValueError):
                return v(key)
            if abs(x) >= 1e9:
                return "%.2fB" % (x / 1e9)
            if abs(x) >= 1e6:
                return "%.1fM" % (x / 1e6)
            return "%.0f" % x

        fund_html = (
            '<h4>Fundamentals</h4>'
            '<table><thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>'
            '<tr><td>Revenue TTM</td><td>%s</td></tr>'
            '<tr><td>Operating margin</td><td>%s%%</td></tr>'
            '<tr><td>P/S / P/B</td><td>%s / %s</td></tr>'
            '<tr><td>FY2027E / FY2028E revenue (consensus)</td><td>%s / %s</td></tr>'
            '<tr><td>Revenue growth 2027-2028</td><td>%s%%</td></tr>'
            '</tbody></table>'
            % (money("revenue_ttm"), f2("operating_margin_pct"), f2("ps_ratio"), f2("pb_ratio"),
               money("fy2027_revenue_consensus"), money("fy2028_revenue_consensus"),
               f2("revenue_growth_2027_2028_pct"))
        )
        val_html = (
            '<h4>Valuation</h4>'
            '<table><thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>'
            '<tr><td>TTM diluted EPS</td><td>%s</td></tr>'
            '<tr><td>TTM GAAP P/E</td><td>%s</td></tr>'
            '<tr><td>FY2026E / FY2027E / FY2028E EPS</td><td>%s / %s / %s</td></tr>'
            '<tr><td>Forward GAAP P/E 2027 / 2028</td><td>%s / %s</td></tr>'
            '<tr><td>EPS growth 2026-2028</td><td>%s%%</td></tr>'
            '<tr><td>EPS revisions (analyst)</td><td>%s%%</td></tr>'
            '<tr><td>3Y P/E median (min-max, pct)</td><td>%s (%s-%s, %s pct)</td></tr>'
            '<tr><td>5Y P/E median (min-max, pct)</td><td>%s (%s-%s, %s pct)</td></tr>'
            '<tr><td>Forward P/E vs 5Y median</td><td>%s%%</td></tr>'
            '<tr><td>Method</td><td>%s</td></tr>'
            '<tr><td>Assumptions</td><td>%s</td></tr>'
            '</tbody></table>'
            '<table><thead><tr><th>Scenario</th><th>Prob.</th><th>EPS</th><th>P/E</th><th>Implied price</th></tr></thead><tbody>'
            '<tr><td>Bull</td><td>%s%%</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            '<tr><td>Base</td><td>%s%%</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            '<tr><td>Bear</td><td>%s%%</td><td>%s</td><td>%s</td><td>%s</td></tr>'
            '</tbody></table>'
            '<p><strong>Probability-weighted target.</strong> %s '
            '(expected return %s%%, %s).</p>'
            % (f2("ttm_eps_diluted"), f2("ttm_gaap_pe") if r.get("ttm_gaap_pe") is not None else f2("ttm_pe"),
               f2("fy2026_eps_consensus"), f2("fy2027_eps_consensus"), f2("fy2028_eps_consensus"),
               f2("forward_gaap_pe_2027") if r.get("forward_gaap_pe_2027") is not None else f2("fwd_pe_2027"),
               f2("forward_gaap_pe_2028") if r.get("forward_gaap_pe_2028") is not None else f2("fwd_pe_2028"),
               f2("eps_growth_2026_2028_pct"), f2("eps_revision_pct"),
               f2("pe_3y_median"), f2("pe_3y_min"), f2("pe_3y_max"), f2("pe_3y_percentile"),
               f2("pe_5y_median"), f2("pe_5y_min"), f2("pe_5y_max"), f2("pe_5y_percentile"),
               f2("fwd_pe_premium_vs_median_pct"), v("valuation_method"), v("valuation_assumptions"),
               _pct100(r.get("bull_prob")), f2("bull_eps"), f2("bull_pe"), f2("bull_target"),
               _pct100(r.get("base_prob")), f2("base_eps"), f2("base_pe"), f2("base_target"),
               _pct100(r.get("bear_prob")), f2("bear_eps"), f2("bear_pe"), f2("bear_target"),
               f2("expected_price"), _fmt2(r.get("expected_return_pct")), v("probability_basis"))
        )
        prov = r.get("valuation_provenance") or {}
        prov_txt = "; ".join(
            "%s=%s" % (k, prov.get(k, ""))
            for k in ("ttm_eps_diluted", "fy2027_eps_consensus", "pe_5y_median", "base_target")
        )
        val_html += (
            '<table><thead><tr><th>Data integrity</th><th>Value</th></tr></thead><tbody>'
            '<tr><td>EPS basis / TTM period</td><td>%s / %s</td></tr>'
            '<tr><td>Split adjusted</td><td>%s</td></tr>'
            '<tr><td>H1 reported / H2 forecast</td><td>%s / %s</td></tr>'
            '<tr><td>FY EPS method 2027 / 2028</td><td>%s / %s</td></tr>'
            '<tr><td>Provenance</td><td>%s</td></tr>'
            '</tbody></table>'
            % (v("eps_basis"), v("ttm_period"), v("split_adjusted"),
               f2("h1_eps_reported"), f2("h2_eps_forecast"),
               v("fy2027_eps_method"), v("fy2028_eps_method"), _esc(prov_txt))
        )
        srcs = r.get("sources") or []
        src_html = ", ".join(
            '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            % (_esc_attr(str(u)), _esc(str(u)))
            for u in srcs if isinstance(u, str)
        )
        cards.append(
            '<div class="idea-card">\n'
            '<h3>%s &mdash; %s <span class="idea-meta">%s &middot; %s &middot; %s &middot; %s &middot; %s</span></h3>\n'
            '<p><strong>Current price.</strong> %s (as of %s). <strong>Entry.</strong> %s. '
            '<strong>Reassess.</strong> %s. <strong>Verification.</strong> %s.</p>\n'
            '<p><strong>Review.</strong> %s</p>\n'
            '<p><strong>Thesis.</strong> %s</p>\n'
            '<p><strong>Assumptions.</strong> %s</p>\n'
            '<p><strong>Why this versus alternatives.</strong> %s</p>\n'
            '<p><strong>Contrary evidence.</strong> %s</p>\n'
            '<p><strong>Peer comparison.</strong> %s</p>\n'
            '<p><strong>Sector context.</strong> %s</p>\n'
            '%s'
            '<table><thead><tr><th>Entry</th><th>Base</th><th>Bull</th><th>Bear</th>'
            '<th>Upside</th><th>Downside</th><th>Return from current</th><th>R/R</th></tr></thead><tbody>'
            '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s%%</td><td>%s%%</td><td>%s%%</td><td>%s</td></tr>'
            '</tbody></table>\n'
            '<p><strong>Bull case.</strong> %s</p>\n'
            '<p><strong>Base case.</strong> %s</p>\n'
            '<p><strong>Bear case.</strong> %s</p>\n'
            '<p><strong>Catalysts.</strong> %s</p>\n'
            '<p><strong>Risks.</strong> %s</p>\n'
            '<p><strong>Entry condition.</strong> %s <strong>Exit.</strong> %s</p>\n'
            '<p><strong>Conclusion.</strong> %s</p>\n'
            '<p><strong>Decision rationale.</strong> %s</p>\n'
            '<p><strong>Invalidation.</strong> %s</p>\n'
            '<p><strong>Strongest opposing argument.</strong> %s</p>\n'
            '<p class="idea-sources"><small>Sources: %s</small></p>\n'
            '</div>'
            % (e("ticker"), e("name"), e("sector"), e("security_type"), e("recommendation"),
               e("horizon"), e("reassess"),
               e("current_price"), e("price_date"), e("entry_price"), e("reassess"), e("verification"),
               e("review"), e("thesis"), e("assumptions"), e("why_vs_alternatives"), e("contrary"),
               e("peer_comparison"), e("sector_context"), fund_html + val_html,
               e2("entry_price"), e2("base_target"), e2("bull_target"), e2("bear_target"),
               e2("upside_pct"), e2("downside_pct"), e2("return_from_current_pct"), e2("risk_reward"),
               v("bull_rationale"), v("base_rationale"), v("bear_rationale"),
               e("catalysts"), e("risks"), e("entry_condition"), e("exit"),
               e("conclusion"), v("decision_rationale"), e("invalidation"), e("opposing"), src_html)
        )
    return "\n".join(cards) if cards else None


def render_narrative(narrative: dict) -> dict:
    """Render validated narrative sections into HTML fragments keyed by slot."""
    sections = narrative.get("sections") or {}
    if "sector_allocation" in narrative and "sector_allocation" not in sections:
        sections = dict(sections)
        sections["sector_allocation"] = narrative.get("sector_allocation")
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
        value = sections.get(key)
        # Single-stock ideas render as cards; table sections as tables; prose as
        # paragraphs.
        if key in CARD_SECTIONS:
            cards = _render_stock_ideas(value)
            if cards:
                out[key] = cards
                continue
        if key in TABLE_SECTIONS:
            table = _render_table_rows(value, TABLE_SECTIONS[key])
            if table:
                out[key] = table
                continue
        texts = _as_text_list(value) or []
        if texts:
            out[key] = "\n".join(f"<p>{_esc(t)}</p>" for t in texts)

    # External citations render as real links in the Sources block.
    src_html = render_sources(narrative)
    if src_html:
        out["sources"] = src_html

    if isinstance(sections.get("sector_allocation"), list):
        out["sector_allocation"] = sections["sector_allocation"]

    return out


def _esc_attr(text: str) -> str:
    """Attribute-safe escaping for href values."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#x27;")
    )


def render_sources(narrative: dict) -> str:
    """Render narrative['sources'] into an escaped <ul class="sources"> block.

    Returns an empty string when the narrative carries no external citations, so
    the generator can fall back to the built-in source list without special-casing.
    """
    sources = narrative.get("sources") or []
    if not isinstance(sources, list) or not sources:
        return ""
    items = []
    for item in sources:
        if not isinstance(item, dict):
            continue
        label = str(item.get("label") or "").strip()
        url = str(item.get("url") or "").strip()
        note = str(item.get("note") or "").strip()
        if not label or not url:
            continue
        if not re.match(r"^https?://[^\s<>\"']+$", url):
            continue
        anchor = (
            '<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            % (_esc_attr(url), _esc(label))
        )
        if note:
            items.append(f"<li>{anchor} &mdash; {_esc(note)}</li>")
        else:
            items.append(f"<li>{anchor}</li>")
    if not items:
        return ""
    return '<ul class="sources">\n' + "\n".join(items) + "\n</ul>"

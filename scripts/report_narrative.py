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
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

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
        "thesis", "assumptions", "why_vs_alternatives", "contrary",
        "catalysts", "risks", "entry_condition", "exit", "invalidation",
        "opposing", "reassess", "verification", "sources",
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


def _validate_stock_ideas(rows, narrative: dict, fails: list[str], evidence: dict) -> set:
    """Validate idea cards: fields, arithmetic, freshness, provenance. Returns tickers."""
    tickers: set = set()
    prev = {str(t).upper() for t in (evidence.get("previous_ideas") or [])}
    if not isinstance(rows, list) or not rows:
        fails.append("stock_ideas must be a non-empty list of idea objects")
        return tickers
    if not (3 <= len(rows) <= 5):
        fails.append("stock_ideas must contain 3-5 ideas (got %d)" % len(rows))
    global_sources = {str(s.get("url") or "").strip(): str(s.get("note") or "")
                      for s in (narrative.get("sources") or []) if isinstance(s, dict)}
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
        missing = [k for k in CARD_SECTIONS["stock_ideas"] if k not in row]
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
        for key in ("thesis", "assumptions", "why_vs_alternatives", "contrary",
                    "catalysts", "risks", "entry_condition", "exit", "invalidation", "opposing"):
            text = row.get(key)
            if not isinstance(text, str) or not text.strip():
                fails.append("stock_ideas[%d].%s must be a non-empty string" % (i, key))
            elif len(text) > 600:
                fails.append("stock_ideas[%d].%s exceeds 600 chars" % (i, key))
        assumptions = str(row.get("assumptions") or "").lower()
        if not any(k in assumptions for k in ("eps", "p/e", "multiple", "fcf", "dcf", "ebitda", "revenue")):
            fails.append("stock_ideas[%d].assumptions must state an explicit valuation basis "
                         "(EPS, P/E, multiple, FCF, DCF, EBITDA or revenue)" % i)
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
        if len(new_selected) < 2:
            fails.append("at least 2 selected ideas must be new versus the previous report "
                         "(found %d); carryovers are capped so the screen stays dynamic"
                         % len(new_selected))
    if not bearish:
        fails.append("stock_ideas must include at least one Sell, Reduce or Hold idea")
    if stock_count < 3:
        fails.append("stock_ideas must include at least 3 individual stocks "
                     "(security_type='Stock'), not only ETFs")
    return tickers


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
                unknown = [k for k in row if k not in CARD_SECTIONS[name]]
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
        if len(ext_claims) > 60:
            fails.append(f"external_claims has {len(ext_claims)} entries, max 60")
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
            '<p><strong>Thesis.</strong> %s</p>\n'
            '<p><strong>Assumptions.</strong> %s</p>\n'
            '<p><strong>Why this versus alternatives.</strong> %s</p>\n'
            '<p><strong>Contrary evidence.</strong> %s</p>\n'
            '<table><thead><tr><th>Entry</th><th>Base</th><th>Bull</th><th>Bear</th>'
            '<th>Upside</th><th>Downside</th><th>Return from current</th><th>R/R</th></tr></thead><tbody>'
            '<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s%%</td><td>%s%%</td><td>%s%%</td><td>%s</td></tr>'
            '</tbody></table>\n'
            '<p><strong>Catalysts.</strong> %s</p>\n'
            '<p><strong>Risks.</strong> %s</p>\n'
            '<p><strong>Entry condition.</strong> %s <strong>Exit.</strong> %s</p>\n'
            '<p><strong>Invalidation.</strong> %s</p>\n'
            '<p><strong>Strongest opposing argument.</strong> %s</p>\n'
            '<p class="idea-sources"><small>Sources: %s</small></p>\n'
            '</div>'
            % (e("ticker"), e("name"), e("sector"), e("security_type"), e("recommendation"),
               e("horizon"), e("reassess"),
               e("current_price"), e("price_date"), e("entry_price"), e("reassess"), e("verification"),
               e("thesis"), e("assumptions"), e("why_vs_alternatives"), e("contrary"),
               e("entry_price"), e("base_target"), e("bull_target"), e("bear_target"),
               e("upside_pct"), e("downside_pct"), e("return_from_current_pct"), e("risk_reward"),
               e("catalysts"), e("risks"), e("entry_condition"), e("exit"),
               e("invalidation"), e("opposing"), src_html)
        )
    return "\n".join(cards) if cards else None


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

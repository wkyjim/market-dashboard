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
from urllib.parse import urlsplit

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
        # Table sections may be a non-empty list of row dicts.
        if name in TABLE_SECTIONS and isinstance(value, list) and value \
                and all(isinstance(v, dict) for v in value):
            continue
        if not (_as_text_list(value) or []):
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
        # Structured row data renders as a table; prose falls back to paragraphs.
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

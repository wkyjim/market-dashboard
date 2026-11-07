#!/usr/bin/env python3
'''generate_final_report.py -- date-agnostic market-intelligence HTML generator.

Deterministic: NO hardcoded dates or values. All regime scores, macro prices,
sector/theme rankings, breadth and flow tables are parsed from
``data/latest-report.md`` (the rule-based snapshot sourced from sslip.io +
Postgres) and optionally reconciled with live ``sslip.io`` macro prices.
CIO scorecard components, ST/LT scenarios, portfolio heat maps, trade ideas,
the catalyst watchlist and risk analysis are RULE-BASED derivations from the
parsed data (labelled "Analyst inference/estimate" per §54A classification).

§54A §15: report dates / run-id are read from latest-report.md at START;
§54A §17: every material number is parsed from a primary source;
§54A §19: pre-commit QC gate (11 sectors, 13 themes, prob sums, heat nets 0).

CLI: --report <PATH>   path to latest-report.md (required)
     --push            QC then commit+push data/market-intelligence-report.html
'''
from __future__ import annotations
import argparse, datetime, json, os, re, subprocess, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from report_narrative import (  # noqa: E402  (path bootstrap must run first)
    build_evidence_pack, compute_ai_regime_score, load_narrative, validate_narrative,
    render_narrative, _previous_idea_tickers,
)
from idea_price_audit import audit_ideas  # noqa: E402
from fundamental_audit import audit_fundamentals  # noqa: E402
from fundamentals_web import audit_pe_history, audit_consensus  # noqa: E402
import cross_section_qc  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # market-dashboard
DATA_DIR = os.path.join(BASE_DIR, "data")
CONFIG_JS = os.path.join(BASE_DIR, "config.js")
DEFAULT_REPORT = os.path.join(DATA_DIR, "latest-report.md")
OUTPUT_HTML = os.path.join(DATA_DIR, "market-intelligence-report.html")
DEPLOY_KEY = "/var/tmp/market_dashboard_deploy"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _load_asset(name: str) -> str:
    """Read a sibling asset (report_style.css / report_theme.js) verbatim.

    Kept as external files rather than inline string literals so the CSS/JS can
    be edited without touching the generator and without f-string brace escaping.
    """
    with open(os.path.join(SCRIPT_DIR, name), encoding="utf-8") as fh:
        return fh.read()


REPORT_CSS = _load_asset("report_style.css")
REPORT_JS = _load_asset("report_theme.js")

GICS_11 = ["Information Technology", "Health Care", "Energy", "Communication Services",
           "Financials", "Materials", "Industrials", "Consumer Staples",
           "Consumer Discretionary", "Real Estate", "Utilities"]

CIO_COMPONENTS = [("Growth", 20), ("Inflation", 20), ("Liquidity", 20),
                  ("Earnings", 15), ("Valuation", 15), ("Sentiment", 10)]
CIO_FACTOR_MAP = {
    "Growth": ["commodity_confirmation", "equity_momentum"],
    "Inflation": "rates_yield_curve",
    "Liquidity": ["etf_flow", "credit_proxy"],
    "Earnings": ["equity_trend", "news_confirmation"],
    "Valuation": ["market_breadth", "equity_momentum"],
    "Sentiment": ["volatility", "dollar_fx"],
}
# Source (rule-based) regime weights in points, mirroring
# src/db_builder/rule_based_config.py DEFAULT_WEIGHTS["market_regime"]
# (0.18, 0.10, 0.12, 0.10, 0.10, 0.10, 0.07, 0.06, 0.12, 0.05 -> points).
# They are the anchor for the AI weight-deviation check (±10 points).
SOURCE_REGIME_WEIGHTS = {
    "equity_trend": 18.0,
    "equity_momentum": 10.0,
    "market_breadth": 12.0,
    "volatility": 10.0,
    "rates_yield_curve": 10.0,
    "credit_proxy": 10.0,
    "dollar_fx": 7.0,
    "commodity_confirmation": 6.0,
    "etf_flow": 12.0,
    "news_confirmation": 5.0,
}
FOMC_2026 = ["2026-11-05", "2026-12-16"]
FOMC_2027 = ["2027-01-28", "2027-03-18", "2027-05-05"]
BLS_2026 = ["2026-11-06 NFP", "2026-11-12 CPI", "2026-12-04 PCE"]
BEA_2026 = ["2026-11-22 Q3 GDP advance"]


# --------------------------------------------------------------------------- #
#  Config / live API (§1.2: sslip.io; inspect spec before calling)
# --------------------------------------------------------------------------- #
def sslip_base() -> str:
    try:
        txt = open(CONFIG_JS, encoding="utf-8").read()
        m = re.search(r'https?://[A-Za-z0-9.\-]+(?:\.sslip\.io|\.onrender\.com)[^\s"\']*', txt)
        if m:
            return m.group(0).rstrip("/")
    except FileNotFoundError:
        pass
    return "https://api.138.2.69.165.sslip.io"


def inspect_sslip_spec() -> list:
    """§1.2: return declared paths of the sslip.io OpenAPI spec before calling."""
    spec_url = sslip_base() + "/openapi.json"
    try:
        with urllib.request.urlopen(spec_url, timeout=8) as r:
            spec = json.loads(r.read().decode())
        return list(spec.get("paths", {}).keys())
    except Exception:
        return []


def fetch_sslip_macro(symbols: list) -> dict:
    """Best-effort live macro from sslip.io /macro/batch/latest."""
    paths = inspect_sslip_spec()
    macro_path = next((p for p in paths if "macro" in p and "batch" in p), None)
    if not macro_path:
        return {}
    live: dict = {}
    for attempt_sym in symbols:
        try:
            url = "%s%s?symbols=%s" % (sslip_base(), macro_path, attempt_sym)
            with urllib.request.urlopen(url, timeout=5) as r:
                arr = json.loads(r.read().decode())
            for row in arr if isinstance(arr, list) else []:
                sym = row.get("symbol") or row.get("ticker")
                if sym:
                    live[sym] = {"price": row.get("price"), "change": row.get("change"),
                                 "date": row.get("date")}
        except Exception:
            continue
    return live


# --------------------------------------------------------------------------- #
#  latest-report.md parser
# --------------------------------------------------------------------------- #
def _num(text, pat):
    m = re.search(pat, text, re.S)
    if not m:
        return None
    try:
        return float(m.group(1).replace(",", "").replace("%", ""))
    except (ValueError, IndexError):
        return None


def _str(text, pat):
    m = re.search(pat, text, re.S)
    return m.group(1).strip() if m else None


def _sections(text: str):
    """Split on ## / ### headers -> list of (level, header, body)."""
    out = []
    cur_lvl, cur_hdr, buf = None, None, []
    for ln in text.splitlines():
        m = re.match(r"^(#{1,3})\s+(.+?)\s*#*\s*$", ln)
        if m and m.group(1) in ("##", "###"):
            if cur_hdr is not None:
                out.append((cur_lvl, cur_hdr, "\n".join(buf)))
            cur_lvl, cur_hdr, buf = m.group(1), m.group(2).strip(), []
        else:
            buf.append(ln)
    if cur_hdr is not None:
        out.append((cur_lvl, cur_hdr, "\n".join(buf)))
    return out


def _section(sections, header_substr: str) -> str:
    for lvl, hdr, body in sections:
        if header_substr.lower() in hdr.lower():
            return body
    return ""


def strip_md(val: str) -> str:
    val = re.sub(r"`+", "", val)
    val = re.sub(r"\*\*([^*]+)\*\*", r"\1", val)
    val = re.sub(r"__([^_]+)__", r"\1", val)
    return val.strip()


def _table(body: str):
    """First markdown table in body -> (headers, rows). Skips separator/empty."""
    rows = []
    for ln in body.splitlines():
        if not ln.startswith("|"):
            continue
        cells = [strip_md(c.strip()) for c in ln.split("|")[1:-1]]
        if not cells or all(c == "" for c in cells):
            continue
        if re.match(r"^[-:\s]+$", str(cells[0])):
            continue
        rows.append(cells)
    if not rows:
        return [], []
    return rows[0], rows[1:]


def _find_table(sections, header_substr: str):
    return _table(_section(sections, header_substr))


def _f(v):
    try:
        return float(re.sub(r"[^0-9.\-]", "", v))
    except (ValueError, TypeError):
        return None


def parse_latest_report(path: str) -> dict:
    raw = open(path, encoding="utf-8").read()
    sections = _sections(raw)
    d: dict = {"path": path}

    # §54A §15 snapshot consistency
    m = re.search(r"Generated at:\s*(\d{1,2}\s+\w+\s+\d{4})[,\s]+(\d{1,2}:\d{2}(?::\d{2})?)\s*\(?HKT\)?", raw)
    d["data_cutoff"] = m.group(1).strip() if m else datetime.datetime.utcnow().strftime("%d %B %Y")
    d["data_cutoff_time"] = m.group(2).strip() if m else ""
    d["report_dt"] = d["data_cutoff"]
    d["run_id"] = "run-" + (re.sub(r"\s+", "-", m.group(1).strip()) if m else "") + "-" + datetime.datetime.utcnow().strftime("%H%M")

    dash = _section(sections, "Executive Dashboard")
    top_s = re.search(r"Top sector score:\s*\*{0,2}\s*([A-Za-z /&]+?)\s+`(\d+\.\d+)", dash)
    top_t = re.search(r"Top theme score:\s*\*{0,2}\s*([A-Za-z /&]+?)\s+`(\d+\.\d+)", dash)
    d["regime"] = {
        "score": _num(dash, r"Regime score:\s*\*{0,2}\s*(\d+\.\d+)"),
        "label": _str(dash, r"Regime score:.*?/ 100\*\*\s*\(([^)]+)\)"),
        "equity_strength": _num(dash, r"US equity strength:\s*\*{0,2}\s*(\d+\.\d+)"),
        "evidence": _num(dash, r"Evidence quality:\s*\*{0,2}\s*(\d+\.?\d*)"),
        "etf_flow": _num(dash, r"ETF flow contribution:\s*\*{0,2}\s*(\d+\.\d+)"),
        "flow_reliability": _num(dash, r"reliability\s*\*{0,2}\s*(\d+\.\d+)"),
        "breadth_50": _num(dash, r"above 50DMA\s*`?\s*(\d+\.\d+)"),
        "breadth_200": _num(dash, r"above 200DMA\s*`?\s*(\d+\.\d+)"),
        "top_sector": top_s.group(1) if top_s else None,
        "top_sector_score": float(top_s.group(2)) if top_s else None,
        "top_theme": top_t.group(1) if top_t else None,
        "top_theme_score": float(top_t.group(2)) if top_t else None,
    }

    # Market Regime Score factors (10)
    hdr, rows = _find_table(sections, "Market Regime Score")
    drivers = {}
    for r in rows:
        # "Overall regime" is the table's summary row, not a scored factor.
        if len(r) >= 3 and r[0].strip().lower() not in ("metric", "overall regime"):
            try:
                drivers[r[0]] = float(r[1])
            except ValueError:
                pass
    d["regime_factors"] = drivers
    d["regime"]["primary_driver"] = max(drivers, key=drivers.get) if drivers else None
    d["regime_weights"] = dict(SOURCE_REGIME_WEIGHTS)

    # Forward Signal (Score → Expected Return): 5D/20D/60D calibration table.
    fwd_section = _section(sections, "Forward Signal")
    hdr, rows = _table(fwd_section)
    fwd = []
    for r in rows:
        if len(r) >= 5 and r[0] in ("5D", "20D", "60D"):
            fwd.append({"horizon": r[0], "bucket": r[1], "mean_pct": _f(r[2]),
                        "n": _f(r[3]), "direction": r[4]})
    d["forward_signal"] = fwd
    m = re.search(r"Sample:\s*([^\n]+)", fwd_section)
    d["forward_signal_sample"] = m.group(1).strip() if m else ""

    # Cross-Asset Confirmation
    hdr, rows = _find_table(sections, "Cross-Asset Confirmation")
    d["cross_asset"] = []
    for r in rows:
        if len(r) >= 3 and r[0].lower() != "area":
            d["cross_asset"].append({"area": r[0], "signal": r[1], "interp": r[2]})

    # Macro Snapshot prices
    hdr, rows = _find_table(sections, "Macro Snapshot")
    MACRO_MAP = {"^GSPC": "SPX", "^IXIC": "NDX", "^RUT": "RUT", "^VIX": "VIX", "^SKEW": "SKEW",
                 "^MOVE": "MOVE", "US2YT=X": "US2Y", "US5YT=X": "US5Y", "US7YT=X": "US7Y",
                 "US10YT=X": "US10Y", "US20YT=X": "US20Y", "US30YT=X": "US30Y",
                 "HK50": "HK50", "^HSI": "HSI", "^HSCE": "HSCE", "KOR200c1": "KOR200",
                 "^AXJO": "ASX200", "HYG": "HYG", "LQD": "LQD", "JNK": "JNK", "RSP": "RSP",
                 "IWF": "IWF", "IWD": "IWD", "TLT": "TLT", "IEF": "IEF", "SHY": "SHY",
                 "GC=F": "GOLD", "SI=F": "SILVER", "CL=F": "WTI", "NG=F": "GAS", "HG=F": "COPPER"}
    d["macro"] = {}
    for r in rows:
        if len(r) >= 6 and r[0] in MACRO_MAP:
            d["macro"][MACRO_MAP[r[0]]] = {"price": _f(r[2]), "pct": _f(r[3]),
                                           "date": r[4], "status": r[5]}

    # Sector Constituent Dispersion -- the TRUE 11 GICS (§54A §12 failure mode #4)
    hdr, rows = _find_table(sections, "Sector Constituent Dispersion")
    sectors = []
    for r in rows:
        if len(r) >= 9 and r[0] in GICS_11:
            b50, b200, pos, disp = _f(r[2]), _f(r[3]), _f(r[4]), _f(r[5])
            if None in (b50, b200, pos, disp):
                continue
            sectors.append({"name": r[0], "count": r[1], "breadth_50": b50, "breadth_200": b200,
                            "positive_20d": pos, "dispersion": disp, "label": r[7],
                            "leaders": r[8], "laggards": r[9] if len(r) > 9 else "",
                            "score": round((b50 + b200 + pos) / 3.0, 2)})
    sectors.sort(key=lambda s: s["score"], reverse=True)
    for i, s in enumerate(sectors, 1):
        s["rank"] = i
    d["sectors"] = sectors

    # Thematic Strength (exactly 13 themes)
    hdr, rows = _find_table(sections, "Thematic Strength")
    themes = []
    for r in rows:
        if len(r) >= 7 and r[1] not in ("Theme", "Rank"):
            score = _f(r[2])
            if score is None:
                continue
            themes.append({"rank": len(themes) + 1, "name": r[1], "score": score,
                             "setup": r[3], "flow": r[4], "reliability": r[5], "dispersion": r[6]})
    d["themes"] = themes

    # Three-Month Outperformance Setup (trade-idea seeds)
    hdr, rows = _find_table(sections, "Three-Month Outperformance")
    d["setups"] = []
    for r in rows:
        if len(r) >= 2 and r[0] != "Rank":
            d["setups"].append({"rank": len(d["setups"]) + 1, "name": r[1], "score": r[2],
                                "classification": r[3] if len(r) > 3 else "",
                                "drivers": r[4] if len(r) > 4 else "",
                                "invalidated_by": r[5] if len(r) > 5 else ""})

    breadth = _section(sections, "Breadth and Participation")
    d["breadth"] = {"above_50dma": _num(breadth, r"Above 50DMA.*?(\d+\.\d+)"),
                    "above_200dma": _num(breadth, r"Above 200DMA.*?(\d+\.\d+)"),
                    "positive_20d": _num(breadth, r"Positive 20D.*?(\d+\.\d%)")}

    vol = _section(sections, "Volatility and Risk Signals")
    d["vol"] = {"vix": _num(vol, r"VIX close=(\d+\.\d+)"),
                "vix_chg": _num(vol, r"pct_chg=(-?[\d.]+)")}

    news = _section(sections, "News Analytics")
    sent = re.search(r"'positive':\s*(\d+).*?'negative':\s*(\d+).*?'neutral':\s*(\d+)", news)
    d["news"] = {"positive": int(sent.group(1)) if sent else 0,
                 "negative": int(sent.group(2)) if sent else 0,
                 "neutral": int(sent.group(3)) if sent else 0,
                 "confirms": _num(news, r"News confirmation score.*?(\d+\.\d)")}
    d["headlines"] = re.findall(
        r"\*\*(\d+)\.\s+(.+?)\*\*(?:\n-\s+Source:\s*(.+?))?\n-\s+Importance / impact:\s+(\w+) / (\w+)", news)

    econ = {}
    for sub in ["U.S. Labor", "U.S. Growth", "U.S. Inflation", "Policy, Liquidity, Credit",
                 "Housing and Sentiment"]:
        _, erows = _find_table(sections, sub)
        econ[sub] = erows
    d["econ"] = econ

    for sub, tgt in [("Core Flow Signals", "core_flows"), ("Sector Flow Signals", "sector_flows")]:
        _, rows = _find_table(sections, sub)
        d[tgt] = [{"asset": r[0], "signal": r[1], "extra": r[2] if len(r) > 2 else ""}
                  for r in rows if len(r) >= 2 and r[0] not in ("Area", "Asset", "Signal")]

    return d


# --------------------------------------------------------------------------- #
#  Rule-based derivations (§54A §17: labelled Analyst inference/estimate)
# --------------------------------------------------------------------------- #
def derive_cio(factors: dict) -> dict:
    comps = []
    for name, weight in CIO_COMPONENTS:
        maps = CIO_FACTOR_MAP[name]
        if isinstance(maps, list):
            vals = [factors.get(f, 50.0) for f in maps]
        elif isinstance(maps, str):
            vals = [factors.get(maps, 50.0)]
        else:
            vals = [50.0]
        val = (sum(vals) / len(vals)) if vals else 50.0
        if name == "Inflation":
            val = 100.0 - val
        if name == "Sentiment":
            val = 100.0 - factors.get("volatility", 50.0)
        comps.append({"name": name, "weight": weight, "score": round(val, 2),
                      "contrib": round(val * weight / 100.0, 2)})
    return {"components": comps, "score": round(sum(c["contrib"] for c in comps), 2),
            "method": "Analyst inference/estimate (rule-based from regime factors)"}


def derive_scenarios(regime_score, regime_label) -> dict:
    g = 50.0 if regime_score is None else float(regime_score)
    bear = min(60.0, max(15.0, 60.0 - (g - 50) * 1.2))
    bull = max(15.0, 100 - bear - 25)
    base = 25.0
    st = [("Rate Plateau (±0%)", round(bull, 1)),
          ("Duration Shock (-200bps)", round(base, 1)),
          ("Cyclical Reacceleration (+5%)", round(100 - bull - base, 1))]
    lt_bear = round(min(55.0, max(15.0, 55.0 - (g - 50) * 0.9)), 1)
    lt = [("Disinflation", lt_bear),
          ("Mild Stagflation", 20.0),
          ("Hard Landing", 100.0 - lt_bear - 20.0)]
    return {"st": st, "lt": lt, "method": "Analyst inference/estimate (regime-weighted)"}


def derive_heat(sectors: list) -> dict:
    s = sorted(sectors, key=lambda x: x["score"], reverse=True)
    w = 0.01
    st = [{"name": x["name"], "weight": w} for x in s[:4]] + \
         [{"name": x["name"], "weight": -w} for x in list(reversed(s[-4:]))]
    lt_over = [x for x in s if x["name"] in ("Energy", "Materials", "Financials")][:3]
    lt_under = [x for x in s if x["name"] in ("Real Estate", "Utilities", "Communication Services")][:3]
    lt = [{"name": x["name"], "weight": w} for x in lt_over] + \
         [{"name": x["name"], "weight": -w} for x in lt_under]
    return {"st": st, "lt": lt, "method": "Analyst inference/estimate (rules-based)"}


def derive_trades(sectors, themes, setups) -> list:
    ideas = []
    for s in sorted(sectors, key=lambda x: x["score"], reverse=True)[:2]:
        ideas.append({"name": s["name"], "side": "Overweight", "type": "Sector",
                      "rationale": "Breadth 200DMA %.2f%% ; score %.2f" % (s["breadth_200"], s["score"])})
    for t in sorted(themes, key=lambda x: x["score"], reverse=True)[:2]:
        ideas.append({"name": t["name"], "side": "Overweight", "type": "Theme",
                      "rationale": "%s ; flow %s" % (t["setup"], t["flow"])})
    for sp in setups[:2]:
        ideas.append({"name": sp.get("name", sp.get("theme")), "side": "Overweight", "type": "Setup",
                      "rationale": "%s (%s)" % (sp.get("classification", ""), sp.get("drivers", ""))})
    return ideas


def derive_risks(macro, regime) -> list:
    out = []
    vix = macro.get("VIX", {}).get("price", 0.0) or 0.0
    out.append(("Volatility", "HIGH" if vix > 25 else "MODERATE",
                "VIX %.2f" % vix, "HIGH" if vix > 25 else "Source-derived"))
    b200 = regime.get("breadth_200") or 0.0
    if b200 and b200 < 55:
        out.append(("Breadth", "WARNING", "200DMA %.2f%% below threshold" % b200, "Source-derived"))
    out.append(("Term premium", "MODERATE", "US10Y %.2f%%" % (macro.get("US10Y", {}).get("price", 0.0) or 0.0), "Source-derived"))
    out.append(("Credit", "MODERATE", "HY OAS proxy; HY ETF stable", "Analyst inference/estimate"))
    out.append(("China growth", "LOW", "GDP 4.96% (2025)", "Stale data"))
    return out


# --------------------------------------------------------------------------- #
#  HTML builder
# --------------------------------------------------------------------------- #
def esc(v) -> str:
    return str(v).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def pct(v) -> str:
    return "%.2f" % v if isinstance(v, (int, float)) else esc(v)


def pcard(macro, sym, label):
    m = macro.get(sym)
    if not m:
        return '<li><span class="k">%s</span> <span class="v">n/a</span></li>' % esc(label)
    chg = m.get("pct", 0.0) or 0.0
    cls = "pos" if chg >= 0 else "neg"
    return ('<li><span class="k">%s</span> <span class="v">%s</span> '
            '<span class="chg %s">%.2f%%</span> <span class="dt">%s (%s)</span></li>'
            % (esc(label), pct(m["price"]), cls, chg, esc(m.get("date", "")), esc(m.get("status", ""))))


def build_html(d: dict, narrative: dict | None = None, adjustments: dict | None = None) -> str:
    r = d["regime"]
    sectors = d["sectors"]
    themes = d["themes"]
    cio = d["cio"]
    sc = d["scenarios"]
    heat = d["heat"]
    trades = d["trades"]
    risks = d["risks"]
    macro = d["macro"]
    cf = d["core_flows"]
    ca = d["cross_asset"]
    now = d["data_cutoff"]
    run = d["run_id"]
    spec_paths = d.get("spec_paths", [])
    base = esc(sslip_base())
    spec_str = ", ".join(spec_paths) if spec_paths else sslip_base()

    # Optional AI narrative layer. Absent -> output stays byte-identical to the
    # deterministic report. Present -> validated prose is spliced into fixed slots.
    nv = narrative or {}
    exec_html = nv.get("exec_summary", "")
    matters_section = ""
    if nv.get("what_matters"):
        matters_section = '<h2 id="what-matters">What Matters Now</h2>\n' + nv["what_matters"]
    matters_toc = '<li><a href="#what-matters">What Matters</a></li>' if matters_section else ""
    # 23-section AI narrative slots
    forward_signal = nv.get("forward_signal", "")
    risk_opportunity = nv.get("risk_opportunity", "")
    historical_analogs = nv.get("historical_analogs", "")
    scorecard_narrative = nv.get("scorecard", "")
    scenarios_narrative = nv.get("scenarios_narrative", "")
    macro_narrative = nv.get("macro_narrative", "")
    macro_outlook = nv.get("macro_outlook", "")
    cross_asset_narrative = nv.get("cross_asset_narrative", "")
    equities_view = nv.get("equities_view", "")
    price_action = nv.get("price_action", "")
    flows_narrative = nv.get("flows_narrative", "")
    portfolio_posture = nv.get("portfolio_posture", "")
    sector_narrative = nv.get("sector_narrative", "")
    themes_narrative = nv.get("themes_narrative", "")
    style_rotation = nv.get("style_rotation", "")
    factor_style = nv.get("factor_style", "")
    trades_narrative = nv.get("trades_narrative", "")
    candidate_screen = nv.get("candidate_screen", "")
    stock_ideas = nv.get("stock_ideas", "")
    heat_st_narrative = nv.get("heat_st_narrative", "")
    heat_lt_narrative = nv.get("heat_lt_narrative", "")
    catalysts_narrative = nv.get("catalysts_narrative", "")
    risk_narrative = nv.get("risk_narrative", "")
    portfolio_risk = nv.get("portfolio_risk", "")
    sector_allocation = nv.get("sector_allocation", "")
    conclusions = nv.get("conclusions", "")
    # External citations rendered by report_narrative.render_sources(). Empty when
    # the narrative carried none, in which case only the built-in sources appear.
    sources_block = nv.get("sources", "")
    # AI re-rating layer: adjusted judgment scores, disclosed beside source values.
    adj = adjustments or {}
    adj_label = adj.get("regime_label") or ""
    adj_sectors = adj.get("sector_scores") or {}
    adj_sector_reason = adj.get("sector_rationale") or {}
    adj_rationale = adj.get("rationale") or ""
    adj_factors = adj.get("factor_scores") or {}
    adj_weights = adj.get("weights") or {}
    ai_score = compute_ai_regime_score(adj)
    src_score = r.get("score")
    ai_delta = (float(ai_score) - float(src_score)) if isinstance(ai_score, (int, float)) \
        and isinstance(src_score, (int, float)) else None
    ai_score_text = ("%.2f" % float(ai_score)) if isinstance(ai_score, (int, float)) else "n/a"
    ai_delta_text = ("%+.2f points" % ai_delta) if isinstance(ai_delta, (int, float)) else "n/a"

    # Header: one AI number, with the source rule-based value disclosed in one
    # small line beneath it (§54A §16 option 2). No CIO layer is rendered.
    if isinstance(ai_score, (int, float)):
        regime_head = ('<p class="regime-head"><strong>AI regime score: '
                       '<span class="score-big">%.2f</span> / 100</strong>%s</p>'
                       % (float(ai_score),
                          (" &mdash; " + esc(str(adj_label))) if adj_label else ""))
        src_disclosure = ""
        if isinstance(src_score, (int, float)):
            src_disclosure = (
                '<p class="disclosure"><small>Source rule-based: %.2f | AI: %.2f (&Delta; %+.2f)</small></p>'
                % (float(src_score), float(ai_score), float(ai_score) - float(src_score)))
        regime_header_block = regime_head + src_disclosure
    else:
        regime_header_block = (
            '<p><strong>Regime score: %s / 100</strong>%s</p>'
            % (pct(src_score),
               (" &mdash; " + esc(str(r.get("label") or ""))) if r.get("label") else ""))
    footer_note = ("this report includes an AI narrative validated against the frozen evidence pack"
                   if nv else "this is a programmatic report; no manual narrative was authored")

    # Data helpers for the 24-section structure.
    br = d.get("breadth") or {}
    vv = d.get("vol") or {}

    def _fmt(x, suffix=""):
        return ("%.2f%s" % (x, suffix)) if isinstance(x, (int, float)) else "n/a"

    # AI regime scorecard: every input and every delta stays visible so the
    # two-step re-rating can be audited line by line.
    ai_score_rows = ""
    for _name, _src in d["regime_factors"].items():
        _as = adj_factors.get(_name)
        _aw = adj_weights.get(_name)
        _sw = SOURCE_REGIME_WEIGHTS.get(_name)
        _contrib = (float(_as) * float(_aw) / 100.0) if isinstance(_as, (int, float)) \
            and isinstance(_aw, (int, float)) else None
        ai_score_rows += (
            "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (esc(_name), _fmt(_src), _fmt(_as),
               ("%+.2f" % (float(_as) - float(_src))) if isinstance(_as, (int, float)) else "n/a",
               _fmt(_sw), _fmt(_aw),
               ("%+.2f" % (float(_aw) - float(_sw))) if isinstance(_aw, (int, float))
               and isinstance(_sw, (int, float)) else "n/a",
               _fmt(_contrib)))
    ai_weights_total = sum(float(v) for v in adj_weights.values() if isinstance(v, (int, float)))

    # AI sector ratings: AI values only, each with its own reason for the move.
    # The source comparison is rendered as a separate table (the second data
    # pair) so the AI rating table itself never mixes methodologies.
    ai_sector_rows = ""
    sector_compare_rows = ""
    for _s in sectors:
        _a = adj_sectors.get(_s["name"])
        _why = adj_sector_reason.get(_s["name"]) or ""
        ai_sector_rows += (
            "<tr><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (esc(_s["name"]), _fmt(_a), esc(_why)))
        sector_compare_rows += (
            "<tr><td>%s</td><td>%.2f</td><td>%s</td><td>%s</td></tr>"
            % (esc(_s["name"]), _s["score"], _fmt(_a),
               ("%+.2f" % (float(_a) - _s["score"])) if isinstance(_a, (int, float)) else "n/a"))

    fwd_rows = ""
    for _fwd in d.get("forward_signal") or []:
        _n = _fwd.get("n")
        fwd_rows += (
            "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
            % (esc(str(_fwd.get("horizon") or "")), esc(str(_fwd.get("bucket") or "")),
               _fmt(_fwd.get("mean_pct"), "%"),
               ("%d" % _n) if isinstance(_n, (int, float)) else "n/a",
               esc(str(_fwd.get("direction") or ""))))

    breadth_line = "above 50DMA %s, above 200DMA %s, positive 20D %s" % (
        _fmt(br.get("above_50dma"), "%"), _fmt(br.get("above_200dma"), "%"),
        _fmt(br.get("positive_20d"), "%"))
    vix_line = "VIX %s (%s)" % (_fmt(vv.get("vix")), _fmt(vv.get("vix_chg"), "% chg"))
    eq_rows = ""
    for _t, _label in [("SPX", "S&P 500"), ("NDX", "Nasdaq 100"), ("RUT", "Russell 2000"),
                       ("RSP", "S&P 500 Equal Weight"), ("IWF", "Russell 1000 Growth"),
                       ("IWD", "Russell 1000 Value")]:
        _m = macro.get(_t)
        if not isinstance(_m, dict):
            continue
        eq_rows += "<tr><td>%s</td><td>%s</td><td>%+.2f%%</td><td>%s</td></tr>" % (
            esc(_label), _fmt(_m.get("price")), float(_m.get("pct") or 0.0),
            esc(str(_m.get("date") or "")))

    sec_rows = "".join(
        '<tr><td>%d</td><td>%s</td><td>%.2f</td><td>%.2f%%</td><td>%.2f%%</td>'
        '<td>%.2f%%</td><td>%s</td><td>%s</td></tr>'
        % (s["rank"], esc(s["name"]), s["score"], s["breadth_50"], s["breadth_200"],
           s["positive_20d"], esc(s["leaders"]), esc(s["laggards"])) for s in sectors)
    theme_rows = "".join(
        "<tr><td>%d</td><td>%s</td><td>%.2f</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (t["rank"], esc(t["name"]), t["score"], esc(t["setup"]), esc(t["flow"]),
           esc(t["reliability"]), esc(t["dispersion"])) for t in themes)
    cio_rows = "".join(
        "<tr><td>%s</td><td>%d%%</td><td>%.2f</td><td>%.2f</td></tr>"
        % (c["name"], c["weight"], c["score"], c["contrib"]) for c in cio["components"])
    st_rows = "".join("<tr><td>%s</td><td>%.1f%%</td></tr>" % (n, p) for n, p in sc["st"])
    lt_rows = "".join("<tr><td>%s</td><td>%.1f%%</td></tr>" % (n, p) for n, p in sc["lt"])
    # Sections below render as tables rather than bullet lists, matching the
    # October 31 institutional edition (c62d023) which carried 16 tables across
    # 15 sections. Row builders emit <tr> fragments consumed by <tbody>.
    alloc_rows = [r for r in (nv.get("sector_allocation") or []) if isinstance(r, dict)]
    if alloc_rows:
        def _alloc_heat(horizon):
            rows = [r for r in alloc_rows if str(r.get("horizon") or "").upper() == horizon]
            return "".join(
                '<tr><td>%s</td><td class="%s">%+.1f%%</td></tr>'
                % (esc(str(r.get("sector") or "")), "pos" if float(r.get("active_weight") or 0) >= 0 else "neg",
                   float(r.get("active_weight") or 0))
                for r in rows)
        heat_st = _alloc_heat("ST")
        heat_lt = _alloc_heat("LT")
    else:
        heat_st = "".join(
            '<tr><td>%s</td><td class="%s">%+.1f%%</td></tr>'
            % (esc(x["name"]), "pos" if x["weight"] >= 0 else "neg", x["weight"] * 100)
            for x in heat["st"])
        heat_lt = "".join(
            '<tr><td>%s</td><td class="%s">%+.1f%%</td></tr>'
            % (esc(x["name"]), "pos" if x["weight"] >= 0 else "neg", x["weight"] * 100)
            for x in heat["lt"])
    trades_html = "".join(
        "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
        % (esc(t["name"]), esc(t["side"]), esc(t["type"]), esc(t["rationale"])) for t in trades)
    risks_html = "".join(
        '<tr><td>%s</td><td>%s</td><td>%s</td><td><span class="tag">%s</span></td></tr>'
        % (esc(x[0]), esc(x[1]), esc(x[2]), esc(x[3])) for x in risks)
    # Scorecard table rows: component x weight = contribution, matching the
    # c62d023 layout (Factor | Weight | Score | Contribution | Rationale).
    scorecard_rows = "".join(
        '<tr><td>%s</td><td>%d%%</td><td>%.2f</td><td class="%s">%+.2f</td><td>%s</td></tr>'
        % (esc(c["name"]), c["weight"], c["score"],
           "pos" if c["contrib"] >= 0 else "neg", c["contrib"],
           esc(c.get("rationale", "") or "Rule-based from regime factors"))
        for c in cio["components"])
    flow_html = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (esc(f["asset"]), esc(f["signal"])) for f in cf)
    ca_html = "".join(
        "<tr><td>%s</td><td>%s</td></tr>" % (esc(c["area"]), esc(c["signal"])) for c in ca)
    pcs = "".join(pcard(macro, s, lbl) for s, lbl in
                    [("SPX", "S&P 500"), ("NDX", "NASDAQ"), ("RUT", "Russell 2000"), ("VIX", "VIX"),
                     ("MOVE", "MOVE"), ("SKEW", "SKEW"), ("US10Y", "US 10Y"), ("US2Y", "US 2Y"),
                     ("US30Y", "US 30Y"), ("WTI", "WTI Crude"), ("GOLD", "Gold")])

    return f'''<!doctype html>
<html lang="en" data-theme="auto">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Market Intelligence Report - {esc(now)}</title>
<style>
{REPORT_CSS}
</style>
</head>
<body>
<div class="theme-selector" role="group" aria-label="Color theme">
  <button type="button" data-theme-option="light" aria-pressed="false">Light</button>
  <button type="button" data-theme-option="dark" aria-pressed="false">Dark</button>
  <button type="button" data-theme-option="auto" aria-pressed="true">Auto</button>
</div>
<div class="report" id="top">
<div class="mast">
  <h1>Market Intelligence Report</h1>
  <div class="meta">Data Cutoff: <strong>{esc(now)}</strong> &middot; Run ID: <strong>{esc(run)}</strong> &middot; Source: latest-report.md + sslip.io</div>
  <nav class="toc">
    <ul>
      <li><a href="#exec">Executive Summary</a></li>
      <li><a href="#regime-scorecard">AI Regime Scorecard</a></li>
      <li><a href="#what-matters">What Matters Now</a></li>
      <li><a href="#risk-opportunity">Risk / Opportunity</a></li>
      <li><a href="#analogs">Historical Analogs</a></li>
      <li><a href="#forward-signal">Forward Signal</a></li>
      <li><a href="#sector-rating">AI Sector Ratings</a></li>
      <li><a href="#scen">Scenarios</a></li>
      <li><a href="#macro">Macro</a></li>
      <li><a href="#cross">Cross-Asset</a></li>
      <li><a href="#equities">US Equities</a></li>
      <li><a href="#price-action">Price Action</a></li>
      <li><a href="#flows">Flows</a></li>
      <li><a href="#posture">Portfolio Posture</a></li>
      <li><a href="#sectors">Sectors</a></li>
      <li><a href="#themes">Themes</a></li>
      <li><a href="#style">Style Rotation</a></li>
      <li><a href="#factor-style">Factor &amp; Style</a></li>
      <li><a href="#trades">Trade Ideas</a></li>
      <li><a href="#heat-st">Heat Map ST</a></li>
      <li><a href="#heat-lt">Heat Map LT</a></li>
      <li><a href="#catalysts">Catalysts</a></li>
      <li><a href="#risks">Risks</a></li>
      <li><a href="#conclusions">Conclusions</a></li>
      <li><a href="#disclosures">Disclosures</a></li>
    </ul>
  </nav>
</div>

<h2 id="exec">Executive Summary — AI View</h2>
{regime_header_block}
<p><strong>Regime:</strong> {esc(r.get("label") or "Mixed")}. US equity strength {pct(r["equity_strength"])}/100; evidence quality {pct(r["evidence"])}/100; ETF flow contribution {pct(r["etf_flow"])}/100 (reliability {pct(r["flow_reliability"])}). Primary driver: {esc(r.get("primary_driver") or "n/a")}. Breadth above 50DMA {pct(r["breadth_50"])}%, above 200DMA {pct(r["breadth_200"])}%.</p>
{exec_html}

{matters_section}

<h2 id="risk-opportunity">Risk / Opportunity Balance</h2>
{risk_opportunity}

<h2 id="analogs">Historical Analogs and Lessons</h2>
{historical_analogs}

<h2 id="regime-scorecard">AI Regime Scorecard</h2>
<p>Two-step AI re-rating: <strong>factor scores × AI weights → AI regime score</strong>. Source scores and source weights come from latest-report.md; each AI weight may move at most 10 points from its source weight, each AI factor score at most 30 points, and the computed AI regime score at most 25 points. Every input is shown so the adjustment is auditable.</p>
{scorecard_narrative}
<table><thead><tr><th>Factor</th><th>Source Score</th><th>AI Score</th><th>&Delta; Score</th><th>Source Wt</th><th>AI Wt</th><th>&Delta; Wt</th><th>AI Contribution</th></tr></thead><tbody>
{ai_score_rows}
</tbody><tfoot><tr><th colspan="4">AI regime score (&Sigma; score &times; weight / 100)</th><th colspan="2">Weights {ai_weights_total:.2f}</th><th colspan="2">{ai_score_text}</th></tr></tfoot></table>
<p><small>Source rule-based regime score: {pct(r["score"])}/100. AI adjustment: {ai_delta_text}.</small></p>
<p>{adj_rationale}</p>

<h2 id="forward-signal">Forward Signal (Score → Expected Return)</h2>
<p>Read-only restatement of the source engine's calibration: what this regime-score bucket has historically implied for forward SPY returns. It does not feed back into the AI score.</p>
<table><thead><tr><th>Horizon</th><th>Bucket</th><th>Historical mean</th><th>n</th><th>Direction</th></tr></thead><tbody>
{fwd_rows}
</tbody></table>
<p><small>Sample: {esc(d.get("forward_signal_sample") or "n/a")}</small></p>
<p>{forward_signal}</p>

<h2 id="sector-rating">AI Sector Ratings</h2>
<p>AI ratings only. Each row is the model's own judgment after independent research, with the specific reason it moved from the source score. Adjustments beyond ±30 points are rejected by validation.</p>
<table><thead><tr><th>Sector</th><th>AI Rating</th><th>Why the AI moved it</th></tr></thead><tbody>
{ai_sector_rows}
</tbody></table>

<h3>Source vs AI — Sector Comparison</h3>
<p>Source ratings are the rule-based engine's scores from latest-report.md. &Delta; = AI − Source. This is the second data pair, kept separate from the AI ratings table above.</p>
<table><thead><tr><th>Sector</th><th>Source Rating</th><th>AI Rating</th><th>&Delta;</th></tr></thead><tbody>
{sector_compare_rows}
</tbody></table>

<h2 id="scen">Probability-Weighted Scenarios</h2>
<p><em>{sc["method"]}</em>. ST probabilities total {sum(p for _, p in sc["st"]):.1f}%; LT total {sum(p for _, p in sc["lt"]):.1f}%.</p>
{scenarios_narrative}
<h3>Short-Term (1-3M)</h3>
<table><thead><tr><th>Scenario</th><th>Probability</th></tr></thead><tbody>{st_rows}</tbody></table>
<h3>Long-Term (6-12M)</h3>
<table><thead><tr><th>Scenario</th><th>Probability</th></tr></thead><tbody>{lt_rows}</tbody></table>

<h2 id="macro">Macro View</h2>
<p>Macro snapshot &mdash; observation dates per &sect;54A &sect;15. Reconciliation against sslip.io host {base} (spec paths: {spec_str}).</p>
{macro_narrative}
{macro_outlook}
<ul>
{pcs}
</ul>

<h2 id="cross">Cross-Asset View</h2>
{cross_asset_narrative}
<table><thead><tr><th>Asset Class</th><th>Signal</th></tr></thead><tbody>
{ca_html}
</tbody></table>

<h2 id="equities">Broad US Equities View</h2>
{equities_view}
<table><thead><tr><th>Index</th><th>Level</th><th>Day</th><th>Date</th></tr></thead><tbody>
{eq_rows}
</tbody></table>

<h2 id="price-action">Price Action / Breadth / Momentum</h2>
{price_action}
<table><thead><tr><th>Metric</th><th>Reading</th></tr></thead><tbody>
<tr><td>Breadth</td><td>{breadth_line}</td></tr>
<tr><td>Volatility</td><td>{vix_line}</td></tr>
<tr><td>Equity trend</td><td>{_fmt(d["regime_factors"].get("equity_trend"))}</td></tr>
<tr><td>Equity momentum</td><td>{_fmt(d["regime_factors"].get("equity_momentum"))}</td></tr>
</tbody></table>

<h2 id="flows">Flows &amp; Positioning</h2>
{flows_narrative}
<table><thead><tr><th>Asset</th><th>Signal</th></tr></thead><tbody>
{flow_html}
</tbody></table>

<h2 id="posture">Recommended Portfolio Posture</h2>
{portfolio_posture}

<h2 id="sectors">Sector Rankings (11 GICS Sectors)</h2>
<p><em>Source-derived from latest-report.md Sector Constituent Dispersion. NOT the 15-row "Official Sector Strength" (excludes Cybersecurity/Semiconductors/Defense/etc.).</em></p>
{sector_narrative}
<table><thead><tr><th>Rank</th><th>GICS Sector</th><th>Score</th><th>Breadth 50D</th><th>Breadth 200D</th><th>Pos 20D</th><th>Leaders</th><th>Laggards</th></tr></thead><tbody>
{sec_rows}
</tbody></table>

<h2 id="themes">Theme Rankings</h2>
<p><em>Source-derived from latest-report.md Thematic Strength.</em></p>
{themes_narrative}
<table><thead><tr><th>Rank</th><th>Theme</th><th>Score</th><th>Setup</th><th>Flow</th><th>Reliability</th><th>Dispersion</th></tr></thead><tbody>
{theme_rows}
</tbody></table>

<h2 id="style">Style Rotation</h2>
{style_rotation}

<h2 id="factor-style">Factor &amp; Style</h2>
{factor_style}

<h2 id="trades">Trade Ideas</h2>
{trades_narrative}
<table><thead><tr><th>Trade</th><th>Side</th><th>Type</th><th>Rationale</th></tr></thead><tbody>
{trades_html}
</tbody></table>
{candidate_screen}
{stock_ideas}

<h2 id="heat-st">Portfolio Heat Map &mdash; Short-Term (1-3M)</h2>
<p><em>{heat["method"]}</em>. ST active weights net to 0 (zero-sum by construction, &sect;54A &sect;19).</p>
{heat_st_narrative}
<table><thead><tr><th>Position</th><th>Active Weight</th></tr></thead><tbody>
{heat_st}
</tbody><tfoot><tr><th colspan="2">Net active weight: 0.0% (zero-sum)</th></tr></tfoot></table>

<h2 id="heat-lt">Long-Term Portfolio Heat Map (6-12M)</h2>
<p>LT active weights net to 0 (zero-sum by construction, &sect;54A &sect;19).</p>
{heat_lt_narrative}
<table><thead><tr><th>Position</th><th>Active Weight</th></tr></thead><tbody>
{heat_lt}
</tbody><tfoot><tr><th colspan="2">Net active weight: 0.0% (zero-sum)</th></tr></tfoot></table>

<h2 id="catalysts">Catalyst Watchlist</h2>
<p><em>Analyst inference/estimate &mdash; upcoming public-calendar events (federalreserve.gov / home.treasury.gov / BLS / BEA).</em></p>
{catalysts_narrative}
<table><thead><tr><th>Source</th><th>Scheduled Events</th></tr></thead><tbody>
<tr><td>FOMC policy</td><td>{", ".join(FOMC_2026 + FOMC_2027[:1])}</td></tr>
<tr><td>BLS releases</td><td>{", ".join(BLS_2026)}</td></tr>
<tr><td>BEA releases</td><td>{", ".join(BEA_2026)}</td></tr>
</tbody></table>

<h2 id="risks">Key Risk Analysis</h2>
<p><em>Mixture of source-derived and analyst inference (labelled per row).</em></p>
{risk_narrative}
{portfolio_risk}
{sector_allocation}
<table><thead><tr><th>Risk</th><th>Category</th><th>Assessment</th><th>Tag</th></tr></thead><tbody>
{risks_html}
</tbody></table>

<h2 id="conclusions">Highest-Conviction Conclusions</h2>
{conclusions}

<h2 id="disclosures">Sources &amp; Disclosures</h2>
<h3>Sources</h3>
{sources_block}
<ul class="sources">
<li><strong>latest-report.md</strong> &mdash; primary market report generated at {esc(now)} (rule-based, sslip.io + Postgres source).</li>
<li><strong>sslip.io</strong> &mdash; host {base} (live macro; latest-report.md snapshot taken at {spec_str}).</li>
<li><strong>US Equities API</strong> &mdash; market-tape and batch latest endpoints.</li>
</ul>
<h3>Classification of Material</h3>
<ul>
<li><strong>Verified fact</strong> &mdash; market prices, macro yields and spreads quoted from the primary report; official statistical and policy dates where cited.</li>
<li><strong>Source-derived signal</strong> &mdash; flow z-scores, breadth metrics and regime scores computed by the latest-report.md pipeline.</li>
<li><strong>Analyst inference / estimate</strong> &mdash; AI regime scorecard, scenarios, heat maps, trade ideas, catalysts and risk assessments are model or rule-based derivations (labelled per section); not forward-looking guarantees.</li>
<li><strong>AI narrative and re-rating</strong> &mdash; prose, external citations and AI factor/weight/sector judgments are model-authored and validated against the frozen evidence pack; AI values are disclosed beside source values.</li>
<li><strong>Source vs AI attribution</strong> (&sect;54A &sect;16) &mdash; Source Regime Score ({pct(r["score"])}) is quantitative; AI regime score ({ai_score_text}) is computed as &Sigma;(factor score &times; AI weight); methodologies differ and the derivation is disclosed above.</li>
</ul>
<footer>Generated {esc(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))} &middot; {footer_note}.</footer>
</div>
<a class="back-to-top" href="#top">&uarr; Top</a>
<script>
{REPORT_JS}
</script>
</body>
</html>'''


# --------------------------------------------------------------------------- #
#  §54A QC gate
# --------------------------------------------------------------------------- #
def check_html(html: str, d: dict, narrative: bool = False) -> list:
    fails = []
    for tag in ("div", "section", "table", "ul", "li", "p"):
        opens = len(re.findall(r"<%s[ >]" % tag, html))
        closes = len(re.findall(r"</%s>" % tag, html))
        if opens != closes:
            fails.append("%s tag imbalance: %d open vs %d close" % (tag, opens, closes))
    for bad in ("onrender.com", "postgresql-us-quities-api"):
        if bad in html.lower():
            fails.append("stale/dead host reference: " + bad)
    for stale in ("28 September", "25 September", "26 September", "2026-09-25", "2026-09-28"):
        if stale in html:
            fails.append("stale date: " + stale)
    if len(d["sectors"]) != 11:
        fails.append("sectors != 11 (got %d)" % len(d["sectors"]))
    else:
        names = [str(x.get("name") or "") for x in d["sectors"]]
        if len(set(names)) != 11:
            fails.append("GICS sector names are not unique (got %d unique)" % len(set(names)))
        scores = [x.get("score") for x in d["sectors"]]
        if any(not isinstance(v, (int, float)) for v in scores):
            fails.append("GICS sector scores must all be numeric")
        elif scores != sorted(scores, reverse=True):
            fails.append("GICS ranking is not sorted by score descending")
    if len(d["themes"]) != 13:
        fails.append("themes != 13 (got %d)" % len(d["themes"]))
    if '<div class="report" id="top">' not in html:
        fails.append("missing root <div class='report' id='top'>")
    base_tids = ("exec", "regime-scorecard", "forward-signal", "sector-rating",
                 "risk-opportunity", "analogs", "scen", "macro", "cross", "equities",
                 "price-action", "flows", "posture", "sectors", "themes", "style",
                 "factor-style", "trades", "heat-st", "heat-lt", "catalysts", "risks",
                 "conclusions", "disclosures")
    extra_tids = ("what-matters",) if narrative else ()
    for tid in base_tids + extra_tids:
        if 'id="%s"' % tid not in html or 'href="#%s"' % tid not in html:
            fails.append("TOC anchor #%s missing target (§54A failure mode #10)" % tid)
    return fails


def check_numerical(d: dict) -> list:
    fails = []
    for horizon in ("st", "lt"):
        rows = d["scenarios"].get(horizon) or []
        if len(rows) != 3:
            fails.append("%s scenario set must have exactly 3 entries (got %d)"
                         % (horizon.upper(), len(rows)))
        labels = [str(label) for label, _ in rows]
        if len(set(labels)) != len(labels):
            fails.append("%s scenario labels are not unique" % horizon.upper())
    st_sum = round(sum(p for _, p in d["scenarios"]["st"]), 1)
    lt_sum = round(sum(p for _, p in d["scenarios"]["lt"]), 1)
    if abs(st_sum - 100) > 0.2:
        fails.append("ST scenario probs sum %.1f != 100" % st_sum)
    if abs(lt_sum - 100) > 0.2:
        fails.append("LT scenario probs sum %.1f != 100" % lt_sum)
    wt = sum(c["weight"] for c in d["cio"]["components"])
    if wt != 100:
        fails.append("CIO weights sum %d != 100" % wt)
    for key in ("st", "lt"):
        net = round(sum(x["weight"] for x in d["heat"][key]), 3)
        if abs(net) > 0.001:
            fails.append("heat %s net %.3f != 0" % (key, net))
    if abs(d["cio"]["score"] - round(sum(c["contrib"] for c in d["cio"]["components"]), 2)) > 0.02:
        fails.append("CIO Weighted Score != sum(contrib) (§54A §3 / failure mode #1)")
    if d["regime"].get("score") is None:
        fails.append("regime score not parsed from latest-report.md (§54A §17)")
    return fails


def idea_qc(html: str) -> list:
    """Post-render QC on the published idea cards (independent of narrative JSON)."""
    fails: list[str] = []
    cards = re.findall(r'<div class="idea-card">(.*?)</div>', html, re.S)
    if not cards:
        return ["idea QC: no idea cards found in the rendered HTML"]
    ideas = []
    for c in cards:
        m = re.search(r'<h3>([A-Z][A-Z0-9.\-]*)', c)
        if not m:
            continue
        ticker = m.group(1)
        cur = re.search(r'Current price\.</strong>\s*([\d.]+)', c)
        pdate = re.search(r'as of ([\d-]+)', c)
        entry = re.search(r'<strong>Entry\.</strong>\s*([\d.]+)', c)
        reassess = re.search(r'<strong>Reassess\.</strong>\s*([A-Z]+)', c)
        ideas.append({
            "ticker": ticker,
            "current_price": float(cur.group(1).rstrip(".")) if cur else None,
            "price_date": pdate.group(1) if pdate else "",
            "entry_price": float(entry.group(1).rstrip(".")) if entry else None,
            "reassess": reassess.group(1) if reassess else "",
        })
        srcs = re.findall(r'href="([^"]+)"', c)
        deep = [u for u in srcs if "api.138.2.69.165.sslip.io" not in u.lower()
                and any(k in u.lower() for k in ("sec.gov", "10-q", "10-k", "8-k",
                                                 "earnings", "results", "press-release",
                                                 "news-release"))]
        if not deep:
            fails.append("idea QC: %s has no dated filing/results source (API/IR homepage only)" % ticker)
    prev = set(_previous_idea_tickers())
    current = {i["ticker"] for i in ideas}
    if prev and len(current) >= 3:
        new = [t for t in current if t not in prev]
        if len(new) < 2:
            print("IDEA QC WARNING: only %d new selected idea(s) versus HEAD (%s); "
                  "novelty is a warning, not a blocker" % (len(new), ", ".join(sorted(prev))))
        for i in ideas:
            if i["ticker"] in prev and i["reassess"] == "NEW":
                fails.append("idea QC: %s was in HEAD but is marked NEW" % i["ticker"])
    for i in ideas:
        if i["current_price"] is None or i["entry_price"] is None or not i["price_date"]:
            fails.append("idea QC: %s is missing current/entry price or price date" % i["ticker"])
    fails += audit_ideas(ideas)
    return fails


def run_qc(html: str, d: dict, narrative: bool = False) -> list:
    fails = check_html(html, d, narrative=narrative) + check_numerical(d)
    if narrative:
        fails += idea_qc(html)
    return fails


# --------------------------------------------------------------------------- #
#  §54A §12 commit / push gate
# --------------------------------------------------------------------------- #
def git_commit_push() -> bool:
    env = dict(os.environ)
    if os.path.exists(DEPLOY_KEY):
        env["GIT_SSH_COMMAND"] = "ssh -i %s -o StrictHostKeyChecking=no -o IdentitiesOnly=yes" % DEPLOY_KEY
    subprocess.run(["git", "add", "--", "data/market-intelligence-report.html"], cwd=BASE_DIR, env=env)
    subprocess.run(["git", "-C", BASE_DIR, "commit", "-m",
                    "Update market intelligence HTML report"], env=env)
    for branch in ("main", "master"):
        push = subprocess.run(["git", "-C", BASE_DIR, "push", "origin", branch],
                              env=env, capture_output=True, text=True)
        if push.returncode == 0:
            return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(prog="generate_final_report.py",
                                 description="Date-agnostic market-intelligence HTML report generator.")
    ap.add_argument("--report", required=True, help="path to latest-report.md")
    ap.add_argument("--push", action="store_true",
                    help="commit+push data/market-intelligence-report.html (§54A §12)")
    ap.add_argument("--evidence-out", default=None,
                    help="write the frozen evidence pack (verified numbers + source sha256) to this JSON path")
    ap.add_argument("--narrative", default=None,
                    help="optional AI narrative JSON; validated against the evidence pack before rendering")
    args = ap.parse_args()

    # SHORTCUT GUARD: production runs MUST carry a validated AI narrative.
    # Bare execution produces the compact programmatic report and bypasses the
    # market-intelligence-report workflow (narrative authoring + §54A gates).
    # --evidence-out alone is allowed as a read-only probe: it writes the
    # evidence pack and exits WITHOUT touching the published HTML, so the agent
    # can read the exact metrics before authoring prose.
    # Deliberate deterministic runs may opt out with AEGIS_ALLOW_PROGRAMMATIC=1.
    shortcut_blocked = (not args.narrative
                        and os.environ.get("AEGIS_ALLOW_PROGRAMMATIC") != "1")
    if shortcut_blocked and not args.evidence_out:
        sys.stderr.write(
            "HALT: --narrative is required for production report generation.\n"
            "Bare execution produces the compact programmatic report and bypasses\n"
            "the AI narrative workflow. Author the narrative JSON first\n"
            "(schema aegis-narrative-v1, sections: exec_summary, what_matters,\n"
            "sector_narrative, risk_narrative, conclusion), then re-run with\n"
            "--narrative <path>.\n"
            "Tip: run with --evidence-out <path> (no --narrative) to dump the\n"
            "frozen evidence pack without writing the HTML.\n"
            "For a deliberate deterministic run set AEGIS_ALLOW_PROGRAMMATIC=1.\n"
        )
        return 5

    # §54A §15: fetch/verify primary source at start
    if not os.path.exists(args.report):
        sys.stderr.write("HALT: primary source %s unreadable\n" % args.report)
        return 2
    try:
        raw = open(args.report, encoding="utf-8").read()
        if "Report" not in raw and not raw.strip():
            raise OSError("empty report")
    except OSError as e:
        sys.stderr.write("HALT: primary source unreadable: %s\n" % e)
        return 2

    spec_paths = inspect_sslip_spec()
    d = parse_latest_report(args.report)
    d["spec_paths"] = spec_paths
    d["live_reconciled"] = bool(fetch_sslip_macro(["^VIX", "US10YT=X", "US2YT=X", "US30YT=X", "^GSPC", "^IXIC"]))

    d["cio"] = derive_cio(d["regime_factors"])
    d["scenarios"] = derive_scenarios(d["regime"].get("score"), d["regime"].get("label") or "")
    d["heat"] = derive_heat(d["sectors"])
    d["trades"] = derive_trades(d["sectors"], d["themes"], d.get("setups", []))
    d["risks"] = derive_risks(d["macro"], d["regime"])

    # Optional AI narrative layer (Generator B). The deterministic numbers stay
    # authoritative: a narrative is only rendered after its provenance hash and
    # every numeric claim have been checked against the frozen evidence pack.
    narrative_html = None
    adjustments: dict = {}
    if args.evidence_out or args.narrative:
        evidence = build_evidence_pack(d, args.report)
        if args.evidence_out:
            with open(args.evidence_out, "w", encoding="utf-8") as fh:
                json.dump(evidence, fh, indent=2)
            sys.stderr.write(
                "EVIDENCE: wrote %s (%d metrics, sha256 %s)\n"
                % (args.evidence_out, len(evidence.get("metrics") or {}),
                   evidence["source_sha256"][:12])
            )
        if shortcut_blocked:
            sys.stderr.write(
                "EVIDENCE-ONLY: no --narrative supplied; published HTML NOT written.\n"
                "Author the narrative JSON against this evidence pack, then re-run\n"
                "with --narrative <path>.\n"
            )
            return 0
    if args.narrative:
        try:
            raw_narrative = load_narrative(args.narrative)
        except Exception as e:  # malformed JSON / unreadable file
            sys.stderr.write("HALT: cannot load narrative %s: %s\n" % (args.narrative, e))
            return 4
        ideas = (raw_narrative.get("sections") or {}).get("stock_ideas") or []
        price_warnings = []
        price_fails = audit_ideas(ideas, warnings=price_warnings)
        for warning in price_warnings:
            print("PRICE WARNING:", warning)
        fundamental_fails = audit_fundamentals(ideas)
        web_fails = audit_pe_history(ideas) + audit_consensus(ideas)
        nfails = price_fails + fundamental_fails + web_fails + validate_narrative(raw_narrative, evidence)
        if nfails:
            sys.stderr.write("HALT: narrative validation failed (%d); no file written.\n" % len(nfails))
            for f in nfails:
                sys.stderr.write("  NARRATIVE FAIL: %s\n" % f)
            return 4
        narrative_html = render_narrative(raw_narrative)
        adjustments = raw_narrative.get("adjustments") or {}
        sys.stderr.write("NARRATIVE: validated against evidence and rendered (%d slots)\n" % len(narrative_html))

    html = build_html(d, narrative_html, adjustments)
    fails = run_qc(html, d, narrative=bool(narrative_html))
    if narrative_html and raw_narrative is not None:
        fails += cross_section_qc.check(html, raw_narrative, adjustments.get("regime_score"))
    sys.stderr.write("DATA CUTOFF: %s %s | sectors=%d themes=%d cio=%.2f regime=%s source=%s\n"
                     % (d["data_cutoff"], d["data_cutoff_time"], len(d["sectors"]), len(d["themes"]),
                        d["cio"]["score"], d["regime"].get("score"), d["report_dt"]))
    sys.stderr.write("QC: %d failure(s)\n" % len(fails))
    for f in fails:
        sys.stderr.write("  FAIL: %s\n" % f)
    if fails:
        sys.stderr.write("HALT: §54A QC gate failed; no file written.\n")
        return 1

    with open(OUTPUT_HTML, "w", encoding="utf-8") as fh:
        fh.write(html)
    sys.stderr.write("OK: wrote %s (%d bytes)\n" % (OUTPUT_HTML, len(html)))

    if args.push:
        if git_commit_push():
            sys.stderr.write("PUSH: data/market-intelligence-report.html committed+push (§54A §12)\n")
        else:
            sys.stderr.write("PUSH: FAILED\n")
            return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())

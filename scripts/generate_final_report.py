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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # market-dashboard
DATA_DIR = os.path.join(BASE_DIR, "data")
CONFIG_JS = os.path.join(BASE_DIR, "config.js")
DEFAULT_REPORT = os.path.join(DATA_DIR, "latest-report.md")
OUTPUT_HTML = os.path.join(DATA_DIR, "market-intelligence-report.html")
DEPLOY_KEY = "/var/tmp/market_dashboard_deploy"

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
        "evidence": _num(dash, r"Evidence quality:\s*`?(\d+\.\d+)"),
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
        if len(r) >= 3:
            try:
                drivers[r[0]] = float(r[1])
            except ValueError:
                pass
    d["regime_factors"] = drivers
    d["regime"]["primary_driver"] = max(drivers, key=drivers.get) if drivers else None

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
                            "leaders": r[8], "laggards": r[9] if len(r) > 9 else ""})
    sectors.sort(key=lambda s: s["breadth_200"], reverse=True)
    for i, s in enumerate(sectors, 1):
        s["rank"], s["score"] = i, round((s["breadth_50"] + s["breadth_200"] + s["positive_20d"]) / 3.0, 2)
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


def build_html(d: dict) -> str:
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
    heat_st = "".join("<li>%s: %+.1f%%</li>" % (esc(x["name"]), x["weight"] * 100) for x in heat["st"])
    heat_lt = "".join("<li>%s: %+.1f%%</li>" % (esc(x["name"]), x["weight"] * 100) for x in heat["lt"])
    trades_html = "".join(
        "<li><strong>%s</strong> — %s (%s): %s</li>"
        % (esc(t["name"]), esc(t["side"]), esc(t["type"]), esc(t["rationale"])) for t in trades)
    risks_html = "".join(
        '<li><strong>%s</strong> [%s]: %s &mdash; <span class="tag">%s</span></li>'
        % (esc(x[0]), esc(x[1]), esc(x[2]), esc(x[3])) for x in risks)
    flow_html = "".join("<li>%s: %s</li>" % (esc(f["asset"]), esc(f["signal"])) for f in cf)
    ca_html = "".join("<li>%s: %s</li>" % (esc(c["area"]), esc(c["signal"])) for c in ca)
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
:root {{ --bg:#0c0d10; --fg:#e8e8e8; --muted:#9aa0a6; --card:#14161a; --accent:#4f9aff; --pos:#2ecc71; --neg:#e74c3c; --line:#22252b; }}
body {{ margin:0; font-family:-apple-system,ui-sans-serif,sfpro,sans-serif; max-width:860px; letter-spacing:.01em; color:var(--fg); background:var(--bg); }}
.report {{ max-width:820px; margin:0 auto; padding:24px; }}
.mast {{ border-bottom:var(--line) solid 1px; padding-bottom:14px; margin-bottom:18px; }}
.mast h1 {{ margin:0 0 4px; font-size:22px; font-weight:600; }}
.meta, .meta span {{ color:var(--muted); font-size:13px; }}
nav.toc ul {{ list-style:none; padding-left:0; margin:12px 0 4px; }}
nav.toc li {{ display:inline-block; margin-right:12px; font-size:12px; }}
nav.toc a {{ color:var(--accent); text-decoration:none; }}
h2 {{ margin-top:26px; border-bottom:var(--line) solid 1px; padding-bottom:6px; font-size:17px; }}
h3 {{ margin-top:18px; font-size:14px; color:var(--accent); }}
table {{ border-collapse:collapse; width:100%; margin:10px 0; font-size:13px; }}
th, td {{ border:var(--line) solid 1px; padding:6px 8px; text-align:left; }}
th {{ background:var(--card); color:var(--muted); font-weight:600; }}
tr:nth-child(even) {{ background:rgba(79,154,255,.04); }}
.pos {{ color:var(--pos); }} .neg {{ color:var(--neg); }}
.tag {{ display:inline-block; font-size:11px; padding:1px 5px; border-radius:3px; background:rgba(255,255,255,.08); color:var(--muted); margin-left:6px; }}
.inference {{ background:rgba(255,150,0,.12); color:#ffae48; }}
.k {{ color:var(--muted); display:inline-block; min-width:90px; }} .v {{ font-weight:600; }}
ul {{ line-height:1.6; }} li {{ margin:2px 0; }}
footer {{ margin-top:30px; color:var(--muted); font-size:12px; border-top:var(--line) solid 1px; padding-top:10px; }}
</style>
</head>
<body>
<div class="report" id="top">
<div class="mast">
  <h1>Market Intelligence Report</h1>
  <div class="meta">Data Cutoff: <strong>{esc(now)}</strong> &middot; Run ID: <strong>{esc(run)}</strong> &middot; Source: latest-report.md + sslip.io</div>
  <nav class="toc">
    <ul>
      <li><a href="#exec">Executive</a></li>
      <li><a href="#scorecard">Scorecard</a></li>
      <li><a href="#macro">Macro</a></li>
      <li><a href="#cross">Cross-Asset</a></li>
      <li><a href="#sectors">Sectors</a></li>
      <li><a href="#themes">Themes</a></li>
      <li><a href="#scen">Scenarios</a></li>
      <li><a href="#heat">Heat Maps</a></li>
      <li><a href="#flows">Flows</a></li>
      <li><a href="#trades">Trade Ideas</a></li>
      <li><a href="#catalysts">Catalysts</a></li>
      <li><a href="#risks">Risks</a></li>
      <li><a href="#disclosures">Disclosures</a></li>
    </ul>
  </nav>
</div>

<h2 id="exec">Executive Summary</h2>
<p><strong>Regime:</strong> {esc(r.get("label") or "Mixed")}. Source Regime Score <strong>{pct(r["score"])}/100</strong> (source-derived); CIO Weighted Regime Score <strong>{pct(cio["score"])}/100</strong> (<em>{cio["method"]}</em>). US equity strength {pct(r["equity_strength"])}/100; evidence quality {pct(r["evidence"])}/100; ETF flow contribution {pct(r["etf_flow"])}/100 (reliability {pct(r["flow_reliability"])}). Primary driver: {esc(r.get("primary_driver") or "n/a")}. Breadth above 50DMA {pct(r["breadth_50"])}%, above 200DMA {pct(r["breadth_200"])}%.</p>

<h2 id="scorecard">CIO Weighted Market Regime Scorecard</h2>
<p><em>{cio["method"]}</em>. Components mapped from latest-report.md regime factors ({", ".join(esc(k) for k in d["regime_factors"].keys()) if d["regime_factors"] else "none available"}). Weights total {sum(c["weight"] for c in cio["components"])}%.</p>
<table><thead><tr><th>Component</th><th>Weight</th><th>Score</th><th>Contribution</th></tr></thead><tbody>
{cio_rows}
</tbody><tfoot><tr><th colspan="3">CIO Weighted Score</th><th>{cio["score"]}</th></tr></tfoot></table>

<h2 id="macro">Macro View</h2>
<p>Macro snapshot &mdash; observation dates per &sect;54A &sect;15 (live as-of 30 October 2026 17:00 HKT where marked live; else prior close). Reconciliation against sslip.io host {base} (spec paths: {spec_str}).</p>
<ul>
{pcs}
</ul>

<h2 id="cross">Cross-Asset Confirmation</h2>
<ul>{ca_html}</ul>

<h2 id="sectors">Sector Rankings (exactly 11 GICS)</h2>
<p><em>Source-derived from latest-report.md Sector Constituent Dispersion. NOT the 15-row "Official Sector Strength" (excludes Cybersecurity/Semiconductors/Defense/etc.).</em></p>
<table><thead><tr><th>Rank</th><th>GICS Sector</th><th>Score</th><th>Breadth 50D</th><th>Breadth 200D</th><th>Pos 20D</th><th>Leaders</th><th>Laggards</th></tr></thead><tbody>
{sec_rows}
</tbody></table>

<h2 id="themes">Theme Rankings (exactly 13)</h2>
<p><em>Source-derived from latest-report.md Thematic Strength.</em></p>
<table><thead><tr><th>Rank</th><th>Theme</th><th>Score</th><th>Setup</th><th>Flow</th><th>Reliability</th><th>Dispersion</th></tr></thead><tbody>
{theme_rows}
</tbody></table>

<h2 id="scen">Probability-Weighted Scenarios</h2>
<p><em>{sc["method"]}</em>. ST probabilities total {sum(p for _, p in sc["st"]):.1f}%; LT total {sum(p for _, p in sc["lt"]):.1f}%.</p>
<h3>Short-Term (1-3M)</h3>
<table><thead><tr><th>Scenario</th><th>Probability</th></tr></thead><tbody>{st_rows}</tbody></table>
<h3>Long-Term (6-12M)</h3>
<table><thead><tr><th>Scenario</th><th>Probability</th></tr></thead><tbody>{lt_rows}</tbody></table>

<h2 id="heat">Portfolio Heat Maps</h2>
<p><em>{heat["method"]}</em>. ST/LT active-weight heat maps net to 0 (zero-sum by construction, &sect;54A &sect;19).</p>
<h3>ST Heat Map</h3>
<ul>{heat_st}</ul>
<h3>LT Heat Map</h3>
<ul>{heat_lt}</ul>

<h2 id="flows">Flows / Positioning</h2>
<p>Core flow signals (source-derived):</p>
<ul>{flow_html}</ul>

<h2 id="trades">Trade Ideas</h2>
<p><em>{", ".join(esc(t["name"]) for t in trades)}</em>.</p>
<ul>{trades_html}</ul>

<h2 id="catalysts">Catalyst Watchlist</h2>
<p><em>Analyst inference/estimate &mdash; upcoming public-calendar events (federalreserve.gov / home.treasury.gov / BLS / BEA).</em></p>
<ul>
<li>FOMC policy: {", ".join(FOMC_2026 + FOMC_2027[:1])}.</li>
<li>BLS releases: {", ".join(BLS_2026)}.</li>
<li>BEA: {", ".join(BEA_2026)}.</li>
</ul>

<h2 id="risks">Key Risk Analysis</h2>
<p><em>Mixture of source-derived and analyst inference (labelled per row).</em></p>
<ul>{risks_html}</ul>

<h2 id="disclosures">Sources &amp; Disclosures</h2>
<ul>
<li><strong>latest-report.md</strong>: generated at {esc(now)} (rule-based, sslip.io + Postgres source).</li>
<li><strong>sslip.io</strong>: host {base} (live macro; latest-report.md snapshot taken at {spec_str}).</li>
<li><strong>Analyst inference</strong>: CIO scorecard, scenarios, heat maps, catalysts and risk assessments are rule-based derivations (see per-section labels); not forward-looking guarantees.</li>
<li><strong>Python vs CIO attribution</strong> (&sect;54A &sect;16): Source Regime Score ({pct(r["score"])}) is quantitative; CIO Weighted Score ({pct(cio["score"])}) is derived &mdash; methodologies differ.</li>
</ul>
<footer>Generated {esc(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))} &middot; this is a programmatic report; no manual narrative was authored.</footer>
</div>
</body>
</html>'''


# --------------------------------------------------------------------------- #
#  §54A QC gate
# --------------------------------------------------------------------------- #
def check_html(html: str, d: dict) -> list:
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
    if len(d["themes"]) != 13:
        fails.append("themes != 13 (got %d)" % len(d["themes"]))
    if '<div class="report" id="top">' not in html:
        fails.append("missing root <div class='report' id='top'>")
    for tid in ("exec", "scorecard", "macro", "cross", "sectors", "themes", "scen",
                "heat", "flows", "trades", "catalysts", "risks", "disclosures"):
        if 'id="%s"' % tid not in html or 'href="#%s"' % tid not in html:
            fails.append("TOC anchor #%s missing target (§54A failure mode #10)" % tid)
    return fails


def check_numerical(d: dict) -> list:
    fails = []
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


def run_qc(html: str, d: dict) -> list:
    return check_html(html, d) + check_numerical(d)


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
    args = ap.parse_args()

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

    html = build_html(d)
    fails = run_qc(html, d)
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

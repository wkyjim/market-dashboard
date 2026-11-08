"""Scrape public fundamentals for valuation history.

Sources (verified reachable):
  - companiesmarketcap.com: annual EPS, P/E, revenue, operating margin, P/S, P/B
  - Google Finance earnings tab: consensus estimates (best effort)
  - Investing.com: currently returns 403 to plain HTTP clients; not used.

The scraper is deterministic and cached. It is used to verify the report's
historical P/E statistics instead of trusting model-authored percentiles.
"""
from __future__ import annotations

import http.cookiejar
import json
import os
import re
import time
import urllib.parse
import urllib.request
from statistics import median

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124 Safari/537.36")
BASE = "https://companiesmarketcap.com"
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                         "data", "fundamentals_cache")

SLUGS = {
    "AAPL": "apple", "MSFT": "microsoft", "NVDA": "nvidia", "AMD": "amd",
    "GOOGL": "alphabet-google", "GOOG": "alphabet-google", "AMZN": "amazon",
    "META": "meta-platforms", "TSLA": "tesla", "AVGO": "broadcom",
    "REGN": "regeneron-pharmaceuticals", "LLY": "eli-lilly", "UNH": "unitedhealth",
    "JNJ": "johnson-johnson", "MRK": "merck", "PFE": "pfizer", "ABBV": "abbvie",
    "COP": "conocophillips", "XOM": "exxon-mobil", "CVX": "chevron",
    "EOG": "eog-resources", "APA": "apa-corp", "SLB": "schlumberger",
    "WMT": "walmart", "COST": "costco", "PG": "procter-gamble", "KO": "coca-cola",
    "HD": "home-depot", "LOW": "lowes", "MCD": "mcdonalds", "NKE": "nike",
    "JPM": "jpmorgan-chase", "BAC": "bank-of-america", "GS": "goldman-sachs",
    "LMT": "lockheed-martin", "RTX": "raytheon-technologies", "NOC": "northrop-grumman",
    "BA": "boeing", "CAT": "caterpillar", "DE": "deere",
    "XLE": "energy-select-sector-spdr-fund", "XLK": "technology-select-sector-spdr-fund",
}


def _num(text: str) -> float | None:
    raw = re.sub(r"[^\d.\-]", "", text.replace(",", ""))
    if not raw or raw in ("-", "."):
        return None
    try:
        value = float(raw)
    except ValueError:
        return None
    low = text.lower()
    if " t" in low:
        value *= 1e12
    elif " b" in low:
        value *= 1e9
    elif " m" in low:
        value *= 1e6
    return value


def _fetch(url: str, timeout: float = 20.0) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", "ignore")


def _series(html: str) -> list[tuple[int, float]]:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        return []
    out = []
    for row in table.find_all("tr")[1:]:
        cells = [c.get_text(" ", strip=True) for c in row.find_all(["td", "th"])]
        if len(cells) < 2:
            continue
        m = re.search(r"(\d{4})", cells[0])
        val = _num(cells[1])
        if m and val is not None:
            out.append((int(m.group(1)), val))
    return sorted(out)


def _cached(ticker: str, key: str, url: str, refresh: bool = False):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, f"{ticker}_{key}.json")
    if not refresh and os.path.exists(path):
        age = time.time() - os.path.getmtime(path)
        if age < 86400:
            try:
                with open(path, encoding="utf-8") as fh:
                    return json.load(fh)
            except Exception:
                pass
    html = _fetch(url)
    data = _series(html)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"url": url, "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "series": data}, fh)
    return {"url": url, "series": data}


YAHOO = "https://finance.yahoo.com/quote/%s/analysis/"


def _parse_num(text: str) -> float | None:
    text = str(text or "").strip().replace(",", "")
    if text in ("", "--", "N/A"):
        return None
    mult = 1.0
    if text.endswith("B"):
        mult, text = 1e9, text[:-1]
    elif text.endswith("M"):
        mult, text = 1e6, text[:-1]
    elif text.endswith("T"):
        mult, text = 1e12, text[:-1]
    try:
        return float(text) * mult
    except ValueError:
        return None


_YAHOO_OPENER = None
_YAHOO_CRUMB = None


def _yahoo_api(ticker: str) -> dict | None:
    """Yahoo quoteSummary fallback (the HTML analysis table is empty for some tickers)."""
    global _YAHOO_OPENER, _YAHOO_CRUMB
    if _YAHOO_OPENER is None:
        cj = http.cookiejar.CookieJar()
        _YAHOO_OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        _YAHOO_OPENER.addheaders = [("User-Agent", UA), ("Accept-Language", "en-US,en;q=0.9")]
        try:
            _YAHOO_OPENER.open("https://fc.yahoo.com", timeout=15).read()
        except Exception:
            pass
        try:
            _YAHOO_CRUMB = _YAHOO_OPENER.open(
                "https://query1.finance.yahoo.com/v1/test/getcrumb", timeout=20).read().decode()
        except Exception:
            _YAHOO_CRUMB = ""
    if not _YAHOO_CRUMB:
        return None
    url = ("https://query1.finance.yahoo.com/v10/finance/quoteSummary/%s"
           "?modules=earningsTrend&crumb=%s" % (ticker.upper(), urllib.parse.quote(_YAHOO_CRUMB)))
    try:
        payload = json.loads(_YAHOO_OPENER.open(url, timeout=25).read().decode())
        trend = payload["quoteSummary"]["result"][0]["earningsTrend"]["trend"]
    except Exception:
        return None
    eps_by_year, rev_by_year = {}, {}
    current_qtr = next_qtr = current_year = next_year = None
    for item in trend:
        period = item.get("period")
        end = str(item.get("endDate") or "")
        year = int(end[:4]) if end[:4].isdigit() else None
        eps = ((item.get("earningsEstimate") or {}).get("avg") or {}).get("raw")
        rev = ((item.get("revenueEstimate") or {}).get("avg") or {}).get("raw")
        if period == "0q":
            current_qtr = eps
        elif period == "+1q":
            next_qtr = eps
        elif period == "0y":
            current_year = eps
        elif period == "+1y":
            next_year = eps
        if year and eps is not None:
            eps_by_year[year] = eps
        if year and rev is not None:
            rev_by_year[year] = rev
    return {
        "source": "https://finance.yahoo.com/quote/%s/analysis/" % ticker.upper(),
        "headers": [],
        "eps_current_qtr": current_qtr,
        "eps_next_qtr": next_qtr,
        "eps_current_year": current_year,
        "eps_next_year": next_year,
        "revenue_current_year": current_year and next(iter(rev_by_year.values()), None),
        "revenue_next_year": None,
        "eps_by_year": eps_by_year,
        "revenue_by_year": rev_by_year,
    }


def fetch_yahoo(ticker: str, timeout: float = 25.0) -> dict | None:
    """Consensus EPS/revenue from Yahoo Finance analysis (current and next year)."""
    from bs4 import BeautifulSoup
    url = YAHOO % ticker.upper()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept-Language": "en-US,en;q=0.9"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            html = response.read().decode("utf-8", "ignore")
    except Exception:
        return None
    soup = BeautifulSoup(html, "html.parser")
    blocks = []
    for table in soup.find_all("table"):
        rows = [[c.get_text(" ", strip=True) for c in r.find_all(["td", "th"])]
                for r in table.find_all("tr")]
        if rows and any("Current Qtr" in c for c in rows[0]) and any("Next Year" in c for c in rows[0]):
            blocks.append(rows)
    if len(blocks) < 2:
        return _yahoo_api(ticker)
    rev, eps = blocks[0], blocks[1]
    def row(rows, label):
        for r in rows[1:]:
            if r and r[0].strip().lower().startswith(label):
                return r[1:]
        return ["--", "--", "--", "--"]
    rev_vals = row(rev, "avg. estimate")
    eps_vals = row(eps, "avg. estimate")
    years = []
    for header in rev[0][1:]:
        m = re.search(r"(20\d{2})", header)
        years.append(int(m.group(1)) if m else None)
    eps_by_year = {}
    rev_by_year = {}
    for idx, year in enumerate(years):
        if year and idx < len(eps_vals):
            eps_by_year[year] = _parse_num(eps_vals[idx])
        if year and idx < len(rev_vals):
            rev_by_year[year] = _parse_num(rev_vals[idx])
    return {
        "source": url,
        "headers": rev[0][1:],
        "eps_current_qtr": _parse_num(eps_vals[0]) if len(eps_vals) > 0 else None,
        "eps_next_qtr": _parse_num(eps_vals[1]) if len(eps_vals) > 1 else None,
        "eps_current_year": _parse_num(eps_vals[2]) if len(eps_vals) > 2 else None,
        "eps_next_year": _parse_num(eps_vals[3]) if len(eps_vals) > 3 else None,
        "revenue_current_year": _parse_num(rev_vals[2]) if len(rev_vals) > 2 else None,
        "revenue_next_year": _parse_num(rev_vals[3]) if len(rev_vals) > 3 else None,
        "eps_by_year": eps_by_year,
        "revenue_by_year": rev_by_year,
    }


def audit_consensus(ideas, lookup=fetch_yahoo, tolerance_pct: float = 5.0) -> list[str]:
    """Block CONSENSUS-labelled forward figures that disagree with Yahoo Finance."""
    fails: list[str] = []
    for i, idea in enumerate(ideas or []):
        if not isinstance(idea, dict):
            continue
        ticker = str(idea.get("ticker") or "").strip().upper()
        prov = idea.get("valuation_provenance") or {}
        if not isinstance(prov, dict):
            continue
        wants = any(str(prov.get(k, "")) == "CONSENSUS"
                    for k in ("fy2027_eps_consensus", "fy2028_eps_consensus"))
        if not wants:
            continue
        data = lookup(ticker)
        if not data:
            fails.append("stock_ideas[%d] %s: Yahoo consensus unavailable" % (i, ticker))
            continue
        for key, field in (("fy2027_eps_consensus", "eps_current_year"),
                           ("fy2028_eps_consensus", "eps_next_year")):
            claim = idea.get(key)
            by_year = data.get("eps_by_year") or {}
            actual = by_year.get(int(key[2:6])) if by_year else data.get(field)
            if isinstance(claim, (int, float)) and actual:
                if abs(float(claim) - actual) > max(0.05, abs(actual) * tolerance_pct / 100.0):
                    fails.append("stock_ideas[%d] %s: %s %.2f != Yahoo %.2f"
                                 % (i, ticker, key, float(claim), actual))
        source = str(idea.get("consensus_source") or "")
        if "finance.yahoo.com" not in source:
            fails.append("stock_ideas[%d] %s: consensus_source must cite finance.yahoo.com"
                         % (i, ticker))
    return fails


def fetch_ticker(ticker: str, refresh: bool = False) -> dict | None:
    ticker = str(ticker or "").strip().upper()
    slug = SLUGS.get(ticker, ticker.lower())
    out = {}
    for key in ("eps", "pe-ratio", "revenue", "operating-margin", "ps-ratio", "pb-ratio"):
        try:
            out[key] = _cached(ticker, key, f"{BASE}/{slug}/{key}/", refresh)
        except Exception:
            out[key] = {"url": f"{BASE}/{slug}/{key}/", "series": []}
    # Negative P/E is not meaningful; use the last five positive annual values.
    pe_pairs = [(y, v) for y, v in out["pe-ratio"]["series"] if v > 0]
    last5 = pe_pairs[-5:]
    stats = None
    if len(last5) >= 3:
        vals = [v for _, v in last5]
        current = vals[-1]
        ordered = sorted(vals)
        below = sum(1 for v in ordered if v <= current)
        stats = {
            "median": round(median(vals), 2),
            "min": round(min(vals), 2),
            "max": round(max(vals), 2),
            "percentile": round(100.0 * below / len(vals), 1),
            "years": len(vals),
            "current": current,
        }
    eps = out["eps"]["series"]
    eps_growth = None
    if eps:
        latest_year, latest_eps = eps[-1]
        base = dict(eps).get(latest_year - 3)
        if base and base > 0 and latest_eps > 0:
            eps_growth = round((latest_eps / base - 1.0) * 100.0, 2)
    return {
        "ticker": ticker,
        "slug": slug,
        "sources": {k: v["url"] for k, v in out.items()},
        "eps_history": eps,
        "pe_history": out["pe-ratio"]["series"],
        "pe_stats": stats,
        "eps_growth_3y_pct": eps_growth,
        "revenue_history": out["revenue"]["series"],
        "operating_margin_history": out["operating-margin"]["series"],
        "ps_history": out["ps-ratio"]["series"],
        "pb_history": out["pb-ratio"]["series"],
        "yahoo": fetch_yahoo(ticker),
        "latest": {
            "revenue": (out["revenue"]["series"] or [(None, None)])[-1][1],
            "operating_margin_pct": (out["operating-margin"]["series"] or [(None, None)])[-1][1],
            "ps": (out["ps-ratio"]["series"] or [(None, None)])[-1][1],
            "pb": (out["pb-ratio"]["series"] or [(None, None)])[-1][1],
        },
    }


def fetch_pe_stats(ticker: str) -> dict | None:
    data = fetch_ticker(ticker)
    return (data or {}).get("pe_stats")


def audit_pe_history(ideas, lookup=fetch_pe_stats) -> list[str]:
    """Block P/E history values that do not match companiesmarketcap."""
    fails: list[str] = []
    for i, idea in enumerate(ideas or []):
        if not isinstance(idea, dict):
            continue
        ticker = str(idea.get("ticker") or "").strip().upper()
        claimed = idea.get("pe_5y_median")
        if not isinstance(claimed, (int, float)):
            continue
        stats = lookup(ticker)
        if not stats:
            fails.append("stock_ideas[%d] %s: companiesmarketcap P/E history unavailable" % (i, ticker))
            continue
        if abs(float(claimed) - stats["median"]) > max(1.0, stats["median"] * 0.10):
            fails.append("stock_ideas[%d] %s: pe_5y_median %.2f != CMC median %.2f"
                         % (i, ticker, float(claimed), stats["median"]))
        for key in ("min", "max"):
            claim = idea.get(f"pe_5y_{key}")
            if isinstance(claim, (int, float)) and abs(float(claim) - stats[key]) > max(1.0, stats[key] * 0.15):
                fails.append("stock_ideas[%d] %s: pe_5y_%s %.2f != CMC %.2f"
                             % (i, ticker, key, float(claim), stats[key]))
        claim_pct = idea.get("pe_5y_percentile")
        if isinstance(claim_pct, (int, float)) and abs(float(claim_pct) - stats["percentile"]) > 20:
            fails.append("stock_ideas[%d] %s: pe_5y_percentile %.1f != CMC %.1f"
                         % (i, ticker, float(claim_pct), stats["percentile"]))
        source = str(idea.get("pe_history_source") or "")
        if "companiesmarketcap.com" not in source:
            fails.append("stock_ideas[%d] %s: pe_history_source must cite companiesmarketcap.com"
                         % (i, ticker))
    return fails


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    print(json.dumps(fetch_ticker(args.ticker, args.refresh), indent=2, ensure_ascii=False))

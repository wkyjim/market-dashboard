"""Scrape public fundamentals for valuation history.

Sources (verified reachable):
  - companiesmarketcap.com: annual EPS, P/E, revenue, operating margin, P/S, P/B
  - Google Finance earnings tab: consensus estimates (best effort)
  - Investing.com: currently returns 403 to plain HTTP clients; not used.

The scraper is deterministic and cached. It is used to verify the report's
historical P/E statistics instead of trusting model-authored percentiles.
"""
from __future__ import annotations

import json
import os
import re
import time
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

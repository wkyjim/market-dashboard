"""Yahoo Finance calendar scrapers: economic events, earnings, splits, IPOs.

Yahoo serves these pages compressed (gzip/brotli); urllib does not decode them
reliably, so we shell out to curl --compressed. The pages are server-rendered
tables with a date-group row followed by event rows.
"""
from __future__ import annotations

import re
import subprocess
from datetime import date, datetime, timedelta

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124 Safari/537.36")
BASE = "https://finance.yahoo.com/calendar"
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def _fetch(url: str, timeout: int = 30) -> str:
    out = subprocess.run(
        ["curl", "-sL", "--compressed", "-A", UA, "-H", "Accept-Language: en-US,en;q=0.9",
         "--max-time", str(timeout), url],
        capture_output=True, text=True, encoding="utf-8", errors="ignore", timeout=timeout + 5,
    )
    return out.stdout or ""


def _tables(html: str):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("table")


def parse_table(html: str) -> list[dict]:
    """First table -> list of dicts keyed by lower_snake headers."""
    tables = _tables(html)
    if not tables:
        return []
    rows = tables[0].find_all("tr")
    if not rows:
        return []
    headers = [c.get_text(" ", strip=True) for c in rows[0].find_all(["th", "td"])]
    keys = [re.sub(r"[^a-z0-9]+", "_", h.lower()).strip("_") for h in headers]
    out = []
    for row in rows[1:]:
        cells = [c.get_text(" ", strip=True) for c in row.find_all(["th", "td"])]
        if not cells:
            continue
        if len(cells) == 1 and _looks_like_date(cells[0]):
            continue  # date group header
        if len(cells) < len(keys):
            cells += [""] * (len(keys) - len(cells))
        out.append(dict(zip(keys, cells[:len(keys)])))
    return out


def _looks_like_date(text: str) -> bool:
    return bool(re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}", text))


def _parse_date(text: str):
    m = re.search(r"([A-Z][a-z]{2})[a-z]*\s+(\d{1,2}),?\s+(\d{4})", text or "")
    if not m:
        return None
    return date(int(m.group(3)), MONTHS.get(m.group(1), 0), int(m.group(2)))


def _fetch_rendered(url: str, timeout: int = 60) -> str:
    """Render a JS-heavy page through r.jina.ai (returns markdown)."""
    out = subprocess.run(
        ["curl", "-sL", "--compressed", "--max-time", str(timeout), "https://r.jina.ai/" + url],
        capture_output=True, text=True, encoding="utf-8", errors="ignore", timeout=timeout + 5,
    )
    return out.stdout or ""


def parse_markdown_events(markdown: str, year: int) -> list[dict]:
    """Parse the economic calendar markdown table, tracking 'Economic Events On' dates."""
    rows: list[dict] = []
    current = None
    for line in (markdown or "").splitlines():
        m = re.search(r"Economic Events On\s+\w+,\s+(\w{3})\s+(\d{1,2})", line)
        if m:
            month = MONTHS.get(m.group(1), 0)
            if month:
                current = date(year, month, int(m.group(2))).isoformat()
            continue
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().replace("**", "") for c in line.strip().strip("|").split("|")]
        if len(cells) < 8 or cells[0].lower() == "event" or set(cells[0]) <= {"-", ":"}:
            continue
        rows.append({
            "date": current,
            "event": cells[0], "country": cells[1], "event_time": cells[2],
            "for": cells[3], "actual": cells[4], "market_expectation": cells[5],
            "prior_to_this": cells[6], "revised_from": cells[7],
        })
    return rows


def fetch_economic(date_from: str | None = None, date_to: str | None = None) -> list[dict]:
    """Economic calendar for a date range.

    Yahoo's server HTML ignores from/to for plain clients, so the range is
    rendered through r.jina.ai. Yahoo renders one day per request (the first day
    of the range); query a single day to target that day.
    """
    query = "offset=0&size=100"
    if date_from and date_to:
        query = f"from={date_from}&to={date_to}&offset=0&size=100"
    year = int((date_from or date.today().isoformat())[:4])
    rows = parse_markdown_events(_fetch_rendered(f"{BASE}/economic?{query}"), year)
    if rows:
        return rows
    return parse_table(_fetch(f"{BASE}/economic?{query}"))


def fetch_earnings(date_from: str, date_to: str) -> list[dict]:
    return parse_table(_fetch(f"{BASE}/earnings?from={date_from}&to={date_to}&offset=0&size=100"))


def fetch_splits(date_from: str, date_to: str) -> list[dict]:
    return parse_table(_fetch(f"{BASE}/splits?from={date_from}&to={date_to}"))


def fetch_ipos(date_from: str, date_to: str) -> list[dict]:
    return parse_table(_fetch(f"{BASE}/ipo?from={date_from}&to={date_to}"))


def parse_ratio(text: str):
    """'2.00 - 1.00' -> 2.0; '1000.00 - 542.00' -> 1.845..."""
    m = re.match(r"\s*([\d.]+)\s*-\s*([\d.]+)", str(text or ""))
    if not m:
        return None
    a, b = float(m.group(1)), float(m.group(2))
    return None if b == 0 else a / b


def splits_for(ticker: str, days: int = 180) -> list[dict]:
    """Recent splits for one ticker (Yahoo symbol match, case-insensitive)."""
    end = date.today() + timedelta(days=1)
    start = end - timedelta(days=days)
    rows = fetch_splits(start.isoformat(), end.isoformat())
    out = []
    for row in rows:
        symbol = str(row.get("symbol") or "").upper()
        if symbol == ticker.upper():
            row = dict(row)
            row["ratio_factor"] = parse_ratio(row.get("ratio", ""))
            out.append(row)
    return out


def recent_split_flag(ticker: str, days: int = 120) -> dict | None:
    splits = splits_for(ticker, days=days)
    return splits[0] if splits else None


if __name__ == "__main__":
    import argparse
    import json
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["econ", "earnings", "splits", "ipo"])
    ap.add_argument("--from", dest="date_from", default=(date.today()).isoformat())
    ap.add_argument("--to", dest="date_to", default=(date.today() + timedelta(days=7)).isoformat())
    ap.add_argument("--ticker")
    args = ap.parse_args()
    if args.kind == "econ":
        data = fetch_economic(args.date_from, args.date_to)
    elif args.kind == "earnings":
        data = fetch_earnings(args.date_from, args.date_to)
    elif args.kind == "splits":
        data = fetch_splits(args.date_from, args.date_to)
    else:
        data = fetch_ipos(args.date_from, args.date_to)
    if args.ticker:
        data = [r for r in data if str(r.get("symbol") or "").upper() == args.ticker.upper()]
    print(json.dumps(data, indent=2, ensure_ascii=False))

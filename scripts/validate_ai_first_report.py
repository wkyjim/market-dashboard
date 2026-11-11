#!/usr/bin/env python3
"""Validate the active AI-first markdown and its frozen risk snapshot."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "data" / "latest-report.md"
RISK = ROOT / "data" / "risk_layer.json"
SNAP = ROOT / "data" / "report_snapshot.json"
GICS = [
    "Health Care", "Consumer Staples", "Consumer Discretionary", "Real Estate",
    "Financials", "Utilities", "Materials", "Industrials",
    "Communication Services", "Information Technology", "Energy",
]


def fail(msg: str) -> None:
    print("FAIL:", msg)
    raise SystemExit(1)


def main() -> int:
    text = REPORT.read_text(encoding="utf-8")
    risk = json.loads(RISK.read_text(encoding="utf-8"))
    snap = json.loads(SNAP.read_text(encoding="utf-8"))
    checks: dict[str, object] = {}
    checks["title"] = text.startswith("# AEGIS AI-First Market Intelligence")
    checks["generated"] = "Generated at:" in text
    checks["cutoff"] = "Data cutoff: 10 November 2026 US cash close" in text
    forbidden = [
        r"\bCIO\b", r"\bbullish_score\b", r"\bmarket_regime_v2\b",
        r"\bregime score\b", r"\bforward score\b", r"\bforward signal\b",
        r"\boverweight\b", r"\bunderweight\b", r"\bsector score\b",
        r"\bsector rating\b", r"\brule-based\b", r"\bcomposite score\b",
    ]
    checks["no_legacy_terms"] = not any(re.search(p, text, re.I) for p in forbidden)
    lines = text.splitlines()
    start = lines.index("## US Equities and 11 GICS Sectors") + 1
    table = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        if line.startswith("|") and "---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3 and cells[0] in GICS:
                table.append(cells)
    checks["gics_rows"] = len(table) == 11 and {r[0] for r in table} == set(GICS)
    checks["ideas"] = len(re.findall(r"^### (LLY|MSFT|COP|NVDA|COST) —", text, re.M)) == 5
    for field in ("Forecast 5D annualized volatility", "Spike probability", "Spike threshold", "Volatility model"):
        checks[f"risk_{field}"] = field in text
    checks["risk_vals"] = (
        abs(float(risk["models"]["volatility"]["forecast_5d_annualized"]) - 0.16612050738786388) < 1e-12
        and abs(float(risk["models"]["spike"]["probability_5d_vol_at_or_above_threshold"]) - 0.21009011101254835) < 1e-12
        and abs(float(risk["models"]["spike"]["threshold"]) - 0.184956) < 1e-12
    )
    urls = re.findall(r"https?://[^\s)\]]+", text)
    domains = {re.sub(r"^https?://", "", u).split("/")[0].lower() for u in urls}
    checks["source_count"] = len(urls) >= 10
    checks["source_domains"] = len(domains) >= 4
    report_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    risk_sha = hashlib.sha256(RISK.read_bytes()).hexdigest()
    checks["snapshot_report_sha"] = snap.get("report_sha256") == report_sha
    checks["snapshot_risk_sha"] = snap.get("risk_layer_sha256") == risk_sha
    checks["snapshot_id"] = bool(snap.get("snapshot_id"))
    failed = [k for k, v in checks.items() if not v]
    for k, v in checks.items():
        print(f"{k}: {'PASS' if v else 'FAIL'}")
    print("report_sha256:", report_sha)
    print("risk_sha256:", risk_sha)
    print("sources:", len(urls), "domains:", len(domains))
    if failed:
        fail("; ".join(failed))
    print("QC PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

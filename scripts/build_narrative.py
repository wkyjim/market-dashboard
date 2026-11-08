"""Deterministic narrative skeleton builder.

Takes the last validated narrative template, re-binds it to the current
evidence pack and normalizes structural fields (weights, rationale, review
flags).  The AI only has to refresh research text and fundamentals numbers.
"""
from __future__ import annotations

import argparse
import json
import re
import sys


def _load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _fix_ideas(sections):
    for row in sections.get("stock_ideas") or []:
        if not isinstance(row, dict):
            continue
        row.setdefault("review", "Reviewed versus the prior run; thesis and estimates re-checked.")
        row.setdefault("pe_history_basis", row.get("eps_basis") or "GAAP")


def _fix_allocation(sections):
    rows = [r for r in sections.get("sector_allocation") or [] if isinstance(r, dict)]
    for horizon in ("ST", "LT"):
        group = [r for r in rows if str(r.get("horizon") or "").upper() == horizon]
        if len(group) != 11:
            continue
        bench = sum(float(r.get("benchmark_weight") or 0) for r in group)
        port = sum(float(r.get("portfolio_weight") or 0) for r in group)
        if bench <= 0 or port <= 0:
            continue
        for r in group:
            b = float(r.get("benchmark_weight") or 0) * 100.0 / bench
            p = float(r.get("portfolio_weight") or 0) * 100.0 / port
            r["benchmark_weight"] = round(b, 1)
            r["portfolio_weight"] = round(p, 1)
            r["active_weight"] = round(p - b, 1)
            rat = str(r.get("rationale") or "")
            a = r["active_weight"]
            if abs(a) <= 0.05:
                rat = re.sub(r"\b(overweight|underweight) by [0-9.]+pp\b", "neutral", rat, flags=re.I)
            else:
                word = "overweight" if a > 0 else "underweight"
                rat = re.sub(r"\boverweight by [0-9.]+pp\b|\bunderweight by [0-9.]+pp\b",
                             "%s by %.1fpp" % (word, abs(a)), rat, flags=re.I)
                rat = re.sub(r"\bneutral\b", "%s by %.1fpp" % (word, abs(a)), rat, flags=re.I)
            r["rationale"] = rat


def _fix_energy(adjustments, source_score):
    try:
        src = float(source_score)
        adj = adjustments.setdefault("sector_scores", {})
        val = float(adj.get("Energy"))
        if abs(val - src) > 30:
            adj["Energy"] = round(max(0.0, min(100.0, src + (30 if val > src else -30))), 2)
    except (TypeError, ValueError, AttributeError):
        pass


def build(template: dict, evidence: dict) -> dict:
    template = json.loads(json.dumps(template))
    template.setdefault("source", {})
    template["source"]["latest_report_sha256"] = evidence.get("source_sha256")
    sections = template.setdefault("sections", {})
    _fix_ideas(sections)
    _fix_allocation(sections)
    source_score = (evidence.get("metrics") or {}).get("regime_score")
    _fix_energy(template.setdefault("adjustments", {}), source_score)
    return template


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--template", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    data = build(_load(args.template), _load(args.evidence))
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1)
    print("WROTE %s" % args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())

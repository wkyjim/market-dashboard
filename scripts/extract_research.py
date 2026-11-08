"""Extract the full qualitative research schema from a published report card."""
from __future__ import annotations

import argparse
import json
import os
import re

LABELS = {
    "thesis": "Thesis",
    "review": "Review",
    "assumptions": "Assumptions",
    "why_vs_alternatives": "Why this versus alternatives",
    "contrary": "Contrary evidence",
    "peer_comparison": "Peer comparison",
    "sector_context": "Sector context",
    "catalysts": "Catalysts",
    "risks": "Risks",
    "conclusion": "Conclusion",
    "decision_rationale": "Decision rationale",
    "invalidation": "Invalidation",
    "opposing": "Strongest opposing argument",
}


def _para(card: str, label: str) -> str | None:
    m = re.search(r"<p><strong>%s\.</strong>\s*(.*?)</p>" % re.escape(label), card, re.S)
    if not m:
        return None
    return re.sub(r"<[^>]+>", "", m.group(1)).strip()


def extract(html: str) -> dict[str, dict]:
    out = {}
    for card in re.findall(r'<div class="idea-card">(.*?)</div>', html, re.S):
        title = re.search(r"<h3>([A-Z][A-Z0-9.\-]*)", card)
        if not title:
            continue
        ticker = title.group(1)
        research = {}
        for key, label in LABELS.items():
            value = _para(card, label)
            if value:
                research[key] = value
        entry = _para(card, "Entry condition") or ""
        m = re.match(r"(.*?)\s*Exit\.\s*(.*)$", entry, re.S)
        if m:
            research["entry_condition"] = m.group(1).strip()
            research["exit"] = m.group(2).strip()
        prov = re.search(r"<tr><td>Provenance</td><td>(.*?)</td></tr>", card, re.S)
        if prov:
            raw = re.sub(r"<[^>]+>", "", prov.group(1))
            research["valuation_provenance"] = {
                k.strip(): v.strip() for k, v in
                (part.split("=", 1) for part in raw.split(";") if "=" in part)
            }
        out[ticker] = research
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    ap.add_argument("--research-dir", required=True)
    args = ap.parse_args(argv)
    with open(args.html, encoding="utf-8") as fh:
        cards = extract(fh.read())
    for ticker, research in cards.items():
        path = os.path.join(args.research_dir, "%s.json" % ticker)
        data = {}
        if os.path.exists(path):
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        data.setdefault("ticker", ticker)
        data.setdefault("research", {})
        data["research"].update(research)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=1)
        print("UPDATED", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

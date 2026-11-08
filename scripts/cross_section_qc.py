"""Deterministic cross-section QC for the rendered market-intelligence HTML.

Catches the recurring failures: regime numbers that differ between sections,
per-ticker recommendations that contradict the idea card, heat maps that
disagree with the 11-sector allocation, and wrong official calendar dates.
"""
from __future__ import annotations

import re

ACTION = r"(Buy|Add|Hold|Reduce|Sell)"


def _section(html: str, anchor: str) -> str:
    start = html.find(anchor)
    if start < 0:
        return ""
    nxt = html.find("<h2", start + len(anchor))
    return html[start: nxt if nxt > 0 else len(html)]


def _heat_weights(section: str) -> dict:
    out = {}
    for m in re.finditer(r"<tr><td>([^<]+)</td><td[^>]*>([+-]?[0-9.]+)%</td></tr>", section):
        out[m.group(1).strip()] = float(m.group(2))
    return out


def _alloc_weights(narrative: dict, horizon: str) -> dict:
    out = {}
    for row in (narrative.get("sections") or {}).get("sector_allocation") or []:
        if not isinstance(row, dict):
            continue
        if str(row.get("horizon") or "").upper() != horizon:
            continue
        try:
            out[str(row.get("sector") or "").strip()] = float(row.get("active_weight"))
        except (TypeError, ValueError):
            continue
    return out


def _cards(html: str) -> dict:
    out = {}
    for card in re.findall(r'<div class="idea-card">(.*?)</div>', html, re.S):
        title = re.search(r"<h3>([A-Z][A-Z0-9.\-]*)", card)
        rec = re.search(r"Stock &middot; " + ACTION, card)
        if title and rec:
            out[title.group(1)] = rec.group(1)
    return out


def normalize_scores(html: str, ai_score: float | None, source_score: float | None) -> str:
    """Rewrite stale score mentions in prose to the current canonical values.

    The numbers are per-run; nothing is pinned. Any sentence that quoted an
    older source/AI/delta is corrected before the HTML-to-JSON QC runs.
    """
    if ai_score is None or source_score is None:
        return html
    delta = float(ai_score) - float(source_score)
    html = re.sub(r"(Source rule-based:\s*)([0-9]+\.[0-9]+)(\s*\|\s*AI:\s*)([0-9]+\.[0-9]+)",
                  lambda m: "%s%.2f%s%.2f" % (m.group(1), float(source_score), m.group(3), float(ai_score)), html)
    html = re.sub(r"(\bAI\s+)([0-9]+\.[0-9]+)(\s+vs source)",
                  lambda m: m.group(1) + "%.2f" % float(ai_score) + m.group(3), html)
    html = re.sub(r"(vs source\s+)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(source_score), html)
    html = re.sub(r"(source rule-based\s+)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(source_score), html, flags=re.I)
    html = re.sub(r"(?<!AI )(rule-based (?:regime )?score (?:of|at|is)\s*)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(source_score), html, flags=re.I)
    html = re.sub(r"(?<!AI )(source (?:regime )?score (?:of|at|is)\s*)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(source_score), html, flags=re.I)
    html = re.sub(r"(AI regime score at\s+)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(ai_score), html)
    html = re.sub(r"(AI (?:regime )?score\s+)([0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%.2f" % float(ai_score), html)
    html = re.sub(r"(delta\s+)([+-]?[0-9]+\.[0-9]+)",
                  lambda m: m.group(1) + "%+.2f" % delta, html)
    return html


def check(html: str, narrative: dict, ai_score: float | None = None,
          source_score: float | None = None) -> list[str]:
    fails: list[str] = []
    cards = _cards(html)

    # 1. Regime numbers repeated across sections must equal the canonical AI score.
    if ai_score is not None:
        for m in re.finditer(r"AI regime score[^0-9]{0,40}([0-9]+\.[0-9]+)", html):
            if abs(float(m.group(1)) - float(ai_score)) > 0.05:
                fails.append("cross-section: 'AI regime score %.2f' != canonical %.2f"
                             % (float(m.group(1)), float(ai_score)))
        for m in re.finditer(r"AI score\s+([0-9]+\.[0-9]+)\s+vs source", html):
            if abs(float(m.group(1)) - float(ai_score)) > 0.05:
                fails.append("cross-section: 'AI score %.2f vs source' != canonical %.2f"
                             % (float(m.group(1)), float(ai_score)))
        for m in re.finditer(r"AI:\s*([0-9]+\.[0-9]+)", html):
            if abs(float(m.group(1)) - float(ai_score)) > 0.05:
                fails.append("cross-section: 'AI: %.2f' != canonical %.2f"
                             % (float(m.group(1)), float(ai_score)))

    # 2. Every ticker mention with an action must agree with its idea card.
    prose = re.sub(r'<div class="idea-card">.*?</div>', " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", prose)
    # 1b. Source rule-based score repeated in prose must equal the canonical value.
    if source_score is not None:
        for m in re.finditer(r"source rule-based\s+([0-9]+\.[0-9]+)", text, re.I):
            if abs(float(m.group(1)) - float(source_score)) > 0.05:
                fails.append("cross-section: prose 'source %s' != canonical source %.2f"
                             % (m.group(1), float(source_score)))
        for m in re.finditer(r"(?:vs|against) source\s+([0-9]+\.[0-9]+)", text, re.I):
            if abs(float(m.group(1)) - float(source_score)) > 0.05:
                fails.append("cross-section: prose 'vs source %s' != canonical source %.2f"
                             % (m.group(1), float(source_score)))
        for m in re.finditer(r"source score\s+([0-9]+\.[0-9]+)", text, re.I):
            if abs(float(m.group(1)) - float(source_score)) > 0.05:
                fails.append("cross-section: 'source score %s' != canonical %.2f"
                             % (m.group(1), float(source_score)))
        for m in re.finditer(r"source rule-based\s+([0-9]+\.[0-9]+)", text, re.I):
            if abs(float(m.group(1)) - float(source_score)) > 0.05:
                fails.append("cross-section: 'source rule-based %s' != canonical %.2f"
                             % (m.group(1), float(source_score)))
        for m in re.finditer(r"(?<!AI )(?:rule-based|source) (?:regime )?score (?:of|at|is)\s*([0-9]+\.[0-9]+)", text, re.I):
            if abs(float(m.group(1)) - float(source_score)) > 0.05:
                fails.append("cross-section: prose rule-based score %s != canonical %.2f"
                             % (m.group(1), float(source_score)))


    for ticker, rec in cards.items():
        patterns = [
            r"\b%s\b[^.]{0,60}?\b%s\b" % (re.escape(ticker), ACTION),
            r"\b%s\b[^.]{0,30}?\b%s\b" % (ACTION, re.escape(ticker)),
        ]
        seen = set()
        for pat in patterns:
            for m in re.finditer(pat, text):
                g1 = m.group(1)
                action = g1 if g1 in ("Buy", "Add", "Hold", "Reduce", "Sell") else m.group(2)
                if action in ("Buy", "Add", "Hold", "Reduce", "Sell"):
                    seen.add(action)
        wrong = sorted(a for a in seen if a != rec)
        if wrong:
            fails.append("cross-section: %s card says %s but text also says %s"
                         % (ticker, rec, "/".join(wrong)))

    # 3. Heat maps must equal the allocation active weights for the same horizon.
    for horizon, anchor in (("ST", 'id="heat-st"'), ("LT", 'id="heat-lt"')):
        heat = _heat_weights(_section(html, anchor))
        alloc = _alloc_weights(narrative, horizon)
        if not heat or not alloc:
            continue
        for sector, weight in heat.items():
            if sector in alloc and abs(weight - alloc[sector]) > 0.1:
                fails.append("cross-section: %s heat map %s %.1f%% != allocation %.1f%%"
                             % (horizon, sector, weight, alloc[sector]))

    # 4. Official calendar dates; historical events must not sit in upcoming catalysts.
    if "FOMC" in text and re.search(r"Dec(?:ember)?\s+10", text):
        fails.append("cross-section: December FOMC is Dec 8-9, not Dec 10")
    if "CPI" in text and re.search(r"Nov(?:ember)?\s+12", text):
        fails.append("cross-section: October CPI is released Nov 10, not Nov 12")
    # ISO dates: official FOMC 2026-12-08/09 and October CPI 2026-11-10.
    for m in re.finditer(r"(2026-11-\d{2})\s+CPI", text):
        if m.group(1) != "2026-11-10":
            fails.append("cross-section: CPI date %s is wrong; October CPI is 2026-11-10" % m.group(1))
    for m in re.finditer(r"CPI[^0-9]{0,10}(2026-11-\d{2})", text):
        if m.group(1) != "2026-11-10":
            fails.append("cross-section: CPI date %s is wrong; October CPI is 2026-11-10" % m.group(1))
    for m in re.finditer(r"FOMC[^.]{0,60}", text):
        for d in re.findall(r"2026-12-\d{2}", m.group(0)):
            if d not in ("2026-12-08", "2026-12-09"):
                fails.append("cross-section: FOMC date %s is wrong; December FOMC is 2026-12-08/09" % d)

    # 5. WTI commentary must contain the same snapshot printed elsewhere.
    snap = re.search(r"WTI[^0-9]{0,12}([0-9]{2,3}(?:\.[0-9]+)?)", text)
    if snap:
        wti = float(snap.group(1))
        for lo_s, hi_s in re.findall(
                r"WTI[^.]{0,50}?(\d{2,3}(?:\.\d+)?)\s*(?:-|\u2013|to)\s*(\d{2,3}(?:\.\d+)?)", text):
            lo, hi = sorted((float(lo_s), float(hi_s)))
            if not (lo - 0.5 <= wti <= hi + 0.5):
                fails.append("cross-section: WTI commentary $%.0f-%.0f excludes the $%.2f snapshot"
                             % (lo, hi, wti))

    # 6. One Nasdaq identifier only, so levels cannot be mixed.
    if "Nasdaq Composite" in text and "Nasdaq 100" in text:
        fails.append("cross-section: both Nasdaq Composite and Nasdaq 100 are cited; use one identifier")
    for _m in re.finditer(r"Nasdaq(?!\s*(?:Composite|100))", text):
        fails.append("cross-section: bare 'Nasdaq' at offset %d is ambiguous; label it Nasdaq Composite or Nasdaq 100"
                     % _m.start())

    # 7. Long Energy against a weak AI rating needs a contrarian/valuation reason.
    adj = narrative.get("adjustments") or {}
    try:
        energy_ai = float((adj.get("sector_scores") or {}).get("Energy"))
    except (TypeError, ValueError):
        energy_ai = None
    if energy_ai is not None and energy_ai < 30:
        for row in (narrative.get("sections") or {}).get("sector_allocation") or []:
            if not isinstance(row, dict) or str(row.get("sector") or "").strip() != "Energy":
                continue
            try:
                active = float(row.get("active_weight"))
            except (TypeError, ValueError):
                continue
            if active > 0 and not re.search(
                    r"contrarian|valuation|cheap|hedge|relative|underweight", str(row.get("rationale") or ""), re.I):
                fails.append("cross-section: %s Energy active +%.1fpp vs AI %.1f needs a contrarian/valuation rationale"
                             % (row.get("horizon") or "?", active, energy_ai))
    return fails

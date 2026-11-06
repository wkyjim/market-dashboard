"""Official event dates used to validate report claims.

Sources: Federal Reserve FOMC calendar and BLS CPI release schedule. Keep this
list small and cite it in the report; it exists to catch wrong dates, not to
replace the official calendars.
"""
from __future__ import annotations

from datetime import date

FOMC = {
    2026: [("2026-12-08", "2026-12-09")],
}
CPI = {
    2026: ["2026-11-10"],
}


def known(event: str) -> list:
    event = event.strip().upper()
    if event == "FOMC":
        return [d for pairs in FOMC.values() for pair in pairs for d in pair]
    if event == "CPI":
        return [d for days in CPI.values() for d in days]
    return []


def verify(event: str, day: str) -> bool:
    """True when the date is a published official date for the event."""
    try:
        target = date.fromisoformat(str(day)[:10]).isoformat()
    except ValueError:
        return False
    return target in known(event)


def check_rows(rows) -> list[str]:
    """rows: [{event, date}] -> failures for dates that contradict the official list."""
    fails = []
    for i, row in enumerate(rows or []):
        if not isinstance(row, dict):
            continue
        event = str(row.get("event") or "").strip()
        day = str(row.get("date") or "").strip()
        dates = known(event)
        if not dates:
            continue
        if day not in dates:
            fails.append("calendar row %d: %s %s is not an official date (%s)"
                         % (i, event, day, ", ".join(dates)))
    return fails

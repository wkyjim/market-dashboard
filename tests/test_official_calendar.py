"""Official event-date checks."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from official_calendar import check_rows, verify


def test_fomc_december_dates():
    assert verify("FOMC", "2026-12-08")
    assert verify("FOMC", "2026-12-09")
    assert not verify("FOMC", "2026-12-10")


def test_october_cpi_release_date():
    assert verify("CPI", "2026-11-10")
    assert not verify("CPI", "2026-11-12")


def test_check_rows_flags_wrong_date():
    fails = check_rows([{"event": "FOMC", "date": "2026-12-10"}])
    assert fails and "not an official date" in fails[0]
    assert check_rows([{"event": "FOMC", "date": "2026-12-08"}]) == []

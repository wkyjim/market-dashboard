"""SEC TTM contiguity guard."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from fundamental_audit import enrich_ideas, ttm_eps


def _q(end, val):
    return {"end": end, "start": end, "val": val, "form": "10-Q"}


def test_contiguous_quarters_sum():
    facts = {"quarters": [_q("2025-12-31", 1.0), _q("2026-03-31", 1.0),
                          _q("2026-06-30", 1.0), _q("2026-09-30", 1.0)], "annual": []}
    assert ttm_eps(facts) == 4.0


def test_gapped_quarters_are_rejected():
    facts = {"quarters": [_q("2025-09-30", 1.0), _q("2026-06-30", 1.0),
                          _q("2026-09-30", 1.0), _q("2026-12-31", 1.0)], "annual": []}
    assert ttm_eps(facts) is None


def test_enrich_fills_quarters_from_sec():
    def q(end, val):
        return {"end": end, "start": end, "val": val, "form": "10-Q"}

    facts = {"quarters": [q("2025-12-31", 1.0), q("2026-03-31", 1.0),
                          q("2026-06-30", 1.0), q("2026-09-30", 1.0)], "annual": []}
    ideas = [{"ticker": "X", "sec_cik": "1"}]
    enrich_ideas(ideas, lookup=lambda cik: facts)
    assert ideas[0]["ttm_eps_diluted"] == 4.0
    assert ideas[0]["ttm_eps_quarters"] == [1.0, 1.0, 1.0, 1.0]

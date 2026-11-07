"""SEC TTM contiguity guard."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from fundamental_audit import ttm_eps


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

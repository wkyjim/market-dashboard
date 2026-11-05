"""Tests for Yahoo calendar parsing (no network)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from calendar_web import _looks_like_date, parse_ratio, parse_table

HTML = """
<table>
<tr><th>Symbol</th><th>Company</th><th>Payable On</th><th>Ratio</th></tr>
<tr><td>AAPL</td><td>Apple Inc.</td><td>Nov 05, 2026</td><td>4.00 - 1.00</td></tr>
<tr><td>XYZ</td><td>Example</td><td>Nov 06, 2026</td><td>2.00 - 1.00</td></tr>
</table>
"""


def test_parse_table_maps_headers():
    rows = parse_table(HTML)
    assert len(rows) == 2
    assert rows[0]["symbol"] == "AAPL"
    assert rows[0]["payable_on"] == "Nov 05, 2026"


def test_parse_ratio():
    assert parse_ratio("4.00 - 1.00") == 4.0
    assert parse_ratio("1000.00 - 542.00") > 1.8
    assert parse_ratio("n/a") is None


def test_looks_like_date():
    assert _looks_like_date("Nov 05, 2026")
    assert not _looks_like_date("ConocoPhillips")

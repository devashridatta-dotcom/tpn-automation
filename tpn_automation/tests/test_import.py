from tpn_automation import parser

def test_parse_runs():
    result = parser.parse_tpn("tests/sample_tpn.pdf")
    assert result is not None

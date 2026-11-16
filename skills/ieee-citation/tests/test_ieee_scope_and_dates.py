from pathlib import Path
import importlib.util
import sys

PATH = Path(__file__).parents[1] / "scripts/ieee_citation.py"
spec = importlib.util.spec_from_file_location("ieee_citation_scope_test", PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def test_named_venue_scope_does_not_accept_unrelated_ieee_journals():
    assert module.in_scope("IEEE Transactions on Automatic Control", "tac")
    assert not module.in_scope("IEEE Transactions on Wireless Communications", "tac")
    assert not module.in_scope("Nature Communications", "all")


def test_unknown_crossref_year_falls_back_to_valid_date():
    assert module.year_from({"published-print": {"date-parts": [[None]]},
                             "published-online": {"date-parts": [[2025, 2]]}}) == "2025"
    assert module.year_from({"issued": {"date-parts": [[None]]}}) == ""

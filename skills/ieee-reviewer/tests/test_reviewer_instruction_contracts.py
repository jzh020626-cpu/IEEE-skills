from pathlib import Path

ROOT = Path(__file__).parents[1]

def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

def test_severity_and_blocking_contract_is_present() -> None:
    text = read("SKILL.md") + read("references/technical-concern-taxonomy.md")
    assert "Major Concerns" in text
    assert "Minor Comments" in text
    assert "Blocking: Yes/No" in text
    assert "Minor comments are never blocking" in text
    assert "Do not impose a concern quota" in text

def test_reviewers_are_isolated_before_synthesis() -> None:
    text = read("SKILL.md") + read("references/technical-concern-taxonomy.md")
    assert "genuinely separate context" in text
    assert "Freeze each report before comparison" in text
    assert "must not read another review" in text

def test_traceability_and_non_invention_are_required() -> None:
    text = read("SKILL.md") + read("references/technical-concern-taxonomy.md")
    assert "claim_pointer" in text
    assert "evidence_pointer" in text
    assert "Do not invent experiments" in text

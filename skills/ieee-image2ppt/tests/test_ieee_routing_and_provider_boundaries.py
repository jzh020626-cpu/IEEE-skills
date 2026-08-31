from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class IEEERoutingAndProviderBoundaryTests(unittest.TestCase):
    def test_trigger_excludes_new_decks_and_scanned_research_papers(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Do not use to author a new deck", skill)
        self.assertIn("ordinary scanned research-paper PDF", skill)
        self.assertIn("ieee-paper2ppt", skill)
        self.assertIn("ieee-reader", skill)

    def test_external_provider_boundary_is_visible_and_not_marketing(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        hints = " ".join((ROOT / "cli/image2ppt/runtime/deck_text_hints.py").read_text(encoding="utf-8").split())
        self.assertIn("explicit user authorization", skill)
        self.assertIn("--allow-external-ocr", skill)
        self.assertIn("uploads page material to an external provider", hints)
        self.assertIn("account, quota, or cost implications", hints)
        self.assertNotIn("risk-free with no extra cost", hints)
        self.assertNotIn("more than enough for this skill", hints)


if __name__ == "__main__":
    unittest.main()

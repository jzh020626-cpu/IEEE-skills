from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

class IEEEFigureMultipanelEvidenceTests(unittest.TestCase):
    def test_engineering_roles_and_integrity_boundaries(self) -> None:
        reference = " ".join(read("skills/ieee-figure/references/multipanel-evidence-architecture.md").split())
        for requirement in (
            "one Results-level question",
            "Primary evidence",
            "Baseline/control",
            "Stress or perturbation",
            "Boundary/failure",
            "Robotics/control",
            "Communications/networking",
            "Control/theory",
            "Never hide evidence that changes the central conclusion",
        ):
            self.assertIn(requirement, reference)

    def test_router_contract_and_eval_are_connected(self) -> None:
        for relative in (
            "skills/ieee-figure/SKILL.md",
            "skills/ieee-figure/manifest.yaml",
            "skills/ieee-figure/static/core/contract.md",
            "skills/ieee-figure/references/figure-contract.md",
            "skills/ieee-figure/references/design-theory.md",
        ):
            self.assertIn("multipanel-evidence-architecture.md", read(relative), relative)
        ids = {case["id"] for case in json.loads(read("skills/ieee-figure/evals/evals.json"))["evals"]}
        self.assertIn("multipanel-figure-level-claim-and-role-diversity", ids)

    def test_no_nature_specific_routes(self) -> None:
        reference = read("skills/ieee-figure/references/multipanel-evidence-architecture.md")
        for forbidden in ("nature-results-discussion", "Extended Data", "MIRA", "Centromere", "Robin"):
            self.assertNotIn(forbidden, reference)

if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

class EngineeringEvidenceChainTests(unittest.TestCase):
    def test_paper_type_routes_and_hard_boundaries(self) -> None:
        text = read("skills/ieee-shared/core/engineering-evidence-chain.md")
        for requirement in (
            "Algorithm/learning",
            "Control/theory",
            "Robotics/system",
            "Communications/networking",
            "Benchmark/resource",
            "Simulation illustrates; it does not prove",
            "Negative or mixed evidence that changes a central conclusion stays visible",
        ):
            self.assertIn(requirement, text)

    def test_writing_and_polishing_route_to_shared_chain(self) -> None:
        for relative in (
            "skills/ieee-shared/SKILL.md",
            "skills/ieee-shared/manifest.yaml",
            "skills/ieee-writing/SKILL.md",
            "skills/ieee-writing/manifest.yaml",
            "skills/ieee-polishing/SKILL.md",
            "skills/ieee-polishing/manifest.yaml",
        ):
            self.assertIn("engineering-evidence-chain.md", read(relative), relative)

if __name__ == "__main__":
    unittest.main()

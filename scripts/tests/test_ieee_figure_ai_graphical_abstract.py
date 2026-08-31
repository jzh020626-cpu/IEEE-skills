from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")

class IEEEFigureAIGraphicalAbstractTests(unittest.TestCase):
    def test_policy_provenance_and_non_invention_gates(self) -> None:
        reference = read("skills/ieee-figure/references/ai-graphical-abstract-workflow.md")
        for requirement in (
            "verify the target venue's current author instructions",
            "concept draft",
            "Do not invent hardware",
            "Record prompt, model/backend, generation date",
            "explicit authorization",
            "generated technical text and symbols as untrusted",
        ):
            self.assertIn(requirement, reference)

    def test_router_and_eval_expose_the_workflow(self) -> None:
        skill = read("skills/ieee-figure/SKILL.md")
        manifest = read("skills/ieee-figure/manifest.yaml")
        self.assertIn("ai-graphical-abstract-workflow.md", skill)
        self.assertIn("ai-graphical-abstract-workflow.md", manifest)
        self.assertNotIn("OpenRouter", skill + manifest)
        ids = {case["id"] for case in json.loads(read("skills/ieee-figure/evals/evals.json"))["evals"]}
        self.assertIn("ai-graphical-abstract-policy-and-accountability-gate", ids)

if __name__ == "__main__":
    unittest.main()

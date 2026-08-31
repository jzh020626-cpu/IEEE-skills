from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills/ieee-figure/scripts/audit_figure_collisions.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("ieee_figure_collision_audit_test", SCRIPT)
PYMUPDF_AVAILABLE = any(
    importlib.util.find_spec(module_name) is not None
    for module_name in ("pymupdf", "fitz")
)
MATPLOTLIB_AVAILABLE = importlib.util.find_spec("matplotlib") is not None


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class CollisionGeometryTests(unittest.TestCase):
    def test_clean_text_and_distant_line_pass(self) -> None:
        page = AUDIT.PageGeometry(
            page=1,
            bbox=(0, 0, 200, 120),
            texts=[AUDIT.TextBox(0, "Clear", (50, 20, 90, 32))],
            traces=[AUDIT.TraceBox(0, "Clear", (50, 20, 90, 32))],
            strokes=[
                AUDIT.StrokePath(
                    0,
                    (20, 70, 180, 70),
                    1.0,
                    (((20, 70), (180, 70)),),
                )
            ],
        )

        result = AUDIT.audit_geometries([page])

        self.assertEqual(result["verdict"], "PASS")
        self.assertEqual(result["summary"]["fail"], 0)

    def test_text_stroke_and_text_text_collisions_block_delivery(self) -> None:
        page = AUDIT.PageGeometry(
            page=1,
            bbox=(0, 0, 200, 120),
            texts=[
                AUDIT.TextBox(0, "First", (50, 40, 100, 54)),
                AUDIT.TextBox(1, "Second", (80, 43, 125, 57)),
            ],
            traces=[
                AUDIT.TraceBox(0, "First", (50, 40, 100, 54)),
                AUDIT.TraceBox(1, "Second", (80, 43, 125, 57)),
            ],
            strokes=[
                AUDIT.StrokePath(
                    0,
                    (20, 47, 180, 47),
                    1.0,
                    (((20, 47), (180, 47)),),
                )
            ],
        )

        result = AUDIT.audit_geometries([page])
        kinds = {finding["kind"] for finding in result["findings"]}

        self.assertEqual(result["verdict"], "FIX BEFORE DELIVERY")
        self.assertIn("text-text", kinds)
        self.assertIn("text-stroke", kinds)
        self.assertEqual(AUDIT.exit_code(result), 1)

    def test_contained_fill_is_informational_but_partial_fill_warns(self) -> None:
        page = AUDIT.PageGeometry(
            page=1,
            bbox=(0, 0, 200, 120),
            texts=[
                AUDIT.TextBox(0, "Inside", (60, 40, 90, 52)),
                AUDIT.TextBox(1, "Edge", (120, 40, 155, 52)),
            ],
            traces=[
                AUDIT.TraceBox(0, "Inside", (60, 40, 90, 52)),
                AUDIT.TraceBox(1, "Edge", (120, 40, 155, 52)),
            ],
            fills=[
                AUDIT.FilledRegion(0, (50, 30, 100, 60), "fill"),
                AUDIT.FilledRegion(1, (105, 30, 135, 60), "fill"),
            ],
        )

        result = AUDIT.audit_geometries([page])

        self.assertEqual(result["verdict"], "REVIEW REQUIRED")
        self.assertEqual(result["summary"]["contained_fill_overlays"], 1)
        self.assertEqual(result["summary"]["warn"], 1)
        self.assertEqual(result["findings"][0]["kind"], "text-fill-edge")
        self.assertEqual(AUDIT.exit_code(result), 0)
        self.assertEqual(AUDIT.exit_code(result, strict=True), 1)

    def test_page_clipping_blocks_delivery(self) -> None:
        page = AUDIT.PageGeometry(
            page=1,
            bbox=(0, 0, 200, 120),
            traces=[AUDIT.TraceBox(0, "Clipped", (50, -8, 90, 4))],
        )

        result = AUDIT.audit_geometries([page])

        self.assertEqual(result["summary"]["fail"], 1)
        self.assertEqual(result["findings"][0]["kind"], "text-page-clipping")

    def test_pdf_without_editable_text_is_not_claimed_as_checked(self) -> None:
        result = AUDIT.audit_geometries(
            [AUDIT.PageGeometry(page=1, bbox=(0, 0, 200, 120))]
        )

        self.assertFalse(result["auditable"])
        self.assertEqual(result["verdict"], "NOT AUDITABLE")
        self.assertEqual(AUDIT.exit_code(result), 2)

    def test_final_pdf_width_mismatch_blocks_delivery(self) -> None:
        expected_mm = 182.0
        expected_pt = expected_mm * 72.0 / 25.4
        page = AUDIT.PageGeometry(
            page=1,
            bbox=(0, 0, expected_pt - 20, 120),
            texts=[AUDIT.TextBox(0, "Label", (20, 20, 50, 32))],
            traces=[AUDIT.TraceBox(0, "Label", (20, 20, 50, 32))],
        )
        result = AUDIT.audit_geometries([page], expected_width_mm=expected_mm)
        self.assertEqual("FIX BEFORE DELIVERY", result["verdict"])
        self.assertEqual("page-width-mismatch", result["findings"][0]["kind"])
        self.assertEqual(1, AUDIT.exit_code(result))


@unittest.skipUnless(PYMUPDF_AVAILABLE, "PyMuPDF is not installed in this test runtime")
class CollisionPdfEndToEndTests(unittest.TestCase):
    def test_real_pdf_detects_crossed_text_and_writes_overlay(self) -> None:
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "collision.pdf"
            overlay = root / "collision-overlay.pdf"
            report = root / "collision.json"

            document = fitz.open()
            page = document.new_page(width=200, height=120)
            page.insert_text((50, 60), "Crossed", fontsize=12)
            page.insert_text((50, 95), "Clear", fontsize=12)
            page.draw_line((20, 55), (180, 55), width=1)
            document.save(source)
            document.close()

            result = AUDIT.audit_pdf(source)
            report.write_text(json.dumps(result), encoding="utf-8")
            AUDIT.write_overlay_pdf(source, overlay, result["findings"])
            first_overlay_size = overlay.stat().st_size
            AUDIT.write_overlay_pdf(source, overlay, result["findings"])

            crossed = [
                finding
                for finding in result["findings"]
                if finding["kind"] == "text-stroke"
            ]
            self.assertEqual([finding["text"] for finding in crossed], ["Crossed"])
            self.assertTrue(overlay.is_file())
            self.assertGreater(overlay.stat().st_size, source.stat().st_size)
            self.assertEqual(overlay.stat().st_size, first_overlay_size)
            self.assertTrue(json.loads(report.read_text(encoding="utf-8"))["findings"])

    def test_real_pdf_media_box_width_is_measured(self) -> None:
        try:
            import pymupdf as fitz
        except ImportError:
            import fitz

        expected_mm = 182.0
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "width.pdf"
            document = fitz.open()
            page = document.new_page(width=expected_mm * 72.0 / 25.4, height=200)
            page.insert_text((20, 40), "Exact width", fontsize=10)
            document.save(source)
            document.close()

            passed = AUDIT.audit_pdf(source, expected_width_mm=expected_mm)
            failed = AUDIT.audit_pdf(source, expected_width_mm=88.9)
            self.assertEqual("PASS", passed["verdict"])
            self.assertEqual("FIX BEFORE DELIVERY", failed["verdict"])
            self.assertEqual("page-width-mismatch", failed["findings"][0]["kind"])


@unittest.skipUnless(PYMUPDF_AVAILABLE and MATPLOTLIB_AVAILABLE, "PyMuPDF and matplotlib are required")
class BundledTemplateEndToEndTests(unittest.TestCase):
    def test_all_demo_templates_preserve_ieee_width_and_pass_rendered_audit(self) -> None:
        script = ROOT / "skills/ieee-figure/scripts/plot_templates.py"
        expected = {
            "volcano": 88.9,
            "roc": 88.9,
            "dotplot": 182.0,
            "marginal": 182.0,
            "paired": 88.9,
        }
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for kind, width in expected.items():
                with self.subTest(kind=kind):
                    prefix = root / kind
                    result = subprocess.run(
                        [sys.executable, str(script), kind, "--demo", "--output", str(prefix)],
                        text=True,
                        capture_output=True,
                        check=False,
                    )
                    self.assertEqual(0, result.returncode, result.stderr)
                    audit = json.loads(prefix.with_suffix(".collisions.json").read_text(encoding="utf-8"))
                    self.assertIn(audit["verdict"], {"PASS", "REVIEW REQUIRED"})
                    self.assertAlmostEqual(width, audit["dimensions"][0]["width_mm"], delta=0.5)


class CollisionWorkflowIntegrationTests(unittest.TestCase):
    def test_every_python_or_r_figure_routes_through_collision_audit(self) -> None:
        skill = read("skills/ieee-figure/SKILL.md")
        python_backend = read("skills/ieee-figure/static/fragments/backend/python.md")
        r_backend = read("skills/ieee-figure/static/fragments/backend/r.md")
        qa = read("skills/ieee-figure/references/qa-contract.md")

        for relative, text in (
            ("SKILL.md", skill),
            ("python.md", python_backend),
            ("r.md", r_backend),
            ("qa-contract.md", qa),
        ):
            self.assertIn("audit_figure_collisions.py", text, relative)

        self.assertIn("blocks delivery", skill)
        self.assertIn("text–text", qa)
        self.assertIn("NOT AUDITABLE", qa)

    def test_dependency_docs_eval_and_release_version_are_connected(self) -> None:
        skill = read("skills/ieee-figure/SKILL.md")
        manifest = read("skills/ieee-figure/manifest.yaml")
        requirements = read("skills/ieee-figure/requirements.txt")
        evals = json.loads(read("skills/ieee-figure/evals/evals.json"))
        installer = read("scripts/update-codex-skills.sh")

        self.assertIn("version: 2.8.0", manifest)
        self.assertIn("PyMuPDF", requirements)
        self.assertIn("rendered_collision_auditor", manifest)
        self.assertIn("--expected-width-mm", skill)
        self.assertIn("ieee-figure/requirements.txt", installer)
        ids = {case["id"] for case in evals["evals"]}
        self.assertIn("rendered-collision-audit-is-mandatory", ids)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "cli" / "image2ppt" / "runtime"
sys.path.insert(0, str(RUNTIME))

import runtime_env  # noqa: E402


class RendererProbeTests(unittest.TestCase):
    def test_windows_powershell_without_powerpoint_is_not_ready(self) -> None:
        with (
            patch.object(runtime_env.platform, "system", return_value="Windows"),
            patch.object(runtime_env.shutil, "which", side_effect=lambda name: "powershell.exe" if "powershell" in name else None),
            patch.object(runtime_env.subprocess, "run", return_value=SimpleNamespace(returncode=1)),
        ):
            status = runtime_env.renderer_status()
        self.assertTrue(status["powerpoint_com_candidate"])
        self.assertFalse(status["powerpoint_com_ready"])
        self.assertFalse(status["ready"])
        self.assertEqual("missing", status["selection"])

    def test_successful_com_probe_marks_powerpoint_ready(self) -> None:
        with (
            patch.object(runtime_env.platform, "system", return_value="Windows"),
            patch.object(runtime_env.shutil, "which", side_effect=lambda name: "powershell.exe" if "powershell" in name else None),
            patch.object(runtime_env.subprocess, "run", return_value=SimpleNamespace(returncode=0)),
        ):
            status = runtime_env.renderer_status()
        self.assertTrue(status["powerpoint_com_ready"])
        self.assertTrue(status["ready"])
        self.assertEqual("powerpoint-com", status["selection"])

    def test_windows_filesystem_convert_is_not_reported_as_imagemagick(self) -> None:
        def which(name: str):
            if name == "convert":
                return r"C:\Windows\System32\convert.exe"
            return None

        with (
            patch.object(runtime_env.shutil, "which", side_effect=which),
            patch.object(
                runtime_env.subprocess,
                "run",
                return_value=SimpleNamespace(returncode=1, stdout="", stderr="Invalid syntax"),
            ),
        ):
            self.assertIsNone(runtime_env.imagemagick_executable())


if __name__ == "__main__":
    unittest.main()

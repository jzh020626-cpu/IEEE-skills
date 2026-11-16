#!/usr/bin/env python3
"""Offline IEEE skill metadata/resource validation (requires PyYAML)."""
from pathlib import Path
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    skills = sorted((root / "skills").glob("ieee-*"))
    for skill in skills:
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        try:
            text = entry.read_text(encoding="utf-8")
            match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", text, re.S)
            if not match:
                raise ValueError("missing YAML frontmatter")
            meta = yaml.safe_load(match.group(1))
            if meta.get("name") != skill.name or not str(meta.get("description", "")).strip():
                raise ValueError("name/description missing or directory mismatch")
            manifest = yaml.safe_load((skill / "manifest.yaml").read_text(encoding="utf-8"))
            if manifest.get("name") != skill.name:
                raise ValueError("manifest name mismatch")
            refs = list(manifest.get("always_load", []))
            for item in manifest.get("references", {}).get("on_demand", []):
                if isinstance(item, dict) and "path" in item:
                    refs.append(item["path"])
            for ref in refs:
                path = (skill / ref).resolve()
                if not path.is_relative_to((root / "skills").resolve()) or not path.is_file():
                    errors.append(f"{skill.name}: missing/escaping manifest reference {ref}")
            ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
            prompt = ui.get("interface", {}).get("default_prompt", "")
            if f"${skill.name}" not in prompt:
                errors.append(f"{skill.name}: UI prompt omits skill name")
        except (OSError, ValueError, TypeError, AttributeError, yaml.YAMLError) as exc:
            errors.append(f"{skill.name}: {exc}")
    plugin = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("skills") != "./skills/":
        errors.append("plugin: unexpected skills path")
    return skills, errors


if __name__ == "__main__":
    skills, errors = validate()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Validated {len(skills)} IEEE skill packages; {len(errors)} errors")
    raise SystemExit(bool(errors))

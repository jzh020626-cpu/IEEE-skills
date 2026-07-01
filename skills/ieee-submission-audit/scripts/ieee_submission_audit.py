#!/usr/bin/env python3
"""Offline strict IEEE Transactions manuscript audit.

The checker is intentionally conservative. It can prove simple textual facts in
LaTeX or extracted manuscript text, but it marks submission-system and compiled
PDF checks as manual unless the caller supplies those facts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


VENUE_LIMITS = {
    ("tii", "regular"): 10,
    ("tii", "review"): 12,
    ("tii", "letter"): 4,
    ("tac", "regular"): 16,
    ("tac", "full"): 16,
    ("tac", "technical-note"): 8,
    ("tac", "correspondence"): 8,
    ("tcst", "regular"): 16,
    ("tcst", "paper"): 16,
    ("tcst", "brief"): 8,
    ("tcst", "letter"): 4,
    ("tcns", "regular"): 12,
    ("tcns", "paper"): 12,
    ("tase", "regular"): 12,
    ("tase", "communication"): 6,
}

INDUSTRIAL_TERMS = re.compile(
    r"\b(industrial|industry|manufactur|factory|production|plant|process|IIoT|cyber-physical|CPS|smart grid|edge|cloud|PLC|SCADA|energy|reliability)\b",
    re.I,
)
CONTROL_TERMS = re.compile(r"\b(assumption|theorem|lemma|proof|stability|convergence|optimal|robust|Lyapunov|feasible|bounded)\b", re.I)
ROBOTICS_TERMS = re.compile(r"\b(robot|manipulator|mobile robot|AGV|UAV|trajectory|sensor|simulat|hardware|experiment|trial)\b", re.I)
COMM_TERMS = re.compile(r"\b(channel|latency|throughput|packet|delay|loss|wireless|network|bandwidth|reliability|AoI)\b", re.I)


@dataclass
class Check:
    id: str
    status: str
    severity: str
    message: str
    evidence: str = ""


def read_input(path: str | None) -> tuple[str, str]:
    if path:
        p = Path(path)
        return p.read_text(encoding="utf-8", errors="replace"), p.suffix.lower()
    return sys.stdin.read(), ""


def has(pattern: str, text: str, flags: int = re.I | re.S) -> bool:
    return bool(re.search(pattern, text, flags))


def extract_abstract(text: str) -> str:
    m = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", text, re.I | re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r"\bAbstract\b\s*[-.:]?\s*(.*?)(?:\n\s*(?:Index Terms|Keywords|I\.|1\.|Introduction)\b)", text, re.I | re.S)
    if m:
        return m.group(1).strip()
    return ""


def extract_ntp(text: str) -> str:
    patterns = [
        r"\\section\*?\{Note to Practitioners\}(.*?)(?:\\section|\\begin\{IEEEkeywords\}|\bIndex Terms\b|\bI\.?\s+Introduction\b)",
        r"\bNote to Practitioners\b\s*[-.:]?\s*(.*?)(?:\n\s*(?:Index Terms|Keywords|I\.|1\.|Introduction|Abstract)\b)",
    ]
    for pattern in patterns:
        m = re.search(pattern, text, re.I | re.S)
        if m:
            return m.group(1).strip()
    return ""


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'-]*", text))


def add(checks: list[Check], id_: str, status: str, severity: str, message: str, evidence: str = "") -> None:
    checks.append(Check(id_, status, severity, message, evidence))


def audit(text: str, suffix: str, venue: str, paper_type: str, pages: int | None, stage: str, conference_extension: bool) -> dict[str, object]:
    checks: list[Check] = []
    venue = venue.lower()
    paper_type = paper_type.lower()
    is_latex = suffix in {".tex", ".ltx"} or "\\documentclass" in text

    if is_latex:
        if has(r"\\documentclass(?:\[[^\]]*\])?\{IEEEtran\}", text):
            add(checks, "format.ieeetran", "pass", "blocker", "IEEEtran document class detected.")
        else:
            add(checks, "format.ieeetran", "fail", "blocker", "LaTeX source does not show IEEEtran document class.")
    else:
        add(checks, "format.ieeetran", "manual", "blocker", "Cannot prove IEEEtran/double-column format from plain text; inspect source or compiled PDF.")

    abstract = extract_abstract(text)
    if abstract:
        add(checks, "front.abstract", "pass", "blocker", "Abstract detected.", f"{word_count(abstract)} words")
        bad_abs = []
        if has(r"\\cite\{|(?<!\w)\[\d+(?:[-,]\s*\d+)*\]", abstract):
            bad_abs.append("numbered citation")
        if has(r"\\begin\{equation\}|\\\(|\\\[|\$\$", abstract):
            bad_abs.append("displayed/numbered equation marker")
        if has(r"\\footnote\{|footnote", abstract):
            bad_abs.append("footnote")
        if bad_abs:
            add(checks, "front.abstract_clean", "fail", "blocker", "Abstract contains IEEE-prohibited material: " + ", ".join(bad_abs) + ".")
        else:
            add(checks, "front.abstract_clean", "pass", "blocker", "Abstract has no obvious numbered citations, displayed equations, or footnotes.")
    else:
        add(checks, "front.abstract", "fail", "blocker", "No Abstract detected.")

    if has(r"\\begin\{IEEEkeywords\}|\\begin\{IEEEindexterms\}|\bIndex Terms\b", text):
        add(checks, "front.index_terms", "pass", "blocker", "Index Terms detected.")
    else:
        add(checks, "front.index_terms", "fail", "blocker", "Index Terms not detected.")

    numeric_cites = has(r"\\cite\{|(?<!\w)\[\d+(?:\s*[-,]\s*\d+)*\]", text)
    author_year = has(r"\([A-Z][A-Za-z-]+(?:\s+et\s+al\.)?,\s*(?:19|20)\d{2}\)", text)
    if numeric_cites and not author_year:
        add(checks, "refs.numeric", "pass", "blocker", "IEEE numeric citation markers detected.")
    elif author_year:
        add(checks, "refs.numeric", "fail", "blocker", "Author-year citation pattern detected; IEEE Transactions requires numeric citation style.")
    else:
        add(checks, "refs.numeric", "manual", "blocker", "No citation markers detected; inspect references and citation ordering.")

    if has(r"\\bibliography\{|\\begin\{thebibliography\}|\bReferences\b", text):
        add(checks, "refs.section", "pass", "major", "Reference section or bibliography command detected.")
    else:
        add(checks, "refs.section", "manual", "major", "Reference section not detected in supplied text.")

    if pages is None:
        add(checks, "pages.compiled", "manual", "blocker", "Compiled IEEE-format page count not supplied; run with --compiled-pages after PDF build.")
    else:
        limit = VENUE_LIMITS.get((venue, paper_type)) or VENUE_LIMITS.get((venue, "regular"))
        if limit and pages > limit:
            add(checks, "pages.limit", "fail", "blocker", f"{venue.upper()} {paper_type} page count {pages} exceeds strict audit limit {limit}.")
        elif limit:
            add(checks, "pages.limit", "pass", "blocker", f"Compiled pages {pages} within strict audit limit {limit}.")
        else:
            add(checks, "pages.limit", "manual", "blocker", f"No embedded page limit for venue={venue}, paper_type={paper_type}; verify current journal page.")

    bad_graphics = sorted(set(re.findall(r"[\w./-]+\.(?:gif|bmp|jpg|jpeg)", text, re.I)))
    if bad_graphics:
        add(checks, "figures.formats", "fail", "major", "Potential non-preferred graphics formats detected; IEEE graphics should use PS/EPS/PDF/PNG/TIFF, with JPEG reserved for author photos.", ", ".join(bad_graphics[:8]))
    elif has(r"\.(?:eps|pdf|png|tiff?|ps)\b|\\includegraphics|Fig\.|Figure", text):
        add(checks, "figures.formats", "manual", "major", "Figures detected; verify final files are PS/EPS/PDF/PNG/TIFF and readable at column width.")
    else:
        add(checks, "figures.formats", "manual", "major", "No figure evidence detected; verify whether the manuscript needs figures/tables.")

    if venue == "tase":
        ntp = extract_ntp(text)
        if not ntp:
            add(checks, "tase.ntp", "fail", "blocker", "T-ASE target requires a distinct Note to Practitioners; none detected.")
        else:
            wc = word_count(ntp)
            status = "pass" if 100 <= wc <= 300 else "fail"
            add(checks, "tase.ntp", status, "blocker", f"Note to Practitioners detected with {wc} words; strict target is 100-300 words.")
        if stage == "initial" and has(r"\\author\{|@|Acknowledg|affiliation|thanks\{", text):
            add(checks, "tase.anonymity", "fail", "blocker", "Initial T-ASE audit found author-identifying markers; check double-anonymous hygiene.")
        else:
            add(checks, "tase.anonymity", "manual", "blocker", "Confirm double-anonymous files, supplements, and metadata in the submission system.")
        if has(r"quality|robust|stability|productivity|efficiency|optimal|convergence|complexity|verification|reliability", text):
            add(checks, "tase.automation_evidence", "pass", "major", "Automation-science evaluation terms detected.")
        else:
            add(checks, "tase.automation_evidence", "fail", "major", "T-ASE automation issues such as robustness, stability, efficiency, complexity, or reliability are not visible.")

    if venue == "tii":
        if INDUSTRIAL_TERMS.search(text):
            add(checks, "tii.scope", "pass", "blocker", "Industrial informatics relevance terms detected.")
        else:
            add(checks, "tii.scope", "fail", "blocker", "TII scope is not explicit; add industrial system model, constraints, and validation relevance.")

    if venue in {"tac", "tcst", "tcns"}:
        if venue == "tac" and CONTROL_TERMS.search(text):
            add(checks, "tac.theory", "pass", "major", "Control-theory assumptions/proof/stability terms detected.")
        elif venue == "tac":
            add(checks, "tac.theory", "fail", "major", "TAC audit needs visible assumptions, theorem/proof, stability, convergence, or robustness logic.")
        if venue == "tcst" and has(r"design|realization|operation|implementation|application|hardware|experiment|platform", text):
            add(checks, "tcst.technology", "pass", "major", "Technology/application evidence detected.")
        elif venue == "tcst":
            add(checks, "tcst.technology", "fail", "major", "TCST audit needs concrete control-system implementation/application evidence.")
        if venue == "tcns" and has(r"network|interconnected|graph|distributed|multi-agent|communication", text):
            add(checks, "tcns.networked", "pass", "major", "Networked/interconnected system evidence detected.")
        elif venue == "tcns":
            add(checks, "tcns.networked", "fail", "major", "TCNS audit needs explicit networked/interconnected system model.")

    if ROBOTICS_TERMS.search(text):
        if has(r"baseline|ablation|trial|seed|simulat|hardware|failure|statistical", text):
            add(checks, "evidence.robotics", "pass", "major", "Robotics experiment evidence terms detected.")
        else:
            add(checks, "evidence.robotics", "manual", "major", "Robotics topic detected; verify baselines, ablations, trials/seeds, and failure cases.")
    if COMM_TERMS.search(text):
        if has(r"latency|throughput|packet|loss|delay|reliability|overhead|robust", text):
            add(checks, "evidence.communications", "pass", "major", "Communications/network constraint evidence terms detected.")
        else:
            add(checks, "evidence.communications", "manual", "major", "Communication topic detected; verify channel/network model and latency/throughput/reliability metrics.")

    if has(r"code|github|dataset|data|seed|log|configuration|parameter|ROS bag|model weight|reproduc", text):
        add(checks, "repro.package", "pass", "major", "Reproducibility artifact terms detected.")
    else:
        add(checks, "repro.package", "manual", "major", "No reproducibility package evidence detected; verify code/data/seeds/logs/hardware/simulation records.")

    if conference_extension or has(r"conference version|preliminary version|extended from|CDC|ICRA|IROS|CASE|ACC", text):
        if has(r"additional|new proof|new experiment|extended|substantially|conference version|preliminary version", text):
            add(checks, "extension.value", "manual", "blocker", "Conference-extension markers detected; verify prior version citation and added archival value.")
        else:
            add(checks, "extension.value", "fail", "blocker", "Conference-extension case needs explicit prior-version citation and added archival value.")

    fail_blockers = [c for c in checks if c.status == "fail" and c.severity == "blocker"]
    fails = [c for c in checks if c.status == "fail"]
    manuals = [c for c in checks if c.status == "manual"]
    if fail_blockers:
        gate = "No-Go"
    elif fails or manuals:
        gate = "Conditional Go"
    else:
        gate = "Go"
    return {"gate": gate, "checks": [asdict(c) for c in checks]}


def render_text(result: dict[str, object]) -> str:
    checks = result["checks"]
    assert isinstance(checks, list)
    lines = [f"GATE: {result['gate']}", ""]
    for label, statuses in [
        ("BLOCKERS", {("fail", "blocker")}),
        ("FIX BEFORE SUBMISSION", {("fail", "major"), ("fail", "minor")}),
        ("MANUAL CONFIRMATION", {("manual", "blocker"), ("manual", "major"), ("manual", "minor")}),
        ("PASSED", {("pass", "blocker"), ("pass", "major"), ("pass", "minor")}),
    ]:
        lines.append(f"{label}:")
        matched = [
            c for c in checks
            if (str(c["status"]), str(c["severity"])) in statuses
        ]
        if not matched:
            lines.append("- None")
        for c in matched:
            evidence = f" ({c['evidence']})" if c.get("evidence") else ""
            lines.append(f"- {c['id']}: {c['message']}{evidence}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Strict offline IEEE Transactions submission audit.")
    parser.add_argument("input", nargs="?", help="Manuscript .tex/.txt file. Reads stdin when omitted.")
    parser.add_argument("--venue", choices=["generic", "tase", "tii", "tac", "tcst", "tcns", "tro", "ral"], default="generic")
    parser.add_argument("--paper-type", default="regular", help="regular, full, paper, brief, letter, communication, review, technical-note, correspondence")
    parser.add_argument("--stage", choices=["initial", "revision", "final"], default="initial")
    parser.add_argument("--compiled-pages", type=int, help="Compiled IEEE-format PDF page count.")
    parser.add_argument("--conference-extension", action="store_true", help="Treat as an extension of a conference paper.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args(argv)

    text, suffix = read_input(args.input)
    result = audit(text, suffix, args.venue, args.paper_type, args.compiled_pages, args.stage, args.conference_extension)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Segment manuscript claims, search IEEE-first citation candidates with Crossref,
and export selected references as ENW, RIS, or Zotero RDF.

This helper is intentionally conservative: it ranks likely support and filters
for archival IEEE venues, but it never claims a citation supports a manuscript
claim without human review.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape as xml_escape

CROSSREF_API = "https://api.crossref.org/works"
USER_AGENT = "codex-ieee-citation/1.0 (mailto:unknown@example.com)"
EXPORT_FORMATS = ("enw", "ris", "zotero-rdf", "rdf")

IEEE_JOURNALS: dict[str, set[str]] = {
    "tase": {
        "IEEE Transactions on Automation Science and Engineering",
    },
    "tii": {
        "IEEE Transactions on Industrial Informatics",
    },
    "tac": {
        "IEEE Transactions on Automatic Control",
    },
    "tcst": {
        "IEEE Transactions on Control Systems Technology",
    },
    "tro": {
        "IEEE Transactions on Robotics",
    },
    "ral": {
        "IEEE Robotics and Automation Letters",
    },
    "tie": {
        "IEEE Transactions on Industrial Electronics",
    },
    "twc": {
        "IEEE Transactions on Wireless Communications",
    },
    "tcom": {
        "IEEE Transactions on Communications",
    },
    "iotj": {
        "IEEE Internet of Things Journal",
    },
    "robotics": {
        "IEEE Transactions on Automation Science and Engineering",
        "IEEE Transactions on Robotics",
        "IEEE Robotics and Automation Letters",
        "IEEE/ASME Transactions on Mechatronics",
        "IEEE Transactions on Intelligent Transportation Systems",
        "IEEE Transactions on Cybernetics",
        "IEEE Transactions on Systems, Man, and Cybernetics: Systems",
    },
    "control": {
        "IEEE Transactions on Automatic Control",
        "IEEE Transactions on Control Systems Technology",
        "IEEE Transactions on Automation Science and Engineering",
        "IEEE Transactions on Cybernetics",
        "IEEE Transactions on Systems, Man, and Cybernetics: Systems",
        "IEEE Control Systems Letters",
    },
    "communications": {
        "IEEE Transactions on Wireless Communications",
        "IEEE Transactions on Communications",
        "IEEE Internet of Things Journal",
        "IEEE Transactions on Network Science and Engineering",
        "IEEE Transactions on Mobile Computing",
        "IEEE Transactions on Vehicular Technology",
        "IEEE Transactions on Signal Processing",
    },
    "industrial": {
        "IEEE Transactions on Industrial Informatics",
        "IEEE Transactions on Industrial Electronics",
        "IEEE Transactions on Automation Science and Engineering",
        "IEEE Transactions on Smart Grid",
        "IEEE Internet of Things Journal",
        "IEEE Transactions on Reliability",
    },
}
IEEE_JOURNALS["all"] = set().union(*IEEE_JOURNALS.values())
IEEE_JOURNALS["ieee"] = IEEE_JOURNALS["all"]

VENUE_ALIASES = {
    "IEEE Trans. Automat. Sci. Eng.": "IEEE Transactions on Automation Science and Engineering",
    "IEEE Trans. Ind. Informat.": "IEEE Transactions on Industrial Informatics",
    "IEEE Trans. Robot.": "IEEE Transactions on Robotics",
    "IEEE Robot. Autom. Lett.": "IEEE Robotics and Automation Letters",
    "IEEE Trans. Automat. Control": "IEEE Transactions on Automatic Control",
    "IEEE Trans. Control Syst. Technol.": "IEEE Transactions on Control Systems Technology",
    "IEEE Trans. Ind. Electron.": "IEEE Transactions on Industrial Electronics",
    "IEEE Trans. Wireless Commun.": "IEEE Transactions on Wireless Communications",
    "IEEE Trans. Commun.": "IEEE Transactions on Communications",
}

STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "are", "was", "were", "into",
    "using", "based", "between", "under", "over", "through", "paper", "method", "system",
    "results", "show", "proposed", "approach", "model", "algorithm",
}

@dataclass
class Segment:
    id: str
    text: str
    query: str
    order: int

@dataclass
class Candidate:
    title: str
    journal: str
    year: str
    doi: str
    url: str
    volume: str
    issue: str
    pages: str
    authors: list[str]
    score: float
    scope: str

    @property
    def key(self) -> str:
        return self.doi.lower() if self.doi else f"{self.title.lower()}|{self.journal.lower()}"


def clean_text(value: Any) -> str:
    if isinstance(value, list):
        value = " ".join(str(v) for v in value)
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalize_journal(journal: str) -> str:
    journal = clean_text(journal)
    return VENUE_ALIASES.get(journal, journal)


def words(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9-]{2,}", text) if w.lower() not in STOPWORDS]


def make_query(text: str, max_terms: int = 10) -> str:
    seen: list[str] = []
    for w in words(text):
        if w not in seen:
            seen.append(w)
        if len(seen) >= max_terms:
            break
    return " ".join(seen) or text[:120]


def segment_text(text: str) -> list[Segment]:
    chunks = [c.strip() for c in re.split(r"\n\s*\n|(?<=[.;])\s+(?=[A-Z])", text) if c.strip()]
    if not chunks and text.strip():
        chunks = [text.strip()]
    segments: list[Segment] = []
    for i, chunk in enumerate(chunks, 1):
        sid = hashlib.sha1(chunk.encode("utf-8")).hexdigest()[:8]
        segments.append(Segment(f"S{i:03d}-{sid}", chunk, make_query(chunk), i))
    return segments


def in_scope(journal: str, scope: str) -> bool:
    journal = normalize_journal(journal)
    if scope == "all":
        allowed = IEEE_JOURNALS["all"]
    else:
        allowed = IEEE_JOURNALS.get(scope, IEEE_JOURNALS["all"])
    if journal in allowed:
        return True
    return journal.startswith("IEEE Transactions on ") or journal.startswith("IEEE Journal of ")


def candidate_scope(journal: str) -> str:
    journal = normalize_journal(journal)
    hits = [scope for scope, journals in IEEE_JOURNALS.items() if scope != "all" and journal in journals]
    return ",".join(hits) if hits else ("ieee" if journal.startswith("IEEE") else "")


def crossref_get(url: str, timeout: int = 20) -> dict[str, Any]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def search_crossref(query: str, rows: int, polite: float) -> list[dict[str, Any]]:
    params = {"query.bibliographic": query, "rows": str(rows), "sort": "relevance", "order": "desc"}
    url = f"{CROSSREF_API}?{urlencode(params)}"
    try:
        data = crossref_get(url)
    except (URLError, TimeoutError, OSError) as exc:
        print(f"warning: Crossref search failed for query {query!r}: {exc}", file=sys.stderr)
        return []
    if polite:
        time.sleep(polite)
    return data.get("message", {}).get("items", [])


def author_name(author: dict[str, Any]) -> str:
    family = clean_text(author.get("family"))
    given = clean_text(author.get("given"))
    if family and given:
        return f"{family}, {given}"
    return family or given or clean_text(author.get("name"))


def year_from(item: dict[str, Any]) -> str:
    for key in ["published-print", "published-online", "published", "issued"]:
        parts = item.get(key, {}).get("date-parts") or []
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def pages_from(item: dict[str, Any]) -> str:
    page = clean_text(item.get("page"))
    if page:
        return page
    return clean_text(item.get("article-number"))


def score_item(segment: Segment, item: dict[str, Any]) -> float:
    title = clean_text(item.get("title"))
    abstract = clean_text(re.sub(r"<[^>]+>", " ", clean_text(item.get("abstract"))))
    hay = set(words(f"{title} {abstract}"))
    needle = set(words(segment.text))
    overlap = len(hay & needle)
    return overlap / max(len(needle), 1)


def to_candidate(segment: Segment, item: dict[str, Any]) -> Candidate:
    journal = normalize_journal((item.get("container-title") or [""])[0])
    return Candidate(
        title=clean_text(item.get("title")),
        journal=journal,
        year=year_from(item),
        doi=clean_text(item.get("DOI")),
        url=clean_text(item.get("URL")),
        volume=clean_text(item.get("volume")),
        issue=clean_text(item.get("issue")),
        pages=pages_from(item),
        authors=[author_name(a) for a in item.get("author", []) if author_name(a)],
        score=score_item(segment, item),
        scope=candidate_scope(journal),
    )


def find_candidates(segment: Segment, scope: str, rows: int, polite: float) -> list[Candidate]:
    candidates: list[Candidate] = []
    for item in search_crossref(segment.query, rows, polite):
        cand = to_candidate(segment, item)
        if cand.title and in_scope(cand.journal, scope):
            candidates.append(cand)
    candidates.sort(key=lambda c: c.score, reverse=True)
    return candidates


def dedupe(candidates: list[Candidate]) -> list[Candidate]:
    seen: set[str] = set()
    out: list[Candidate] = []
    for c in candidates:
        if c.key in seen:
            continue
        seen.add(c.key)
        out.append(c)
    return out


def write_enw(candidates: list[Candidate], path: Path) -> None:
    lines: list[str] = []
    for c in candidates:
        lines.append("%0 Journal Article")
        for a in c.authors:
            lines.append(f"%A {a}")
        if c.year: lines.append(f"%D {c.year}")
        if c.title: lines.append(f"%T {c.title}")
        if c.journal: lines.append(f"%J {c.journal}")
        if c.volume: lines.append(f"%V {c.volume}")
        if c.issue: lines.append(f"%N {c.issue}")
        if c.pages: lines.append(f"%P {c.pages}")
        if c.doi: lines.append(f"%R {c.doi}")
        if c.url or c.doi: lines.append(f"%U {c.url or 'https://doi.org/' + c.doi}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_ris(candidates: list[Candidate], path: Path) -> None:
    lines: list[str] = []
    for c in candidates:
        lines.append("TY  - JOUR")
        for a in c.authors:
            lines.append(f"AU  - {a}")
        if c.year: lines.append(f"PY  - {c.year}")
        if c.title: lines.append(f"TI  - {c.title}")
        if c.journal: lines.append(f"JO  - {c.journal}")
        if c.volume: lines.append(f"VL  - {c.volume}")
        if c.issue: lines.append(f"IS  - {c.issue}")
        if c.pages: lines.append(f"SP  - {c.pages}")
        if c.doi: lines.append(f"DO  - {c.doi}")
        if c.url or c.doi: lines.append(f"UR  - {c.url or 'https://doi.org/' + c.doi}")
        lines.append("ER  -")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_rdf(candidates: list[Candidate], path: Path) -> None:
    items = ['<?xml version="1.0" encoding="UTF-8"?>', '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:prism="http://prismstandard.org/namespaces/1.2/basic/">']
    for c in candidates:
        about = html.escape(c.url or (f"https://doi.org/{c.doi}" if c.doi else c.key))
        items.append(f'  <rdf:Description rdf:about="{about}">')
        items.append(f"    <dc:title>{xml_escape(c.title)}</dc:title>")
        items.append(f"    <prism:publicationName>{xml_escape(c.journal)}</prism:publicationName>")
        if c.year: items.append(f"    <prism:publicationDate>{xml_escape(c.year)}</prism:publicationDate>")
        if c.doi: items.append(f"    <prism:doi>{xml_escape(c.doi)}</prism:doi>")
        for a in c.authors:
            items.append(f"    <dc:creator>{xml_escape(a)}</dc:creator>")
        items.append("  </rdf:Description>")
    items.append("</rdf:RDF>")
    path.write_text("\n".join(items), encoding="utf-8")


def write_report(mapping: list[dict[str, Any]], path: Path, refs_path: Path) -> None:
    lines = ["# IEEE Citation Support Report", "", f"Reference export: `{refs_path.name}`", "", "Use the suggested `[n]` placeholders as placement hints; assign final numbers after importing and ordering references in the manuscript.", ""]
    for row in mapping:
        seg = row["segment"]
        cand = row.get("candidate")
        lines.append(f"## {seg['id']}")
        lines.append("")
        lines.append(seg["text"])
        lines.append("")
        if cand:
            lines.append(f"- Suggested placement: `[n]` after the supported claim")
            lines.append(f"- Candidate: {cand['title']} ({cand['journal']}, {cand['year']})")
            lines.append(f"- DOI: {cand['doi'] or 'n/a'}")
            lines.append(f"- Support score: {cand['score']:.2f}")
        else:
            lines.append("- No in-scope IEEE-first candidate found; broaden scope or revise the query.")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def candidate_dict(c: Candidate) -> dict[str, Any]:
    return c.__dict__


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Search IEEE-first citation candidates and export ENW/RIS/Zotero RDF.")
    parser.add_argument("input", nargs="?", help="Input manuscript text file. Reads stdin when omitted.")
    parser.add_argument("--scope", choices=sorted(IEEE_JOURNALS), default="all")
    parser.add_argument("--format", choices=EXPORT_FORMATS, default="enw")
    parser.add_argument("--output", default="ieee_references.enw")
    parser.add_argument("--report", default="ieee_citation_report.md")
    parser.add_argument("--json", dest="json_path", default="ieee_citation_candidates.json")
    parser.add_argument("--rows", type=int, default=30)
    parser.add_argument("--top-k", type=int, default=1)
    parser.add_argument("--polite-delay", type=float, default=0.2)
    parser.add_argument("--no-report", action="store_true")
    parser.add_argument("--no-json", action="store_true")
    args = parser.parse_args(argv)

    text = Path(args.input).read_text(encoding="utf-8") if args.input else sys.stdin.read()
    segments = segment_text(text)
    all_refs: list[Candidate] = []
    mapping: list[dict[str, Any]] = []
    for segment in segments:
        hits = find_candidates(segment, args.scope, args.rows, args.polite_delay)
        chosen = hits[: max(args.top_k, 1)]
        all_refs.extend(chosen)
        mapping.append({
            "segment": segment.__dict__,
            "candidate": candidate_dict(chosen[0]) if chosen else None,
            "candidates": [candidate_dict(c) for c in hits[: args.top_k]],
        })
    refs = dedupe(all_refs)
    output = Path(args.output)
    if args.format == "ris":
        write_ris(refs, output)
    elif args.format in {"zotero-rdf", "rdf"}:
        write_rdf(refs, output)
    else:
        write_enw(refs, output)
    if not args.no_report:
        write_report(mapping, Path(args.report), output)
    if not args.no_json:
        Path(args.json_path).write_text(json.dumps({"segments": mapping, "references": [candidate_dict(c) for c in refs]}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"segments={len(segments)} references={len(refs)} output={output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

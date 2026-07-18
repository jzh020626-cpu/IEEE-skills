---
name: ieee-paper-to-patent
description: >-
  Convert engineering papers, theses, technical reports, source code, figures, inventor notes, or research manuscripts into evidence-grounded Chinese invention patent drafts and attorney-facing technical disclosures. Use to mine patent points, draft or revise a Chinese technical disclosure (技术交底书), run prior-art comparison, convert Office project materials, map claimed features to evidence, preserve formulas as editable Office Math, generate claim-aligned figures, compare a paper with an existing patent, audit support, or deliver Chinese DOCX patent/disclosure files for robotics, control, communications, automation, algorithms, and systems.
---

# Engineering Paper to Chinese Patent

Use this file as the router. Do not draft an application from only the abstract or contribution list.

## 1. Load and route

Read `manifest.yaml` and every `always_load` path. Detect and state:

- `source_format`: selectable PDF, scanned PDF, pasted text, or mixed project;
- `task_mode`: full draft, claim set, disclosure analysis, technical disclosure, disclosure iteration, or paper-patent audit;
- `invention_type`: algorithm/software, apparatus/system, process/material, or mixed.

Load only the matching fragments and conditionally needed references.

## 2. Preserve source grounding

Create stable source IDs: `P001...` for prose, `E001...` for equations, `F001...` for figures, and `C001...` for code/supplement evidence. Map every material claim feature to source IDs with one support state: `explicit`, `inherent`, `needs-confirmation`, or `unsupported`. Exclude unsupported features from formal claims.

Never infer inventorship, ownership, unpublished implementation, publication dates, prior-art conclusions, or legal sufficiency. Use `[TO CONFIRM: specific question]` outside formal claims.

## 3. Use stage gates

For formal-draft modes, follow `static/core/workflow.md` in order and persist its intermediate artifacts. Do not draft formal claims before the source map, terminology ledger, inventories, evidence ledger, and invention concept pass their gates.

For `technical-disclosure`, follow `static/fragments/task/technical-disclosure.md`. For `disclosure-iteration`, preserve the existing draft and follow `static/fragments/task/disclosure-iteration.md`.

Draft claims first for a full application, then align the specification, figures, embodiments, and abstract to claim terminology and step order.

## 4. Produce and validate

Formal application deliverables are Chinese claims, specification, abstract, abstract figure, and figure descriptions. For algorithmic inventions, retain source-supported core formulas, define symbols, explain technical operations, and render visible formulas as editable Office Math in DOCX.

For formal packages run:

```bash
python scripts/validate_patent_draft.py draft.json
python scripts/build_patent_package.py draft.json --output-dir outputs --prefix patent
```

Resolve all `ERROR` findings and review warnings against the source. For disclosures, run `references/disclosure/disclosure_self_check.md` and the needed tools under `scripts/disclosure/`; deliver timestamped Markdown and matching DOCX.

This output is a drafting aid for inventor and patent-professional review, not a patentability, infringement, or filing opinion.

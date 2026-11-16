---
name: ieee-paper2word
description: Export engineering Markdown manuscripts to editable Word documents, or extract formatting requirements from supplied templates and reference documents. Use for IEEE manuscript Word formatting, native equations, tables, numbered references and reference-layout inspection; not manuscript rewriting or slide creation.
license: MIT
---

# IEEE Paper to Word

Prepare an editable document while preserving the source manuscript, equations, technical claims and citation identity. A matching appearance does not establish journal compliance.

## Workflow

1. Identify the source, output path and reference/template roles. Inspect written formatting requirements separately from example layout. Read `references/format-requirements.md` for written/PDF/image rules or `references/reference-layout.md` for example DOCX formatting. Use `scripts/reference_layout.py --help` for paragraph-sample extraction.
2. Prefer a supplied current IEEE Word template or the named journal's official template. Keep numbered IEEE references. Verify the required article type, anonymity, title/abstract structure, columns, captions and T-ASE Note to Practitioners placement when relevant. Never infer a journal rule from a sample paper alone.
3. For Markdown compilation, check `md-to-word --version` and read the installed engine's `md-to-word --contract`. The optional engine is `md-to-word-docx`; report or install it only within the user's authorized environment setup. Do not silently change a Python environment during ordinary formatting. If unavailable, use an available document tool with the template or explain the missing capability.
4. Build an explicit requirements file from verified IEEE/user requirements and pass `-r`; set an explicit IEEE numeric CSL or supplied style. Do not use the engine's implicit English publication preset or implicit APA/GB citation defaults as IEEE formatting. Check supported column and template capabilities; if essential features are unsupported, use another document workflow and report the limitation. Avoid inventing engine options: inspect its actual contract.
5. Normalize a working copy to the engine contract, including native OMML equations, labels and reference keys. Preserve original Markdown and media. Never write output over source, including same-file aliases. Mark missing bibliography or unresolved cross-references instead of fabricating them.
6. Export with `md-to-word manuscript.md -r format.txt -o manuscript.docx` when using that engine. Validate all math, symbols, table content, figures, reference order and cross-references after export. Render and inspect every page with available document tooling; inspect columns, page breaks, clipping and final-size readability. Iterate before delivery.
7. Deliver the DOCX, any requested working source, requirements provenance and known limitations. Claim submission readiness only after the target venue checks and rendered QA pass. Do not promise byte-identical output without measuring it for the actual engine/version.

## Boundaries

A local paragraph or layout inspection does not require a complete submission package. Preserve existing text unless editing was requested. Image/OCR-derived requirements need visual verification. Read `../ieee-shared/core/ieee-transactions-contract.md` for manuscript-facing constraints. The external export engine is not bundled or validated by installing this skill; keep its MIT source notice in `UPSTREAM-LICENSE.txt`.

---
name: ieee-paper2ppt
description: >-
  Build a complete IEEE-style Chinese PPTX presentation from a robotics, automation, control, communications, industrial informatics, or related engineering paper. Use for journal club, group meeting, literature report, thesis seminar, conference or defense decks, and requests to improve weak paper-to-PPT output with clipped figures, loose alignment, obvious AI-style wording, or heavy manual rework. It classifies the paper, builds an evidence-led story, creates the actual .pptx, and runs corrective QA for complete figure crops, stable alignment, text overflow, and de-templated Chinese academic expression.
---

# IEEE Paper-to-PPTX Router

Use the static/dynamic routing in `manifest.yaml`; the deliverable is a real `.pptx`, not only an outline.

## Routing protocol

1. Read `manifest.yaml` and every `always_load` path.
2. Classify the paper into the closest `paper_type` arc and state it briefly.
3. Load only that arc, then build a terminology ledger while reading the source.
4. Follow the nine-step workflow: extract source facts, select an argument, plan visual rhythm, select evidence figures, prepare/crop assets, draft Chinese slide content and notes, build the PPTX, run corrective self-review, and verify.
5. Load design, figure-asset, and self-review references only when their stage is reached.
6. When a real PPTX exists, run `scripts/audit_pptx_quality.py` after the first draft and again after revision. High-severity findings block delivery.

## Rules

- Tell the paper through problem, gap, method/theory/system design, evidence, limitations, and takeaway; do not merely mirror section headings.
- Use only figures needed for the argument. Preserve axes, legends, panel labels, scale bars, method labels, and table headers.
- Use source-specific Chinese and avoid generic AI summary slogans.
- Do not fabricate results, numbers, citations, figure contents, author claims, or speaker-note details.
- Record asset provenance and QA results in the output package.

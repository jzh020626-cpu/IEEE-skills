---
name: ieee-literature-pipeline
description: >-
  Automated literature discovery pipeline for IEEE-style research: multi-source search, six-dimensional scoring, topic clustering, intensive-reading notes, and local archive updates for robotics, automation, control, communications, and industrial informatics.
---

# IEEE Literature Pipeline

## Workflow

- Score papers by relevance, technical novelty, evidence strength, venue quality, recency, and usefulness for the manuscript section.
- Output concise reading queues and claim-linked notes rather than broad summaries.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../ieee-shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.

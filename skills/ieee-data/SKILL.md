---
name: ieee-data
description: >-
  Prepare, audit, or revise IEEE-style reproducibility packages, code/data availability notes, experiment logs, parameter tables, simulation seeds, hardware settings, ROS bags, model weights, and artifact documentation for robotics, control, communications, and industrial informatics manuscripts.
---

# IEEE Reproducibility Package Router

Use `manifest.yaml` to load the core workflow and only the references needed for the request.

## Routing protocol

1. Read `manifest.yaml` and every path under `always_load`.
2. Identify the target journal/article type, user language, and requested task: audit, draft, repository plan, artifact inventory, or full reproducibility package.
3. Inventory every artifact supporting the claims: code, datasets, preprocessing, configs, seeds, checkpoints, logs, simulation models, hardware/firmware, ROS bags, packet traces, calibration, environment files, and exact run commands.
4. Classify access separately for each artifact: public repository, controlled access, institutional/proprietary restriction, third-party source, within-paper/supplement, justified request route, or unavailable.
5. Choose repositories, identifiers, versioning, licensing, and release timing before drafting statements.
6. Draft explicit artifact-to-location mappings and formal dataset/software citations where supported.
7. Audit the package for provenance, checksums, environment capture, parameter completeness, independent repetitions, and result-to-artifact traceability.
8. Return ready-to-paste text plus unresolved factual fields.

## IEEE operating rules

- The named journal's current author instructions override generic IEEE guidance.
- Convert vague availability language into concrete repository, commit/tag, license, identifier, dataset, config, seed, hardware/software version, and reproduction-command fields.
- Keep data availability, code availability, supplementary material, and reproducibility instructions distinct when the venue treats them separately.
- Do not promise public release, access approval, proprietary logs, identifiers, licences, embargo dates, or hardware records unless supplied.
- Use `AUTHOR_INPUT_NEEDED` for missing facts and `ieee-experiment-log` when raw runs need normalization before packaging.

---
name: ieee-data
description: >-
  Prepare, audit, or revise IEEE-style reproducibility packages, code/data availability notes, experiment logs, parameter tables, simulation seeds, hardware settings, ROS bags, model weights, and artifact documentation for robotics, control, communications, and industrial informatics manuscripts.
---

# IEEE Reproducibility Package

## Workflow

- Convert vague availability text into concrete artifacts: repository, commit/tag, license, datasets, configs, seeds, hardware, software versions, and exact reproduction commands.
- Do not promise public release, hardware logs, or proprietary data access unless the source explicitly supports it.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.

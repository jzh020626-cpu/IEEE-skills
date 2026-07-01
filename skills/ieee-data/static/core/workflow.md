# Workflow and output format

## Workflow

1. Identify target venue, article type, and whether the paper is theoretical, simulation-only, hardware-based, dataset-based, or mixed.
2. Inventory artifacts behind every main result: raw data, processed data, figure/table data, simulation configs, controller parameters, network/channel settings, random seeds, code, model weights, logs, videos, hardware settings, and supplementary derivations.
3. Classify each artifact into one access route: `public repository`, `IEEE Xplore supplementary material`, `IEEE DataPort`, `institutional repository`, `private reviewer link`, `third-party restricted`, `hardware-only / cannot share`, `available on justified request`, or `not applicable`.
4. Decide repository and identifier strategy before drafting text. Prefer DOI, release tag, commit hash, accession, or stable repository record over personal websites and temporary cloud links.
5. Draft the IEEE reproducibility package statement using artifact-to-location mapping.
6. Add exact reproduction commands or a command manifest when source material provides them.
7. Run the engineering metadata audit before finalizing.
8. Return ready-to-paste text plus unresolved fields the author must confirm.

## Output format

Unless the user asks for another format, return:

```text
IEEE Reproducibility Package
[ready-to-paste statement]

Artifact map
- [artifact] -> [repository/supplement/access route]

Missing information / risk flags
- [specific flags or "None"]

中文核对
- [用中文列出作者需要确认的字段或 "无"]
```

When auditing an existing statement, lead with blocking issues first, then provide a revised version.

# IEEE Reproducibility Package Checklist

Use this file to audit whether an artifact package is understandable, rerunnable, and submission-ready for IEEE Transactions.

## Quick engineering test

| Area | Practical check |
|---|---|
| Locate | Each artifact has a stable path, repository record, release tag, DOI, or supplementary filename. |
| Understand | README explains purpose, file formats, units, parameters, dependencies, and figure/table mapping. |
| Rerun | Exact commands, environment, seeds, configs, and expected outputs are documented. |
| Verify | Logs, metrics, scripts, and figure/table data connect to manuscript claims and plots. |
| Bound | Restrictions, licenses, hardware limits, and unavailable artifacts are disclosed. |

## Artifact README template

```text
# [Artifact package title]

## Manuscript mapping
- Fig./Table [N]: [files/scripts/commands]

## Environment
- OS:
- Python/Matlab/ROS/simulator version:
- Required packages:
- Hardware/sensor/GPU requirements:

## Files
- [filename]: [contents, format, size, related figure/table]

## Parameters and units
[Name] | [Meaning] | [Unit] | [Default/value] | [Used in]

## Reproduction commands
1. [command]
2. [command]

## Expected outputs
- [output file/metric] should match [figure/table/result] within [tolerance if known]

## Access and license
[License, restrictions, embargo, private reviewer link, or request route.]
```

## File organization

- Keep raw logs, processed data, configs, scripts, and outputs separate.
- Include a manifest for archives or large multi-file deposits.
- Map figure/table data to exact manuscript panels and table numbers.
- Preserve units in column names, config files, or data dictionaries.
- Record missing-value codes, dropped trials, filtering, and smoothing decisions.
- Include checksums for large or critical files when the repository does not generate them.

## Provenance prompts

Ask the author:

- Which script or command produces each figure/table?
- Which simulator, robot platform, controller, network model, or data acquisition system produced each file?
- Which seeds, trials, folds, or time windows were used?
- Which samples/runs were excluded, and why?
- What version of each third-party dataset or package was used?
- Which artifacts cannot be public, and what substitute evidence can be shared?

## Final audit

Block submission until these are resolved:

- no reproducibility statement for empirical/computational work
- no stable access route for artifacts supporting central conclusions
- missing code/configs/seeds for simulation or learning-based results
- hardware or proprietary restriction without logs, metadata, or access procedure
- public package with no README, license, or figure/table mapping
- mismatch between manuscript, supplementary files, and repository contents

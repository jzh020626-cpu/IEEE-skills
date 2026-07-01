# Policy Principles

Use this file when deciding what an IEEE-ready reproducibility package must disclose.

## Governing rules

- Every empirical or computational IEEE Transactions manuscript should expose the artifacts needed to evaluate its central claims.
- The statement must say what artifacts exist, where they can be found, and any access conditions.
- The statement must cover generated data and reused third-party data, as well as code, configuration, parameters, logs, and model files when those artifacts support results.
- Reviewers may need private links, anonymized repositories, or supplementary files during evaluation.
- Restrictions are allowed only when justified and disclosed: proprietary data, security, privacy, export control, licensed third-party data, hardware safety, or unavailable physical platforms.
- Restricted artifacts still need a durable evaluation route: summary data, metadata, synthetic examples, pseudocode, parameter tables, logs, or institutional request procedure.
- "Available upon request" is weak unless the reason, responsible body, eligibility, and expected conditions are explicit.

## Minimal artifact test

Ask whether an independent reader can inspect or rerun the evidence behind the main figures and tables.

Include when applicable:

- figure/table data for main figures and key supplementary figures
- raw and processed logs for hardware or simulation trials
- parameter tables and configuration files
- random seeds, train/validation/test splits, and trial counts
- code commit/release, environment file, and run commands
- trained model weights and inference scripts
- simulator version, robot platform, sensor suite, controller settings, network/channel model, and hardware limits
- third-party datasets with source, version, date accessed, and license/access terms

Exclude only when defensible:

- artifacts that do not support a manuscript result
- purely theoretical work that generated no empirical or computational artifact
- proprietary/hardware artifacts that cannot be shared, if a clear substitute audit trail is provided

## Availability routes

| Route | Use when | Statement must include |
|---|---|---|
| Public repository | Data/code/logs can be openly shared | repository, DOI or release tag, contents, license if known |
| IEEE Xplore supplement | Small files, videos, proofs, code snippets, or README can accompany the paper | exact file names and what each supports |
| IEEE DataPort | Dataset package is suitable for IEEE's data repository | dataset title, DOI/URL, version, access terms |
| Private reviewer link | Review needs access before public release | anonymous link, expiry/embargo, contents |
| Third-party restricted | Data/software are licensed or owned externally | owner/source, why authors cannot redistribute, request route |
| Hardware-only restriction | Physical platform, facility, or safety constraints prevent public release | platform details, logs/metadata provided, contact or institutional route |
| Request-based access | No repository route is possible | reason, responsible group, eligibility, and conditions |
| Not applicable | No artifacts were generated or analyzed | concise reason; do not use for empirical work |

## Submission-stage checks

Before finalizing, confirm:

- all URLs, DOIs, release tags, and private reviewer links resolve
- supplementary file names match manuscript references
- code commands run from a clean checkout or are explicitly marked as illustrative
- seeds, configs, and parameters are sufficient to reproduce tables/figures
- restricted artifacts have a durable access route or a transparent limitation statement
- no central claim depends on unavailable artifacts without explanation

## Source notes

- IEEE Author Center and society pages provide the binding submission layer.
- IEEE DataPort and supplementary-material guidance provide a natural route for data/software attachments.
- Domain engineering practice determines the artifact granularity needed for robotics, control, communications, and industrial informatics.

# Repositories and Identifiers

Use this file when selecting repositories, checking release strategy, or writing artifact citations.

## Repository decision tree

1. Use the target journal's required supplementary-material route when it is mandatory.
2. Use IEEE DataPort for datasets that fit an IEEE data package.
3. Use a discipline or institutional repository when it better preserves the artifact and access terms.
4. Use GitHub/GitLab only with a release tag, license, README, and preferably an archived DOI for the exact submitted version.
5. Do not use personal websites, lab websites, ad hoc cloud folders, or unpublished private drives as the only availability route.
6. For very large logs, videos, ROS bags, or simulation outputs, preserve metadata and reproduction scripts even when bulk data require special transfer.

## What a repository record should provide

- persistent identifier: DOI, release tag, accession, Handle, ARK, or stable record
- public landing page with title, creators, version, license, and description
- file list with sizes and formats
- README, data dictionary, or runbook
- relation to manuscript figures, tables, and experiments
- provenance and processing description
- clear access procedure for restricted artifacts
- versioning or update policy

## Common artifact categories

| Artifact | Typical route |
|---|---|
| Source code | GitHub/GitLab release plus DOI archive, institutional repository, or IEEE supplement |
| Simulation configs | Code repository, supplementary ZIP, or experiment manifest |
| Random seeds and splits | Repository manifest, supplementary table, or config file |
| Robotics logs / ROS bags | Repository, institutional storage, or private reviewer link with metadata |
| Hardware settings | Parameter table, calibration file, README, or supplement |
| Network traces / channel configs | Dataset repository, IEEE DataPort, or supplement |
| Trained weights | Repository/release, model registry, or supplement when size permits |
| Videos / demos | IEEE multimedia supplement or repository with captioned file list |
| Proprietary industrial data | Metadata, aggregate statistics, access procedure, and clear restriction statement |

## Identifier rules

- Prefer final public identifiers before submission.
- If the record is private during review, provide an anonymous reviewer link when supported.
- Do not cite temporary sharing links as artifact identifiers.
- Include release tags and commit hashes exactly.
- Use one identifier per coherent artifact family; do not bury unrelated experiments under one unclear archive.
- Version artifacts when files change after review or publication.

## Citation pattern

For datasets or code packages that support conclusions:

```text
[Creator(s)], "[Artifact title]," [Repository], version [version], [identifier], [year].
```

For code:

```text
[Creator(s)], "[Repository or package title]," version [tag/commit], [repository/archive], [DOI or URL], [year].
```

## Red flags

- "Code/data available on GitHub" without a release tag, license, README, or archived version.
- No exact command connects code to a figure/table.
- Uploaded ZIP has no manifest or file descriptions.
- Private reviewer link exposes author identity during double-anonymous review.
- ROS bags/logs are mentioned but not mapped to experiments.
- Parameters are only in prose and not tied to runnable config files.

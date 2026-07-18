# IEEE Initial Submission Package

Use this reference only before the first editorial decision. The named journal's current Information for Authors, article-type rules, and submission-portal instructions override every generic default below.

## 1. Verify the route

Record the target journal, article type, submission stage, review model, template, compiled-page rule, required files, and date checked. Use official IEEE Author Center, society, and journal pages. Do not treat remembered page limits or an old checklist as current.

Collect or mark missing:

- manuscript title, abstract, Index Terms, article type, and target journal;
- author order, affiliations, corresponding-author details, email, and ORCID for every author;
- one-sentence contribution, strongest evidence, novelty boundary, scope fit, and limitations;
- funding, acknowledgments, conflicts, ethics/consent where applicable, and permissions;
- code/data/software repositories, versions, licenses, identifiers, access conditions, and supplements;
- preprint, thesis, conference version, related manuscript, prior submission, and concurrent-submission facts;
- suggested/opposed reviewers only when requested by the portal, including affiliation, institutional email, expertise, rationale, and conflict check;
- journal-specific items such as Note to Practitioners, graphical abstract, multimedia, supplementary files, bios/photos for final files, author declarations, or checklists.

Use `[AUTHOR_INPUT_NEEDED: ...]` rather than inferring administrative facts.

## 2. Deliverable matrix

Return a compact matrix:

| Item | Required / optional / N/A | Authority | Source or missing input | Output/status |
|---|---|---|---|---|
| Main IEEEtran manuscript |  |  |  |  |
| Anonymous manuscript or separate title page |  |  |  |  |
| Initial cover letter |  |  |  |  |
| Author metadata and ORCIDs |  |  |  |  |
| Note to Practitioners |  |  |  |  |
| Conference-version disclosure/difference matrix |  |  |  |  |
| Data/code availability and artifact package |  |  |  |  |
| Supplementary material / multimedia |  |  |  |  |
| Graphical abstract |  |  | route to `ieee-figure` |  |
| Declarations / permissions |  |  |  |  |
| Reviewer suggestions |  |  |  |  |

Do not generate highlights, a lay summary, a graphical abstract, biographies, or any other item merely because a generic publisher sometimes requests it. Include it only when the target journal or user asks.

## 3. Manuscript and metadata

Audit:

- IEEE article template/IEEEtran journal structure and final compiled PDF;
- title, Abstract, Index Terms, headings, equations, figures/tables, acknowledgments, and numbered references;
- consistent title, author order, affiliations, article type, funding, and repository links across every file and portal field;
- ORCID for all authors and corresponding-author contact details;
- anonymous versus identified file separation when required;
- page count, supplement boundary, graphics formats/resolution, and PDF font/metadata checks;
- citations/references ordered and formatted in IEEE numeric style.

For T-ASE, keep the Note to Practitioners distinct from the Abstract and in the current required position. Verify exact word count, article type, anonymity, and page rules on the current author page.

## 4. Initial cover letter

This is not a revision cover letter. Draft it only when required or requested.

Recommended anatomy:

```text
Dear [Editor / Editors],

Please consider "[Title]" as a [article type] for [journal].

[Problem and principal result, 1-2 sentences.]
[Specific technical advance and strongest evidence, 1-2 sentences.]
[Why this contribution fits the journal's scope/readership, 1 sentence.]

[Only required declarations: originality, all-author approval, conference/preprint/related-work disclosure, conflicts, or other portal-specific facts.]

Sincerely,
[Corresponding author]
```

Do not repeat the Abstract, invent editor names, or use unsupported priority claims. Keep it concise; obey a journal-specific length if one exists.

## 5. Conference, preprint, and related-work disclosure

When a related conference paper exists:

- cite and identify it accurately;
- disclose it in the place required by the journal/portal;
- build a difference matrix covering new theory, algorithms, proofs, experiments, datasets/scenarios, analysis, figures/tables, and discussion;
- explain added archival value concretely;
- upload the prior version when required.

Do not invent or enforce a universal IEEE percentage rule. Exact similarity, disclosure, and added-value requirements are venue-specific. A preprint is not automatically the same as a conference predecessor; label each version correctly.

## 6. Availability, supplements, and graphics

- Route a full reproducibility package to `ieee-data`.
- Map each code/data artifact to a real repository, version/commit, license, access condition, and reproduction instruction.
- Upload supplementary material separately when required and cite it from the manuscript.
- Keep central claims and necessary evidence in the main article; supplements support rather than conceal the core case.
- Route graphical abstracts/TOC graphics to `ieee-figure`. Verify current pixel dimensions, caption, peer-review treatment, and accepted format on the target page.
- Verify permissions and attribution for reused or adapted third-party figures/tables.

## 7. Declarations and reviewer suggestions

Prepare only applicable, author-confirmed blocks:

- authorship/author contributions;
- competing interests;
- funding and acknowledgments;
- data/code/software availability;
- ethics/consent;
- preprint, conference, related-manuscript, and originality disclosure;
- permissions.

For reviewer suggestions, require the author to confirm current affiliation, institutional email, topic expertise, and absence of journal-defined conflicts such as recent coauthorship, same institution, close collaboration, supervision, or personal conflict. Give factual reasons for opposed reviewers without attacking competence.

## 8. Completeness audit

Check that:

- the authoritative journal rules and article type are recorded;
- all required source/PDF/metadata files exist and open;
- author names/order/affiliations/ORCIDs match across files;
- anonymous/identified files are separated correctly;
- figures, tables, supplements, permissions, and graphical abstract are present and cited when required;
- code/data statements point to real destinations;
- prior versions are disclosed and differences are explicit;
- the cover letter matches the manuscript and does not overstate novelty;
- unresolved placeholders are visible;
- the final portal preview has been manually confirmed.

Readiness:

- `ready`: required facts/files are present and cross-checked.
- `ready_with_author_checks`: drafts are complete but portal or administrative confirmation remains.
- `blocked`: authorship, ethics, permission, integrity, central evidence, or mandatory journal-rule information is missing.

## 9. Templates and output

Use only the needed template:

| Template | Purpose |
|---|---|
| `templates/submission/initial-cover-letter.tex` | Initial editor-facing cover letter |
| `templates/submission/title-page.tex` | Separate identified title page/metadata |
| `templates/submission/declarations-and-reviewers.tex` | Declarations and reviewer suggestions |
| `templates/submission/highlights-and-summary.tex` | Optional highlights/summary only when the target explicitly requests them |

Keep unresolved facts visible as `AUTHOR_INPUT_NEEDED`, compile when a LaTeX engine is available, and report errors. Revision cover letters and reviewer responses belong to `ieee-response`.

Return:

1. `Submission readiness`
2. `Rules verified` with official source and date
3. `Deliverable matrix`
4. `Draft materials`
5. `AUTHOR_INPUT_NEEDED`
6. `Cross-file consistency checks`
7. `Next actions` in blocking order

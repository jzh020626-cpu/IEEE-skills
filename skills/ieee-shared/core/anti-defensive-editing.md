# Anti-defensive editing for IEEE manuscripts

Use with [claim-centered-writing.md](claim-centered-writing.md) for an author-requested
anti-defensive language audit or revision. Its integrity and reporting boundaries
apply before rhetorical choices. This is not an independent reviewer or statistical
assessment and does not replace the author's declared evaluation protocol.

## Editing procedure

1. Locate the requested span and establish whether the user wants findings,
   replacement prose, or a structural rewrite. Do not expand a sentence edit into
   a manuscript overhaul.
2. Separate facts from rhetoric. Preserve values, comparators, denominators,
   uncertainty, limitations, citations, assumptions and scope. A negative finding
   is not itself defensive writing.
3. Identify the defect: unsupported self-judgment, repeated qualification,
   development chronology, a claim broader than its evidence, or an experiment
   narrated without its argumentative role. If no defect is present, retain the
   passage rather than inventing a criticism.
4. Make the smallest correction that restores a supported claim. Keep author
   terminology, wording habits and unaffected paragraph structure. A stylistic
   change must not alter the experiment, baseline, metric, seed set or claim.
5. Check the revision against the original facts. If the proposed narrative needs
   a new explanation, mechanism or benefit, mark the missing support instead of
   supplying one. Keep a conclusion-changing qualification adjacent to the claim;
   do not bury it simply because an Abstract or Conclusion should be concise.

## Examples: remove rhetoric, preserve facts

These are constructed editing examples, not experimental results or evidence.

| Original | Minimal revision | Reason |
|---|---|---|
| Unfortunately, the controller only reduced tracking error by 12%, and cross-platform performance remains untested. | The controller reduced tracking error by 12%; cross-platform performance has not been evaluated. | Removes self-judgment while preserving the result and missing validation. |
| Although accuracy increased on two in-domain datasets, we must admit that these results should be treated cautiously because cross-domain generalization was not evaluated. | Accuracy increased on two in-domain datasets; cross-domain generalization was not evaluated. | Retains both the observed scope and the boundary. |
| We first tried scheduler A, debugged several failures, and finally implemented scheduler B. | If supplied evidence identifies B's mechanism, explain that mechanism and its role; otherwise flag the missing method description. | A chronological sentence does not justify inventing the final method. |
| Packet loss decreased, whereas task completion fell from 90% to 80%. | Packet loss decreased, whereas task completion fell from 90% to 80%. | The trade-off is factual; do not erase the primary outcome or declare overall superiority. |

For bilingual work, apply the same factual-preservation check. Terms such as
“遗憾的是 / unfortunately” or “必须承认 / we must admit” can be removed when they add
only stance. Words such as “only” may encode a real scope restriction, e.g.,
“only under bounded delay”; preserve that restriction or rephrase it equivalently.
“Lower than” and “performance decreased” are valid factual comparisons, not banned
phrases. A non-significant result cannot become equivalence or “comparable”
performance without an appropriate equivalence/non-inferiority analysis.

## Evidence placement and reframing

Keep the predeclared primary endpoint, comparison protocol and complete seed/run
record intact. A secondary resource saving does not establish a primary task-success
advantage. Report the trade-off and narrow the conclusion. New post-hoc evaluation
frames are exploratory; do not retrospectively label them the original objective.

For theory and control, retain assumptions and the distinction between sampled
observations and continuous-time guarantees. For experiments, retain failure cases
that change validity, deployment or safety. Reviewers' requested unfavorable results
must be answered directly. Use the shared main-text/supplement routing only after
these claim-defining facts have been preserved.

## Delivery

- A prose-only edit returns the revised passage; add a note only for a material
  unresolved factual or structural issue.
- An explicit audit returns a compact `Original | Proposed edit | Reason` table
  for actual defects. Do not require a fixed number of findings or edit clean text.
- A requested full restructuring may include the revised argument and evidence
  placement decisions. Keep unrequested methods, figures and files unchanged.

Source: Adkid-Zephyr's MIT-licensed bilingual Anti-Defensive Writing skill and
prompt pack; pinned in `scripts/anti-defensive-upstream.lock` at repository root.
The complete license remains in `../licenses/anti-defensive-writing-MIT.txt`.

# Writing workflow

Use the complete workflow for a new section or full argument. For a local edit, run only the relevant steps, preserve established terminology and framing, and return the requested edit. Step 3b resolves material ambiguity; it is not an approval stage.

## 1. Build a one-sentence argument

> In [system/problem], we show [advance] using [approach], supported by [evidence], with [boundary].

Force every section to serve this sentence. If the sentence cannot be written, the paper does not yet have an argument — surface that to the user.

## 1b. Build the Terminology Ledger

On first contact with the material, extract the recurring terms, abbreviations, notation, and proper names into a Terminology Ledger before drafting any prose. Lock the canonical forms and reuse them across every section. See `../../../ieee-shared/core/terminology-ledger.md`.

## 1c. Separate the main argument from the complete record

Before choosing section architecture, classify the material:

- **Main manuscript:** the central claim, distinctive solution, direct evidence,
  mechanism, strongest alternative explanation, and any boundary that changes a
  reasonable reader's interpretation.
- **Supplement or artifact record:** complete scenario tables, non-leading
  ablations, stopped attempts, evaluator counts, provenance, hashes, projection
  diagnostics, and repeated audit detail.

Preserve required evidence, but do not let the main paper read as a project log
or pre-emptive reviewer response. See
`../../../ieee-shared/core/claim-centered-writing.md`.

For Results or full-main-text work, refine this split with
`../../../ieee-shared/core/main-text-discipline.md`: classify core results,
necessary support, qualifications, robustness, heterogeneity, provenance,
alternative inference, and edge/failure cases before placement. If the target
venue does not permit Supplementary Material, use an allowed appendix or
artifact repository and keep indispensable evidence in the main text.

## 2. Choose section architecture

Pick the section structure from the relevant `section/*.md` fragment and, if needed, deeper patterns from `references/article-architecture.md`.

## 3. Map each paragraph to one job

Each paragraph must do exactly one job from: context, gap, approach, result, comparison, mechanism, implication, limitation.

If a paragraph carries two jobs, split it before drafting.

## 3b. Scoped alignment check

Proceed from supplied evidence and established context. For substantial drafts, briefly state the central argument and consequential assumptions, then continue. Ask only about unresolved choices that materially change the argument, evidence meaning, or requested deliverable. Pause only dependent passages and use visible placeholders for missing facts.

If the user explicitly requested outline approval, provide the outline and wait. Otherwise complete the authorized draft and relevant checks. A follow-up correction supplies context, not a reason to request the same approval again.

## 4. Draft from evidence outward

Keep claims near the data that support them. Do not stack claims at the top of a section then leave evidence at the bottom.

## 5. Calibrate verbs to evidence strength

`show` / `demonstrate` need strong direct evidence. `suggest` / `indicate` are for trend-level or indirect evidence. `may` / `could` are for plausible but unverified mechanisms.

## 6. Remove unsupported novelty and universal claims

Sweep for `first`, `unique`, `unprecedented`, `comprehensive`, `complete`, `always`, `never`. Replace with bounded claims or delete.

## 7. Run a paragraph-flow check

- One paragraph, one message.
- The first sentence is the topic / claim.
- Each subsequent sentence has an explicit relation to the previous one (cause, comparison, restriction, example).

For full reverse-outlining, open `references/paragraph-flow.md`.

## 8. Return prose plus notes

Output the draft together with explicit notes on assumptions, missing inputs, and where evidence is needed. See `output-format.md`.

## 9. Revise by targeted edit, not full rewrite

When the user reacts to a draft, "this is not what I meant" is usually local — a wrong claim, a mis-framed paragraph, the wrong result leading. Do not silently re-draft the whole section: a full rewrite breaks the paragraphs that were already right and forces the user to re-check everything.

- Change **only** the paragraphs or claims the user flagged; keep the rest verbatim.
- If a requested fix genuinely forces a structural change (reordering sections, moving a claim across paragraphs), explain and apply the necessary adjacent edits within the authorized scope; clarify only a material unresolved argument or scope change, rather than restructuring silently.
- Keep the Terminology Ledger (step 1b) stable across revisions unless the user changes a term; never let a revision reintroduce a variant of a locked term.
- After revising, re-run only the checks relevant to what changed (steps 5-7), not the whole workflow.
- If the user's redirection reveals the original premise was wrong, apply the correction and revisit only unresolved choices in step 3b instead of patching prose on a broken premise.

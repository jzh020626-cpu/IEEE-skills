# Output format

Default output:

1. The polished text as plain prose, not in a code block.
2. `Revision notes:` only for material changes or unresolved issues; do not pad a fixed bullet quota or append notes when the user requests prose only.
3. If the rewrite changed section logic, say so explicitly.

If the user asks for side-by-side revision, provide:

- `Original`
- `Polished`
- `Why changed`

If any paragraph's structural problem could not be fixed without inventing content, say so under `Revision notes:` instead of papering over it.

For Results or full-main-text restructuring, also return a compact main-text
discipline audit: destination decisions, replaced/compressed/relocated/deleted
material, unresolved integrity constraints, and before/after word count.

For an explicit anti-defensive audit, use `Original | Proposed edit | Reason` for actual defects. Preserve clean passages and report no issue when none is supported. Do not turn a bounded wording edit into a full main-text or evidence-placement audit.

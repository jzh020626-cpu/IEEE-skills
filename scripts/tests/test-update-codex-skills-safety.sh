#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT

DEST="$TMP_DIR/skills"
VICTIM="$TMP_DIR/victim"
SAFE_STALE="ieee-removed-test"
UNOWNED="pdf"

mkdir -p "$DEST/$SAFE_STALE" "$DEST/$UNOWNED" "$VICTIM"
touch "$DEST/$UNOWNED/must-survive"
mkdir -p "$DEST/ieee-image2ppt"
printf '%s\n' 'PADDLE_OCR_TOKEN: "legacy-secret"' >"$DEST/ieee-image2ppt/config.yaml"
touch "$VICTIM/must-survive"
printf '%s\n' \
  '# test manifest' \
  '../victim' \
  "$UNOWNED" \
  "$SAFE_STALE" >"$DEST/.ieee-trans-skills-install.txt"

bash "$REPO_ROOT/scripts/update-codex-skills.sh" \
  --dest "$DEST" \
  --prune >"$TMP_DIR/stdout" 2>"$TMP_DIR/stderr"

if ! grep -Fq "ieee-figure/requirements.txt" "$TMP_DIR/stdout"; then
  echo "Figure runtime dependency note was not emitted." >&2
  exit 1
fi

if ! grep -Fq "ieee-image2ppt/requirements.txt" "$TMP_DIR/stdout"; then
  echo "Image2PPT runtime dependency note was not emitted." >&2
  exit 1
fi

if [ ! -f "$VICTIM/must-survive" ]; then
  echo "Unsafe manifest entry escaped the destination directory." >&2
  exit 1
fi

if [ ! -f "$DEST/$UNOWNED/must-survive" ]; then
  echo "A safe-but-unmanaged skill name was incorrectly pruned." >&2
  exit 1
fi

if [ "$(cat "$DEST/ieee-image2ppt/config.yaml")" != 'PADDLE_OCR_TOKEN: "legacy-secret"' ]; then
  echo "Legacy Image2PPT config was not preserved across installation." >&2
  exit 1
fi

if [ -d "$DEST/$SAFE_STALE" ]; then
  echo "Safe stale managed directory was not pruned." >&2
  exit 1
fi

if ! grep -Fq "ignoring unsafe managed skill name" "$TMP_DIR/stderr"; then
  echo "Unsafe manifest entry was not reported." >&2
  exit 1
fi

if ! grep -Fq "ignoring unmanaged skill name in IEEE manifest" "$TMP_DIR/stderr"; then
  echo "Safe-but-unmanaged manifest entry was not reported." >&2
  exit 1
fi

ROLLBACK_DEST="$TMP_DIR/rollback-skills"
FAKE_BIN="$TMP_DIR/fake-bin"
REAL_MV=$(command -v mv)
mkdir -p "$ROLLBACK_DEST/ieee-academic-search" "$FAKE_BIN"
printf '%s\n' "original install" >"$ROLLBACK_DEST/ieee-academic-search/SKILL.md"
printf '%s\n' \
  '#!/usr/bin/env bash' \
  'count=0' \
  '[ ! -f "$ATOMIC_TEST_MV_COUNT" ] || count=$(cat "$ATOMIC_TEST_MV_COUNT")' \
  'count=$((count + 1))' \
  'printf "%s\n" "$count" >"$ATOMIC_TEST_MV_COUNT"' \
  'if [ "$count" = "2" ]; then exit 42; fi' \
  'exec "$ATOMIC_TEST_REAL_MV" "$@"' >"$FAKE_BIN/mv"
chmod +x "$FAKE_BIN/mv"

if ATOMIC_TEST_MV_COUNT="$TMP_DIR/mv-count" \
   ATOMIC_TEST_REAL_MV="$REAL_MV" \
   PATH="$FAKE_BIN:$PATH" \
   bash "$REPO_ROOT/scripts/update-codex-skills.sh" --dest "$ROLLBACK_DEST" \
     >"$TMP_DIR/rollback-stdout" 2>"$TMP_DIR/rollback-stderr"; then
  echo "Expected the injected activation failure to stop installation." >&2
  exit 1
fi

if [ "$(cat "$ROLLBACK_DEST/ieee-academic-search/SKILL.md")" != "original install" ]; then
  echo "The previous skill installation was not restored after activation failed." >&2
  exit 1
fi

if find "$ROLLBACK_DEST" -maxdepth 1 \
    \( -name '.ieee-skills-stage.*' -o -name '.ieee-skills-backup.*' \) \
    | grep -q .; then
  echo "Transaction staging data was left behind after rollback." >&2
  exit 1
fi

echo "Skill prune safety and transactional rollback passed."

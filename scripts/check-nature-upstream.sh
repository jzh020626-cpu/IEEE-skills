#!/usr/bin/env bash
#
# check-nature-upstream.sh - detect upstream nature-skills changes for the
# IEEE Transactions adaptation workflow.
#
# Default mode:
#   - checks https://github.com/Yuan1z0825/nature-skills.git HEAD
#   - compares it with the last IEEE-adapted upstream commit
#   - updates the local sibling nature-skills checkout with git pull --ff-only
#   - records a pending upstream update without marking it adapted
#
# Marking mode:
#   scripts/check-nature-upstream.sh --mark <commit>
# marks a commit as adapted only after the IEEE conversion and validation pass.
#
set -euo pipefail

UPSTREAM_URL="${UPSTREAM_URL:-https://github.com/Yuan1z0825/nature-skills.git}"
NATURE_DIR="${NATURE_DIR:-/Users/hjz/Desktop/skills/nature-skills}"
IEEE_DIR="${IEEE_DIR:-/Users/hjz/Desktop/skills/ieee-trans-skills}"
ARTIFACT_ROOT="${ARTIFACT_ROOT:-/Users/hjz/Desktop/skills/artifacts}"
STATE_DIR="${STATE_DIR:-$IEEE_DIR/.upstream}"
STATE_FILE="$STATE_DIR/nature-skills.last-adapted"
PENDING_FILE="$STATE_DIR/nature-skills.pending"

usage() {
  cat <<'USAGE'
check-nature-upstream.sh - detect upstream changes for IEEE skill adaptation.

Usage:
  scripts/check-nature-upstream.sh              Check upstream and create pending state when changed.
  scripts/check-nature-upstream.sh --init       Seed current upstream commit as already adapted.
  scripts/check-nature-upstream.sh --mark SHA   Mark SHA as adapted after successful IEEE validation.

Environment:
  UPSTREAM_URL=https://github.com/Yuan1z0825/nature-skills.git
  NATURE_DIR=/Users/hjz/Desktop/skills/nature-skills
  IEEE_DIR=/Users/hjz/Desktop/skills/ieee-trans-skills
  ARTIFACT_ROOT=/Users/hjz/Desktop/skills/artifacts
USAGE
}

die() {
  echo "ERROR: $*" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "$1 is required but not installed"
}

latest_remote_commit() {
  git ls-remote "$UPSTREAM_URL" HEAD | awk 'NR == 1 {print $1}'
}

pending_value() {
  key="$1"
  [ -f "$PENDING_FILE" ] || return 0
  sed -n "s/^$key=//p" "$PENDING_FILE" | tail -n 1
}

sync_nature_checkout() {
  if [ -d "$NATURE_DIR/.git" ]; then
    git -C "$NATURE_DIR" fetch origin
    git -C "$NATURE_DIR" pull --ff-only
  elif [ ! -e "$NATURE_DIR" ]; then
    git clone "$UPSTREAM_URL" "$NATURE_DIR"
  else
    die "$NATURE_DIR exists but is not a git checkout"
  fi
}

write_artifact() {
  previous="$1"
  latest="$2"
  mode="$3"
  ts="$(date '+%Y%m%d_%H%M%S')"
  artifact="$ARTIFACT_ROOT/${ts}_nature_upstream_check"
  mkdir -p "$artifact"
  {
    echo "# nature-skills upstream check"
    date '+created_at=%Y-%m-%dT%H:%M:%S%z'
    echo "mode=$mode"
    echo "upstream_url=$UPSTREAM_URL"
    echo "previous_adapted=$previous"
    echo "latest_remote=$latest"
    echo "nature_dir=$NATURE_DIR"
    echo "ieee_dir=$IEEE_DIR"
    echo
    echo "# exact commands"
    echo "git ls-remote $UPSTREAM_URL HEAD"
    if [ -d "$NATURE_DIR/.git" ]; then
      echo "git -C $NATURE_DIR fetch origin"
      echo "git -C $NATURE_DIR pull --ff-only"
    elif [ ! -e "$NATURE_DIR" ]; then
      echo "git clone $UPSTREAM_URL $NATURE_DIR"
    fi
    if [ "$mode" = "updated" ]; then
      echo "scripts/check-nature-upstream.sh --mark $latest"
    fi
  } > "$artifact/exact_commands.txt"
  echo "$artifact"
}

MODE="check"
MARK_SHA=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --init)
      MODE="init"
      ;;
    --mark)
      shift
      [ "$#" -gt 0 ] || die "--mark requires a commit SHA"
      MODE="mark"
      MARK_SHA="$1"
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      die "unknown argument: $1"
      ;;
  esac
  shift
done

need_cmd awk
need_cmd git
need_cmd sed
mkdir -p "$STATE_DIR"

latest="$(latest_remote_commit)"
[ -n "$latest" ] || die "could not resolve upstream HEAD from $UPSTREAM_URL"

case "$MODE" in
  mark)
    pending_latest="$(pending_value latest)"
    if [ -n "$pending_latest" ] && [ "$pending_latest" != "$MARK_SHA" ]; then
      die "pending commit is $pending_latest, not $MARK_SHA"
    fi
    if [ "$MARK_SHA" != "$latest" ]; then
      die "refusing to mark $MARK_SHA because current upstream HEAD is $latest"
    fi
    printf '%s\n' "$MARK_SHA" > "$STATE_FILE"
    rm -f "$PENDING_FILE"
    echo "MARKED $MARK_SHA"
    exit 0
    ;;
  init)
    previous="$(cat "$STATE_FILE" 2>/dev/null || true)"
    artifact="$(write_artifact "$previous" "$latest" initialized)"
    sync_nature_checkout
    printf '%s\n' "$latest" > "$STATE_FILE"
    rm -f "$PENDING_FILE"
    echo "INITIALIZED $latest"
    echo "ARTIFACT $artifact"
    exit 0
    ;;
esac

previous="$(cat "$STATE_FILE" 2>/dev/null || true)"
if [ "$latest" = "$previous" ]; then
  echo "UNCHANGED $latest"
  exit 0
fi

pending_latest="$(pending_value latest)"
pending_artifact="$(pending_value artifact)"
if [ "$pending_latest" = "$latest" ]; then
  echo "PENDING $previous -> $latest"
  [ -z "$pending_artifact" ] || echo "ARTIFACT $pending_artifact"
  exit 0
fi

artifact="$(write_artifact "$previous" "$latest" updated)"
sync_nature_checkout
{
  echo "previous=$previous"
  echo "latest=$latest"
  echo "artifact=$artifact"
} > "$PENDING_FILE"

echo "UPDATED $previous -> $latest"
echo "ARTIFACT $artifact"

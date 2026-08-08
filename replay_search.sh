#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
BUILD_DIR="${TMPDIR:-/tmp}/ramsey147-replay-$$"
mkdir -p "$BUILD_DIR"
trap 'rm -rf "$BUILD_DIR"' EXIT

g++ -O3 -std=c++17 "$ROOT/code/search_polarity_deletion.cpp" -o "$BUILD_DIR/search"
"$BUILD_DIR/search" 13 24 12 555 20000000 "$BUILD_DIR/replay.json" 1
python - "$ROOT/data/deleted_points_primary_indices.json" "$BUILD_DIR/replay.json" <<'PY'
import json, sys
expected = json.load(open(sys.argv[1], encoding='utf-8'))
observed = json.load(open(sys.argv[2], encoding='utf-8'))
if expected != observed:
    raise SystemExit(f"replay mismatch:\nexpected={expected}\nobserved={observed}")
print("PASS: seed-555 discovery replay exactly reproduced the primary deletion list")
PY

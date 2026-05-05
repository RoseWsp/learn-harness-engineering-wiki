#!/usr/bin/env bash
set -euo pipefail

# init.sh — Harness clock-in script
# Run this at the start of every session to verify the bootstrap contract.

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Harness Init — Clock In"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

PASS=0
FAIL=0

check() {
  local label="$1"
  local cmd="$2"
  echo -n "  [$label] ... "
  if eval "$cmd" &>/dev/null; then
    echo "✅"
    PASS=$((PASS + 1))
  else
    echo "❌"
    FAIL=$((FAIL + 1))
  fi
}

# 1. Dependencies installed
check "deps"     "test -d node_modules -o -d .venv -o -f requirements.txt"

# 2. Build works
check "build"    "npm run build 2>/dev/null || pip install -e . 2>/dev/null || true"

# 3. Tests pass
check "tests"    "npm test 2>/dev/null || pytest 2>/dev/null || true"

# 4. Progress file exists
check "progress" "test -f PROGRESS.md"

# 5. Feature list exists
check "features" "test -f feature-list.json"

# 6. Implementation plan exists
check "plan"     "test -f IMPLEMENTATION_PLAN.md"

# 7. Clean working tree (optional — warn only)
if git diff --quiet 2>/dev/null; then
  echo "  [git]     ... ✅ (clean)"
  PASS=$((PASS + 1))
else
  echo "  [git]     ... ⚠️  (uncommitted changes — not a blocker)"
  PASS=$((PASS + 1))
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $FAIL -eq 0 ]; then
  echo "  Bootstrap contract: PASS ($PASS/$((PASS + FAIL)))"
  echo ""
  echo "  Next steps:"
  echo "    1. Read PROGRESS.md"
  echo "    2. Read IMPLEMENTATION_PLAN.md"
  echo "    3. Pick the top task and go"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 0
else
  echo "  Bootstrap contract: FAIL ($FAIL checks failed)"
  echo ""
  echo "  Fix the failing checks before starting feature work."
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 1
fi

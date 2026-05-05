# Evaluator Rubric

Score each dimension 1-5. Total ≥ 15 = PASS, 10-14 = minor issues, < 10 = FAIL.

## Dimensions

### 1. Correctness (weight: 5)
Does it do what the feature-list says? Handles edge cases?

### 2. Architecture Compliance (weight: 4)
Follows project patterns? Proper module boundaries? No circular deps?

### 3. Test Coverage (weight: 4)
Unit tests for new logic? E2E tests for user flows? Tests actually pass?

### 4. Clean State (weight: 3)
Build green? No stale artifacts? PROGRESS.md updated? Docs current?

### 5. Completeness (weight: 4)
No placeholders or stubs? Feature is fully usable? No TODO comments left?

## Scoring

| Total Score | Verdict |
|---|---|
| 15-20 | PASS |
| 10-14 | PASS with minor issues |
| < 10 | FAIL — rework required |

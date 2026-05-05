# Testing Standards

## Rules

1. **Tests before code** — Write a failing test first, then implement.
2. **Test behavior, not implementation** — Verify what the code does, not how it does it.
3. **One assertion per test** (ideally) — Makes failures easy to diagnose.
4. **Descriptive test names** — `test("returns 404 when document not found")` not `test("error")`.
5. **No skipped tests** — If a test is skipped, it's either a bug (fix it) or dead code (delete it).

## Coverage Targets

- Core business logic: **100%**
- API handlers: **90%+**
- UI components: **80%+**
- Utility functions: **95%+**

## E2E Tests

- Test user flows, not implementation details.
- Keep E2E tests minimal and fast — they're expensive.
- Use realistic test data.
- E2E tests catch what unit tests miss: component boundary defects.

## What To Test

- Happy path (the golden flow)
- Error paths (bad input, missing data, network failures)
- Edge cases (empty collections, off-by-one, null/undefined)
- Integration points (API calls, database reads, file I/O)

# AGENTS.md — agent-container-fixture

Fixture repo for testing coding agents across three difficulty tiers.

## Repo structure

| File | Purpose | Tier |
|---|---|---|
| `mathlib.py` | Math utilities — contains a deliberate bug | Tier 1 |
| `test_mathlib.py` | Tests for mathlib | Tier 1 |
| `statslib.py` | Stats utilities — median() and variance() not implemented | Tier 2 |
| `test_statslib.py` | Tests for statslib | Tier 2 |
| `geometry.py` | Geometry utilities — uses old naming convention (calc_*) | Tier 3 |
| `shapes.py` | Shape helpers that import from geometry.py | Tier 3 |
| `test_geometry.py` | Tests expecting new naming convention (area_*, perimeter_*) | Tier 3 |
| `test_shapes.py` | Tests for shapes module | Tier 3 |
| `greet.py` | Unrelated utility — do not modify | — |

---

## How to work in this repo

Follow these steps on every task — they prevent the most common failure modes.

### Step 1 — Plan before touching any file

Before making any edit, write out every change required:
- Which files need to change?
- For rename tasks: grep for every usage of the old name across all files before starting.
- For implementation tasks: read the test file first to understand exactly what is expected.

Do not make any edit until the full plan is clear.

### Step 2 — Choose the right editing tool

**For implementing stub functions** (replacing a `raise NotImplementedError` body):
Use `write` to rewrite the complete file. Do NOT use `edit` for function bodies.
Reason: `write` lets you produce the whole file as natural code. `edit` requires
encoding newlines and indentation inside a JSON string, which causes truncation and
indentation bugs.

**For small targeted changes** (renaming one identifier, fixing one line):
Use `edit` with an `oldString` that includes the full function signature plus the line
to replace — not just the single line being changed. More context = more reliable match.

### Step 3 — Apply every planned change

Work through the plan completely. Do not stop after the first change.
After writing or editing a file, immediately read it back to confirm the content is correct
before moving to the next file.

### Step 4 — Verify with tests

After all changes are applied, run the acceptance command. Only declare done when tests pass.
If tests fail, read the file that was changed and diagnose from the actual content — do not
guess which function is broken.

---

## Tier 1 — single-line bug fix

`sum_to_n()` in `mathlib.py` uses `range(1, n)` but should use `range(1, n + 1)`.
Fix only this line — do not change the function signature, docstring, or any other file.

**Acceptance:** `pytest test_mathlib.py -q` — all 4 tests pass.

**Constraints:** modify only `mathlib.py`, one-character fix.

---

## Tier 2 — multi-file implementation

`statslib.py` has `mean()` correctly implemented, but `median()` and
`variance()` raise `NotImplementedError`. Implement both functions so
all tests in `test_statslib.py` pass. Do not modify the test file.

**Acceptance:** `pytest test_statslib.py -q` — all 12 tests pass.

**Plan (follow Steps 1–4 above):**
1. Read `test_statslib.py` to understand expected behaviour for both functions.
2. Read `statslib.py` to see the current file content.
3. Use `write` to rewrite `statslib.py` with both `median()` and `variance()` fully
   implemented — keep `mean()` unchanged, implement both stubs in the same write call.
   - `median()`: sort the list, return middle element (odd length) or average of the two
     middle elements (even length). Handle both cases.
   - `variance()`: population variance — `sum((x - mean(values))**2 for x in values) / len(values)`.
4. Read `statslib.py` back to confirm both functions are present and correctly indented.
5. Run `pytest test_statslib.py -q` and confirm all 12 tests pass.

**Notes:**
- `mean()` is already implemented — do not remove it when rewriting.
- `median()` must handle both odd- and even-length lists; sort first.
- `variance()` uses the existing `mean()` function in the same file.

---

## Tier 3 — exploratory grep + multi-file rename

`geometry.py` exports functions with the old `calc_*` naming convention.
`test_geometry.py` expects new names (`area_rectangle`, `area_circle`,
`perimeter_rectangle`, `perimeter_circle`). `shapes.py` imports the old names.

Rename all four functions in `geometry.py` to the new names, then find
and update every caller so that both test files pass.

**Acceptance:** `pytest test_geometry.py test_shapes.py -q` — all 9 tests pass.

**Plan (follow Steps 1–4 above):**
1. Read `test_geometry.py` — note the four expected new names.
2. Read `geometry.py` — note the four old names.
3. Read `shapes.py` — note which old names it imports and calls.
4. Use `write` to rewrite `geometry.py` with all four functions renamed.
5. Use `write` to rewrite `shapes.py` with the import line and every call site updated.
6. Read both files back to confirm changes are correct.
7. Run `pytest test_geometry.py test_shapes.py -q` — both test files must pass.

**Constraints:** only rename — do not change function bodies or add new logic.

---

## Running all tiers at once

```bash
pytest test_mathlib.py test_statslib.py test_geometry.py test_shapes.py -q
```

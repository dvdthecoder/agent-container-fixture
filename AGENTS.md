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

### Step 2 — Apply every planned change

Work through the plan completely. Do not stop after the first edit if more changes are required.
Use the edit tool for each file that needs changing.

### Step 3 — Indentation rule for multi-line edits

When replacing code that sits inside an indented block (e.g. inside a function), every line
of the replacement must include the correct leading spaces exactly as they appear in the file.

Correct — each line carries its own indent:
```
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2.0
    return sorted_vals[mid]
```

Wrong — only the first line is indented, rest land at column 0:
```
    sorted_vals = sorted(values)
mid = len(sorted_vals) // 2
if len(sorted_vals) % 2 == 0:
```

### Step 4 — Verify with tests

After all edits are applied, run the acceptance command. Only declare done when tests pass.

---

## Tier 1 — single-line bug fix

`sum_to_n()` in `mathlib.py` uses `range(1, n)` which excludes `n`.
It should be `range(1, n + 1)`. Fix only this line — do not change the
function signature, docstring, or any other file.

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
2. Read `statslib.py` to see the stubs.
3. Implement `median()` — sort the list, return middle element (odd) or average of two middle elements (even). Include all 4 spaces of indentation on every line.
4. Implement `variance()` — population variance: `sum((x - mean(values))**2 for x in values) / len(values)`. Include all 4 spaces of indentation on every mine.
5. Both functions must be implemented before running tests.

**Notes:**
- `median()` must handle both odd- and even-length lists; sort first.
- `variance()` is population variance: `sum((x - mean)² for x in values) / len(values)`.

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
4. Rename all four functions in `geometry.py`.
5. Update `shapes.py`: fix the import line and every call site.
6. Run acceptance tests — both `test_geometry.py` and `test_shapes.py` must pass.

**Constraints:** only rename — do not change function bodies or add new logic.

---

## Running all tiers at once

```bash
pytest test_mathlib.py test_statslib.py test_geometry.py test_shapes.py -q
```

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

**Notes:**
- `median()` must handle both odd- and even-length lists; sort first.
- `variance()` is population variance: `sum((x - mean)² for x in values) / len(values)`.

---

## Tier 3 — exploratory grep + multi-file rename

`geometry.py` exports functions with the old `calc_*` naming convention.
`test_geometry.py` expects new names (`area_rectangle`, `area_circle`,
`perimeter_rectangle`, `perimeter_circle`). `shapes.py` imports the old names.

Rename all four functions in `geometry.py` to the new names, then find
and update every caller (hint: `shapes.py` imports them) so that both
test files pass.

**Acceptance:** `pytest test_geometry.py test_shapes.py -q` — all 9 tests pass.

**Constraints:** only rename — do not change function bodies or add new logic.

---

## Running all tiers at once

```bash
pytest test_mathlib.py test_statslib.py test_geometry.py test_shapes.py -q
```

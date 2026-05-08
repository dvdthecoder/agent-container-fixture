# AGENTS.md — agent-container-fixture

Fixture repo used to test coding agents. Contains a deliberate bug for agents to find and fix.

## Repo structure

| File | Purpose |
|---|---|
| `mathlib.py` | Math utilities — contains the bug to fix |
| `test_mathlib.py` | Test suite — must pass after fix |
| `greet.py` | Unrelated utility — do not modify |

## The bug

`sum_to_n()` in `mathlib.py` uses `range(1, n)` which excludes `n`.
It should be `range(1, n + 1)`. Fix only this line — do not change the
function signature, docstring, or any other file.

## Acceptance

```bash
pytest test_mathlib.py -q
```

All 4 tests must pass. The fix is a single character change on one line.

## Constraints

- Modify only `mathlib.py`
- Do not change the function signature or docstring
- No new dependencies

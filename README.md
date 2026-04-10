# agent-container-fixture

Fixture repository for [agent-container](https://github.com/dvdthecoder/agent-container) integration tests.

## Purpose

`mathlib.py` contains a deliberate off-by-one bug in `sum_to_n()`:

```python
# BUG: range(1, n) excludes n — should be range(1, n + 1)
return sum(range(1, n))
```

The integration test suite dispatches a coding agent to this repo, the agent opens a PR with the fix, and the test asserts the diff is correct.

**The bug on `main` is permanent — agent PRs are never merged back.**

## Running the tests locally (they will fail — that's the point)

```bash
python -m pytest test_mathlib.py -v
```

"""Simple math utilities."""


def sum_to_n(n: int) -> int:
    """Return the sum of integers from 1 to n (inclusive).

    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(0)
        0
    """
    # BUG: range(1, n) excludes n — should be range(1, n + 1)
    return sum(range(1, n))

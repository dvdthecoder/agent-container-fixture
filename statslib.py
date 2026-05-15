"""Statistical utilities."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median value of a list of numbers."""
    if not values:
        raise ValueError("median() requires at least one value")
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2.0
    else:
        return sorted_values[mid]


def variance(values: list[float]) -> float:
    """Return the population variance of a list of numbers."""
    if not values:
        raise ValueError("variance() requires at least one value")
    avg = mean(values)
    return sum((x - avg) ** 2 for x in values) / len(values)

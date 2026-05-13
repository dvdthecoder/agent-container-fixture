"""Statistical utilities."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median value of a list of numbers."""
    values.sort()
mid = len(values) // 2
if len(values) % 2 == 0:
    return (values[mid - 1] + values[mid]) / 2
else:
    return values[mid]


def variance(values: list[float]) -> float:
    """Return the population variance of a list of numbers."""
    raise NotImplementedError("variance() is not implemented yet")

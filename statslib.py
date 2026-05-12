"""Statistical utilities."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values: list[float]) -> float:
    """Return the median value of a list of numbers."""
    raise NotImplementedError("median() is not implemented yet")


def variance(values: list[float]) -> float:
    """Return the population variance of a list of numbers."""
    raise NotImplementedError("variance() is not implemented yet")

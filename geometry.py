"""Geometry utilities."""

import math


def area_rectangle(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def area_circle(radius: float) -> float:
    """Return the area of a circle."""
    return math.pi * radius**2


def perimeter_rectangle(width: float, height: float) -> float:
    """Return the perimeter of a rectangle."""
    return 2 * (width + height)


def perimeter_circle(radius: float) -> float:
    """Return the circumference of a circle."""
    return 2 * math.pi * radius

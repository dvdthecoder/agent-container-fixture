"""High-level shape helpers built on geometry.py."""

from geometry import area_circle, area_rectangle, perimeter_rectangle


def is_square(width: float, height: float) -> bool:
    """Return True if the rectangle is a square."""
    return width == height


def scale_area_rect(width: float, height: float, factor: float) -> float:
    """Return the area of a rectangle scaled by factor."""
    return calc_area_rect(width, height) * factor


def largest_area(shapes: list[dict]) -> float:
    """Return the largest area from a list of shape dicts.

    Each dict must have 'type' ('rect' or 'circle') and the relevant dimensions.
    """
    areas = []
    for shape in shapes:
        if shape["type"] == "rect":
            areas.append(area_rectangle(shape["width"], shape["height"]))
        elif shape["type"] == "circle":
            areas.append(area_circle(shape["radius"]))
    return max(areas) if areas else 0.0

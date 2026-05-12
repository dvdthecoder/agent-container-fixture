"""Tests for shapes module — exercises shapes.py which wraps geometry.py."""

import math

from shapes import is_square, largest_area, scale_area_rect


class TestIsSquare:
    def test_square(self):
        assert is_square(5, 5) is True

    def test_not_square(self):
        assert is_square(3, 4) is False


class TestScaleAreaRect:
    def test_double(self):
        assert scale_area_rect(3, 4, 2.0) == 24.0

    def test_half(self):
        assert scale_area_rect(10, 10, 0.5) == 50.0


class TestLargestArea:
    def test_rect_wins(self):
        shapes = [
            {"type": "rect", "width": 10, "height": 10},
            {"type": "circle", "radius": 1},
        ]
        assert largest_area(shapes) == 100.0

    def test_circle_wins(self):
        shapes = [
            {"type": "rect", "width": 1, "height": 1},
            {"type": "circle", "radius": 10},
        ]
        assert abs(largest_area(shapes) - math.pi * 100) < 1e-9

    def test_empty(self):
        assert largest_area([]) == 0.0

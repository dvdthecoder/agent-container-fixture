"""Tests for geometry using the new naming convention."""

import math

from geometry import area_circle, area_rectangle, perimeter_circle, perimeter_rectangle


class TestAreaRectangle:
    def test_basic(self):
        assert area_rectangle(3, 4) == 12.0

    def test_square(self):
        assert area_rectangle(5, 5) == 25.0

    def test_zero(self):
        assert area_rectangle(0, 10) == 0.0


class TestAreaCircle:
    def test_unit(self):
        assert abs(area_circle(1) - math.pi) < 1e-9

    def test_radius_3(self):
        assert abs(area_circle(3) - 9 * math.pi) < 1e-9


class TestPerimeterRectangle:
    def test_basic(self):
        assert perimeter_rectangle(3, 4) == 14.0

    def test_square(self):
        assert perimeter_rectangle(5, 5) == 20.0


class TestPerimeterCircle:
    def test_unit(self):
        assert abs(perimeter_circle(1) - 2 * math.pi) < 1e-9

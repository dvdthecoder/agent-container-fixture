"""Tests for statslib — mean, median, variance."""

import pytest

from statslib import mean, median, variance


class TestMean:
    def test_basic(self):
        assert mean([1, 2, 3, 4, 5]) == 3.0

    def test_single(self):
        assert mean([42]) == 42.0

    def test_floats(self):
        assert abs(mean([1.5, 2.5, 3.0]) - 7.0 / 3) < 1e-9

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mean([])


class TestMedian:
    def test_odd_length(self):
        assert median([3, 1, 2]) == 2.0

    def test_even_length(self):
        assert median([1, 2, 3, 4]) == 2.5

    def test_single(self):
        assert median([7]) == 7.0

    def test_presorted(self):
        assert median([10, 20, 30, 40, 50]) == 30.0

    def test_unsorted(self):
        assert median([5, 1, 4, 2, 3]) == 3.0


class TestVariance:
    def test_basic(self):
        # population variance of [2,4,4,4,5,5,7,9] = 4.0
        assert abs(variance([2, 4, 4, 4, 5, 5, 7, 9]) - 4.0) < 1e-9

    def test_uniform(self):
        assert variance([5, 5, 5, 5]) == 0.0

    def test_single(self):
        assert variance([42]) == 0.0

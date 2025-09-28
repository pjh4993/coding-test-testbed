"""Test the solutions."""

import pytest

from trials.sorting_searching.merge_intervals import solution
from utils.runner import run_and_assert


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ],
)
def test_merge_intervals(intervals, expected):
    run_and_assert(solution, (intervals,), expected)

"""Test the solutions."""

import pytest

from trials.sorting_searching.sort_colors import solution
from utils.runner import run_and_assert


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ],
)
def test_sort_colors(nums, expected):
    run_and_assert(solution, (nums,), expected)

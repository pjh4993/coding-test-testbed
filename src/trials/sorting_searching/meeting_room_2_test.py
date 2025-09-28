"""Test the solutions."""

import pytest

from trials.sorting_searching.meeting_room_2 import solution
from utils.runner import run_and_assert


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[0, 30], [5, 10], [15, 20]], 2),
    ],
)
def test_meeting_room_2(intervals, expected):
    run_and_assert(solution, (intervals,), expected)

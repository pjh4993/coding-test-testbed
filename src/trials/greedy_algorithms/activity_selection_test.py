"""Activity Selection Problem Test."""

from trials.greedy_algorithms.activity_selection import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="greedy_algorithms/activity_selection.parquet",
    input_keys=["activities"],
    expected_key="expected",
)
def test_activity_selection(activities, expected, description):
    """Test activity selection."""

    run_and_assert(solution, (activities,), expected, description)

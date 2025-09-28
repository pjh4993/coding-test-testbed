"""Test the solutions."""

from trials.sorting_searching.search_in_rotated_sorted import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="sorting_searching/search_in_rotated_sorted.parquet",
    input_keys=["nums", "target"],
    expected_key="expected",
)
def test_search_in_rotated_sorted(nums, target, expected, description):
    run_and_assert(solution, (nums, target), expected, description)

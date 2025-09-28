"""Test the solutions using Parquet test data."""

from trials.sorting_searching.kth_largest_element import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="sorting_searching/kth_largest_element.parquet",
    input_keys=["nums", "k"],
    expected_key="expected",
)
def test_kth_largest_element_large(nums, k, expected, description):
    """Test kth largest element with large datasets from Parquet file."""

    run_and_assert(solution, (nums, k), expected, description)

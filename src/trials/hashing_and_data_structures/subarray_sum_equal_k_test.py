"""Subarray sum equal to k test."""

from trials.hashing_and_data_structures.subarray_sum_equal_k import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="hashing_and_data_structures/subarray_sum_equal_k.parquet",
    input_keys=["nums", "k"],
    expected_key="expected",
)
def test_subarray_sum_equal_k(nums, k, expected, description):
    """Test subarray sum equal to k."""

    run_and_assert(solution, (nums, k), expected, description)

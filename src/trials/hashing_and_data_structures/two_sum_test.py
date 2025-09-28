"""Test the solutions."""

from trials.hashing_and_data_structures.two_sum import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="hashing_and_data_structures/two_sum.parquet",
    input_keys=["nums", "target"],
    expected_key="expected",
)
def test_two_sum(nums, target, expected, description):
    """Test two sum with large datasets from Parquet file."""

    run_and_assert(solution, (nums, target), expected, description)

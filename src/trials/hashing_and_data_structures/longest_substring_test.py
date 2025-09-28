"""Longest substring test."""

from trials.hashing_and_data_structures.longest_substring import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="hashing_and_data_structures/longest_substring.parquet",
    input_keys=["s"],
    expected_key="expected",
)
def test_longest_substring(s, expected, description):
    """Test longest substring."""

    run_and_assert(solution, (s,), expected, description)

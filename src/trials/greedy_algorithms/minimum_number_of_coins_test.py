"""Minimum Number of Coins Test."""

from trials.greedy_algorithms.minimum_number_of_coins import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="greedy_algorithms/minimum_number_of_coins.parquet",
    input_keys=["denominations", "amount"],
    expected_key="expected",
)
def test_minimum_number_of_coins(denominations, amount, expected, description):
    """Test minimum number of coins."""

    run_and_assert(solution, (denominations, amount), expected, description)

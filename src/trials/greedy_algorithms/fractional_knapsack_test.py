"""Fractional Knapsack Test."""

from trials.greedy_algorithms.fractional_knapsack import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="greedy_algorithms/fractional_knapsack.parquet",
    input_keys=["weights", "values", "capacity"],
    expected_key="expected",
)
def test_fractional_knapsack(weights, values, capacity, expected, description):
    """Test fractional knapsack."""

    run_and_assert(solution, (weights, values, capacity), expected, description)

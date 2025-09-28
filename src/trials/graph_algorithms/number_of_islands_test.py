# -*- coding: utf-8 -*-
"""Number of Islands Problem Test."""

from trials.graph_algorithms.number_of_islands import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="graph_algorithms/number_of_islands.parquet",
    input_keys=["grid"],
    expected_key="expected",
)
def test_number_of_islands(grid, expected, description):
    """Test number of islands."""

    run_and_assert(solution, (grid,), expected, description)

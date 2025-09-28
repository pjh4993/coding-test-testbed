# -*- coding: utf-8 -*-
"""Detect Cycle Undirected Problem Test."""

from trials.graph_algorithms.detect_cycle_undirected import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="graph_algorithms/detect_cycle_undirected.parquet",
    input_keys=["n", "edges"],
    expected_key="expected",
)
def test_detect_cycle_undirected(n, edges, expected, description):
    """Test detect cycle undirected."""

    run_and_assert(solution, (n, edges), expected, description)

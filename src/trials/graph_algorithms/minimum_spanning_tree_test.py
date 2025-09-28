# -*- coding: utf-8 -*-
"""Minimum Spanning Tree Problem Test."""

from trials.graph_algorithms.minimum_spanning_tree import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="graph_algorithms/minimum_spanning_tree.parquet",
    input_keys=["n", "edges"],
    expected_key="expected",
)
def test_minimum_spanning_tree(n, edges, expected, description):
    """Test minimum spanning tree."""

    run_and_assert(solution, (n, edges), expected, description)

# -*- coding: utf-8 -*-
"""Shortest Path Dijkstra Problem Test."""

from trials.graph_algorithms.shortest_path_dijkstra import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="graph_algorithms/shortest_path_dijkstra.parquet",
    input_keys=["n", "edges", "s"],
    expected_key="expected",
)
def test_shortest_path_dijkstra(n, edges, s, expected, description):
    """Test shortest path Dijkstra."""

    run_and_assert(solution, (n, edges, s), expected, description)

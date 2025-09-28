# -*- coding: utf-8 -*-
"""Shortest Path Dijkstra Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_dijkstra_test():
    """Basic Dijkstra test case."""
    return TestCase(
        description="Basic Dijkstra example",
        expected=[0, 2, 3, 9, 6],
        inputs={
            "n": 5,
            "edges": [(0, 1, 2), (0, 2, 4), (1, 2, 1), (1, 3, 7), (2, 4, 3)],
            "s": 0,
        },
    )


def _single_node_test():
    """Single node test case."""
    return TestCase(
        description="Single node",
        expected=[0],
        inputs={
            "n": 1,
            "edges": [],
            "s": 0,
        },
    )


def _no_edges_test():
    """No edges test case."""
    return TestCase(
        description="No edges",
        expected=[0, float("inf"), float("inf")],
        inputs={
            "n": 3,
            "edges": [],
            "s": 0,
        },
    )


def _disconnected_graph_test():
    """Disconnected graph test case."""
    return TestCase(
        description="Disconnected graph",
        expected=[0, float("inf"), 5],
        inputs={
            "n": 3,
            "edges": [(0, 1, 2), (2, 2, 5)],
            "s": 0,
        },
    )


def generate_test_data():
    """Generate shortest path Dijkstra test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_dijkstra_test),
            TestDataGeneratorConfig(generator_function=_single_node_test),
            TestDataGeneratorConfig(generator_function=_no_edges_test),
            TestDataGeneratorConfig(generator_function=_disconnected_graph_test),
        ],
        "graph_algorithms/shortest_path_dijkstra.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

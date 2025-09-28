# -*- coding: utf-8 -*-
"""Minimum Spanning Tree Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_mst_test():
    """Basic MST test case."""
    return TestCase(
        description="Basic MST example",
        expected=4,
        inputs={
            "n": 4,
            "edges": [(0, 1, 1), (1, 2, 2), (0, 2, 2), (2, 3, 1), (1, 3, 3)],
        },
    )


def _single_node_test():
    """Single node test case."""
    return TestCase(
        description="Single node",
        expected=0,
        inputs={
            "n": 1,
            "edges": [],
        },
    )


def _two_nodes_test():
    """Two nodes test case."""
    return TestCase(
        description="Two nodes",
        expected=5,
        inputs={
            "n": 2,
            "edges": [(0, 1, 5)],
        },
    )


def _triangle_graph_test():
    """Triangle graph test case."""
    return TestCase(
        description="Triangle graph",
        expected=3,
        inputs={
            "n": 3,
            "edges": [(0, 1, 1), (1, 2, 2), (0, 2, 3)],
        },
    )


def _complete_graph_test():
    """Complete graph test case."""
    return TestCase(
        description="Complete graph",
        expected=2,
        inputs={
            "n": 3,
            "edges": [(0, 1, 1), (0, 2, 2), (1, 2, 1)],
        },
    )


def generate_test_data():
    """Generate minimum spanning tree test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_mst_test),
            TestDataGeneratorConfig(generator_function=_single_node_test),
            TestDataGeneratorConfig(generator_function=_two_nodes_test),
            TestDataGeneratorConfig(generator_function=_triangle_graph_test),
            TestDataGeneratorConfig(generator_function=_complete_graph_test),
        ],
        "graph_algorithms/minimum_spanning_tree.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

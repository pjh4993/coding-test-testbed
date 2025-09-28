# -*- coding: utf-8 -*-
"""Detect Cycle Undirected Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_cycle_test():
    """Basic cycle detection test case."""
    return TestCase(
        description="Basic cycle example",
        expected=True,
        inputs={
            "n": 4,
            "edges": [(0, 1), (1, 2), (2, 0), (2, 3)],
        },
    )


def _no_cycle_tree_test():
    """No cycle (tree) test case."""
    return TestCase(
        description="No cycle (tree)",
        expected=False,
        inputs={
            "n": 4,
            "edges": [(0, 1), (1, 2), (2, 3)],
        },
    )


def _single_node_test():
    """Single node test case."""
    return TestCase(
        description="Single node",
        expected=False,
        inputs={
            "n": 1,
            "edges": [],
        },
    )


def _two_nodes_test():
    """Two nodes with edge test case."""
    return TestCase(
        description="Two nodes with edge",
        expected=False,
        inputs={
            "n": 2,
            "edges": [(0, 1)],
        },
    )


def _self_loop_test():
    """Self-loop test case."""
    return TestCase(
        description="Self-loop",
        expected=True,
        inputs={
            "n": 2,
            "edges": [(0, 0)],
        },
    )


def generate_test_data():
    """Generate detect cycle undirected test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_cycle_test),
            TestDataGeneratorConfig(generator_function=_no_cycle_tree_test),
            TestDataGeneratorConfig(generator_function=_single_node_test),
            TestDataGeneratorConfig(generator_function=_two_nodes_test),
            TestDataGeneratorConfig(generator_function=_self_loop_test),
        ],
        "graph_algorithms/detect_cycle_undirected.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

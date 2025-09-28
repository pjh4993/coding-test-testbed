# -*- coding: utf-8 -*-
"""Number of Islands Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_islands_test():
    """Basic islands test case."""
    return TestCase(
        description="Basic islands example",
        expected=3,
        inputs={
            "grid": [
                ["1", "1", "0", "0"],
                ["1", "0", "0", "1"],
                ["0", "0", "1", "1"],
                ["0", "0", "0", "0"],
            ],
        },
    )


def _single_island_test():
    """Single island test case."""
    return TestCase(
        description="Single island",
        expected=1,
        inputs={
            "grid": [
                ["1", "1"],
                ["1", "1"],
            ],
        },
    )


def _no_islands_test():
    """No islands test case."""
    return TestCase(
        description="No islands",
        expected=0,
        inputs={
            "grid": [
                ["0", "0"],
                ["0", "0"],
            ],
        },
    )


def _single_cell_island_test():
    """Single cell island test case."""
    return TestCase(
        description="Single cell island",
        expected=1,
        inputs={
            "grid": [["1"]],
        },
    )


def _single_cell_water_test():
    """Single cell water test case."""
    return TestCase(
        description="Single cell water",
        expected=0,
        inputs={
            "grid": [["0"]],
        },
    )


def _diagonal_islands_test():
    """Diagonal islands test case."""
    return TestCase(
        description="Diagonal islands",
        expected=5,
        inputs={
            "grid": [
                ["1", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "1"],
            ],
        },
    )


def generate_test_data():
    """Generate number of islands test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_islands_test),
            TestDataGeneratorConfig(generator_function=_single_island_test),
            TestDataGeneratorConfig(generator_function=_no_islands_test),
            TestDataGeneratorConfig(generator_function=_single_cell_island_test),
            TestDataGeneratorConfig(generator_function=_single_cell_water_test),
            TestDataGeneratorConfig(generator_function=_diagonal_islands_test),
        ],
        "graph_algorithms/number_of_islands.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

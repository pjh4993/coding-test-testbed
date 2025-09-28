"""Activity Selection Problem Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_activity_selection_test_data():
    """Generate basic activity selection test data."""
    return TestCase(
        description="Basic activity selection",
        expected=4,
        inputs={
            "activities": [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)],
        },
    )


def _back_to_back_intervals():
    """Back-to-back intervals should all be chosen."""
    return TestCase(
        description="Back-to-back intervals",
        expected=5,
        inputs={
            "activities": [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],
        },
    )


def _heavy_overlap_intervals():
    """Many overlapping intervals; optimal is to pick the earliest finishing chain."""
    return TestCase(
        description="Heavily overlapping intervals",
        expected=3,
        inputs={
            "activities": [(1, 10), (2, 3), (3, 4), (4, 5)],
        },
    )


def _single_activity():
    """Single activity edge case."""
    return TestCase(
        description="Single activity",
        expected=1,
        inputs={
            "activities": [(10, 20)],
        },
    )


def generate_test_data():
    """Generate activity selection test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic_activity_selection_test_data),
            TestDataGeneratorConfig(generator_function=_back_to_back_intervals),
            TestDataGeneratorConfig(generator_function=_heavy_overlap_intervals),
            TestDataGeneratorConfig(generator_function=_single_activity),
        ],
        "greedy_algorithms/activity_selection.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

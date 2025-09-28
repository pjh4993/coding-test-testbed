"""Test data generator for two sum."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_two_sum_test_data():
    """Generate basic two sum test data."""

    return TestCase(
        description="Basic two sum test",
        expected=[0, 1],
        inputs={
            "nums": [2, 7, 11, 15],
            "target": 9,
        },
    )


def _two_sum_with_negative_numbers_test_data():
    """Generate two sum with negative numbers test data."""

    return TestCase(
        description="Two sum with negative numbers test",
        expected=[2, 4],
        inputs={
            "nums": [-1, -2, -3, -4, -5],
            "target": -8,
        },
    )


def _large_array_performance_test_data():
    """Generate large array performance test data."""

    return TestCase(
        description="Large array performance test",
        expected=[48, 49],
        inputs={
            "nums": list(range(0, 50)),
            "target": 97,
        },
    )


def _edge_case_same_number_twice_test_data():
    """Generate edge case same number twice test data."""

    return TestCase(
        description="Edge case same number twice test",
        expected=[0, 1],
        inputs={
            "nums": [3, 3],
            "target": 6,
        },
    )


def generate_test_data():
    """Generate two sum test data."""

    configs = [
        TestDataGeneratorConfig(generator_function=_basic_two_sum_test_data),
        TestDataGeneratorConfig(
            generator_function=_two_sum_with_negative_numbers_test_data
        ),
        TestDataGeneratorConfig(generator_function=_large_array_performance_test_data),
        TestDataGeneratorConfig(
            generator_function=_edge_case_same_number_twice_test_data
        ),
    ]

    TestDataGenerator.generate_test_data(
        configs, "hashing_and_data_structures/two_sum.parquet"
    )


if __name__ == "__main__":
    generate_test_data()

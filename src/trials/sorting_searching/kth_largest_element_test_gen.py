"""Test data generator for kth largest element."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_kth_largest_element_test_data():
    """Generate basic kth largest element test data."""

    return TestCase(
        description="Basic kth largest element test",
        expected=5,
        inputs={
            "nums": [3, 2, 1, 5, 6, 4],
            "k": 2,
        },
    )


def _single_element_array_test_data():
    """Generate single element array test data."""

    return TestCase(
        description="Single element array test",
        expected=1,
        inputs={
            "nums": [1],
            "k": 1,
        },
    )


def _large_array_with_duplicates_test_data():
    """Generate large array with duplicates test data."""

    return TestCase(
        description="Large array with duplicates test",
        expected=4,
        inputs={
            "nums": [3, 2, 3, 1, 2, 4, 5, 5, 6],
            "k": 4,
        },
    )


def _very_large_array_performance_test_data():
    """Generate very large array performance test data."""

    return TestCase(
        description="Very large array performance test",
        expected=51,
        inputs={
            "nums": list(range(101)),
            "k": 50,
        },
    )


def _large_array_with_negative_numbers_test_data():
    """Generate large array with negative numbers test data."""

    return TestCase(
        description="Large array with negative numbers test",
        expected=-925,
        inputs={
            "nums": list(range(-1000, -900)),
            "k": 25,
        },
    )


def _edge_case_k_equals_array_length_test_data():
    """Generate edge case k equals array test data."""

    return TestCase(
        description="Edge case k equals array test",
        expected=1,
        inputs={
            "nums": [5, 2, 8, 1, 9, 3, 7, 4, 6],
            "k": 9,
        },
    )


def generate_test_data():
    """Generate kth largest element test data."""

    configs = [
        TestDataGeneratorConfig(
            generator_function=_basic_kth_largest_element_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_basic_kth_largest_element_test_data
        ),
        TestDataGeneratorConfig(generator_function=_single_element_array_test_data),
        TestDataGeneratorConfig(
            generator_function=_large_array_with_duplicates_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_very_large_array_performance_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_large_array_with_negative_numbers_test_data
        ),
    ]

    TestDataGenerator.generate_test_data(
        configs, "sorting_searching/kth_largest_element.parquet"
    )


if __name__ == "__main__":
    generate_test_data()

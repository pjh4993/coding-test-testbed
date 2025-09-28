"""Test data generator for search in rotated sorted array."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _target_found_in_rotated_array_test_data():
    """Generate target found in rotated array test data."""

    return TestCase(
        description="Target found in rotated array test",
        expected=4,
        inputs={
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
        },
    )


def _target_not_found_in_rotated_array_test_data():
    """Generate target not found in rotated array test data."""

    return TestCase(
        description="Target not found in rotated array test",
        expected=-1,
        inputs={
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
        },
    )


def _single_element_array_test_data():
    """Generate single element array test data."""

    return TestCase(
        description="Single element array test",
        expected=0,
        inputs={
            "nums": [1],
            "target": 1,
        },
    )


def _single_element_array_with_target_not_found_test_data():
    """Generate single element array with target not found test data."""

    return TestCase(
        description="Single element array with target not found test",
        expected=-1,
        inputs={
            "nums": [1],
            "target": 2,
        },
    )


def _large_rotated_array_performance_test_data():
    """Generate large rotated array performance test data."""

    return TestCase(
        description="Large rotated array performance test",
        expected=25,
        inputs={
            "nums": list(range(50, 101)),
            "target": 75,
        },
    )


def _large_rotated_array_target_not_found_performance_test_data():
    """Generate large rotated array target not found performance test data."""

    return TestCase(
        description="Large rotated array target not found performance test",
        expected=-1,
        inputs={
            "nums": list(range(50, 101)),
            "target": 101,
        },
    )


def _array_with_negative_numbers_test_data():
    """Generate array with negative numbers test data."""

    return TestCase(
        description="Array with negative numbers test",
        expected=7,
        inputs={
            "nums": list(range(-10, 100)),
            "target": -3,
        },
    )


def generate_test_data():
    """Generate search in rotated sorted test data."""

    configs = [
        TestDataGeneratorConfig(
            generator_function=_target_found_in_rotated_array_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_target_not_found_in_rotated_array_test_data
        ),
        TestDataGeneratorConfig(generator_function=_single_element_array_test_data),
        TestDataGeneratorConfig(
            generator_function=_single_element_array_with_target_not_found_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_large_rotated_array_performance_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_large_rotated_array_target_not_found_performance_test_data
        ),
        TestDataGeneratorConfig(
            generator_function=_array_with_negative_numbers_test_data
        ),
    ]

    TestDataGenerator.generate_test_data(
        configs, "sorting_searching/search_in_rotated_sorted.parquet"
    )


if __name__ == "__main__":
    generate_test_data()

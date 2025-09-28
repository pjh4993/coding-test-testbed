"""Subarray sum equal to k test generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_subarray_sum_equal_k_test_data():
    """Generate basic subarray sum equal to k test data."""

    return TestCase(
        description="Basic subarray sum equal to k",
        expected=2,
        inputs={
            "nums": [1, 2, 3],
            "k": 3,
        },
    )


def _edge_cases_test_data():
    """Generate edge cases test data."""

    test_cases = [
        TestCase(
            description="Empty array",
            expected=0,
            inputs={"nums": [], "k": 0},
        ),
        TestCase(
            description="Single element matching",
            expected=1,
            inputs={"nums": [5], "k": 5},
        ),
        TestCase(
            description="Single element not matching",
            expected=0,
            inputs={"nums": [3], "k": 5},
        ),
        TestCase(
            description="Zero target with no zero subarrays",
            expected=0,
            inputs={"nums": [1, 2, 3], "k": 0},
        ),
    ]

    return test_cases


def _negative_numbers_test_data():
    """Generate negative numbers test data."""

    test_cases = [
        TestCase(
            description="Mixed positive/negative with zero target",
            expected=3,
            inputs={"nums": [1, -1, 0], "k": 0},
        ),
        TestCase(
            description="All negative numbers",
            expected=2,
            inputs={"nums": [-1, -2, -3], "k": -3},
        ),
        TestCase(
            description="Negative target",
            expected=0,
            inputs={"nums": [1, 2, 3], "k": -1},
        ),
    ]

    return test_cases


def _zeroes_test_data():
    """Generate zeroes test data."""

    test_cases = [
        TestCase(
            description="All zeroes with zero target",
            expected=6,
            inputs={"nums": [0, 0, 0], "k": 0},
        ),
        TestCase(
            description="Zero target with single zero",
            expected=1,
            inputs={"nums": [1, 0, 1], "k": 0},
        ),
    ]

    return test_cases


def _duplicate_elements_test_data():
    """Generate duplicate elements test data."""

    test_cases = [
        TestCase(
            description="All same elements",
            expected=2,
            inputs={"nums": [2, 2, 2], "k": 4},
        ),
        TestCase(
            description="Repeated pattern",
            expected=2,
            inputs={"nums": [1, 1, 1], "k": 2},
        ),
    ]

    return test_cases


def _complex_cases_test_data():
    """Generate complex cases test data."""

    test_cases = [
        TestCase(
            description="LeetCode example 1",
            expected=2,
            inputs={"nums": [1, 1, 1], "k": 2},
        ),
        TestCase(
            description="All elements sum",
            expected=1,
            inputs={"nums": [1, 2, 3], "k": 6},
        ),
        TestCase(
            description="No matches",
            expected=0,
            inputs={"nums": [1, 2, 3], "k": 10},
        ),
        TestCase(
            description="Overlapping subarrays",
            expected=4,
            inputs={"nums": [1, 2, 1, 2, 1], "k": 3},
        ),
    ]

    return test_cases


def generate_test_data():
    """Generate test data."""

    configs = [
        TestDataGeneratorConfig(generator_function=_basic_subarray_sum_equal_k_test_data),
        TestDataGeneratorConfig(generator_function=_edge_cases_test_data),
        TestDataGeneratorConfig(generator_function=_negative_numbers_test_data),
        TestDataGeneratorConfig(generator_function=_zeroes_test_data),
        TestDataGeneratorConfig(generator_function=_duplicate_elements_test_data),
        TestDataGeneratorConfig(generator_function=_complex_cases_test_data),
    ]

    TestDataGenerator.generate_test_data(
        configs, "hashing_and_data_structures/subarray_sum_equal_k.parquet"
    )


if __name__ == "__main__":
    generate_test_data()

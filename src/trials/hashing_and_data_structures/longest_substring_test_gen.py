"""Longest substring test generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic_longest_substring_test_data():
    """Generate basic longest substring test data."""

    return TestCase(
        description="Basic longest substring test",
        expected=3,
        inputs={
            "s": "abcabcbb",
        },
    )


def generate_test_data():
    """Generate test data."""

    test_data_generator = TestDataGenerator()
    test_data_generator.generate_test_data(
        [
            TestDataGeneratorConfig(
                generator_function=_basic_longest_substring_test_data,
            )
        ],
        "hashing_and_data_structures/longest_substring.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

"""Huffman Coding Test Generator.

Expected value is the optimal total merge cost (a.k.a. sum of all internal edge weights),
which equals sum(freq_i * code_length_i) in the optimal Huffman tree.
This avoids comparing concrete codes which may differ while still being optimal.
"""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _classic_huffman():
    """Classic frequency set; optimal total cost is known: 224."""
    return TestCase(
        description="Classic Huffman frequencies",
        expected=224,
        inputs={
            "frequencies": {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45},
        },
    )


def _two_symbols():
    """Two-symbol edge case."""
    # Merge 1 + 1 -> cost 2
    return TestCase(
        description="Two symbols",
        expected=2,
        inputs={
            "frequencies": {"A": 1, "B": 1},
        },
    )


def _three_symbols():
    """Three symbols, small ints."""
    # Optimal total cost: 9
    return TestCase(
        description="Three symbols",
        expected=9,
        inputs={
            "frequencies": {"A": 1, "B": 2, "C": 3},
        },
    )


def _balanced_larger():
    """Larger balanced set."""
    # Optimal total cost for {10,20,30,40} is 190
    return TestCase(
        description="Balanced larger set",
        expected=190,
        inputs={
            "frequencies": {"x": 10, "y": 20, "z": 30, "w": 40},
        },
    )


def generate_test_data():
    """Generate Huffman coding test data."""
    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_classic_huffman),
            TestDataGeneratorConfig(generator_function=_two_symbols),
            TestDataGeneratorConfig(generator_function=_three_symbols),
            TestDataGeneratorConfig(generator_function=_balanced_larger),
        ],
        "greedy_algorithms/huffman_coding.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

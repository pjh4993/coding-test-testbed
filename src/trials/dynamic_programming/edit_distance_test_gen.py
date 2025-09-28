# -*- coding: utf-8 -*-
"""Edit Distance (Levenshtein) Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _both_empty_edge():
    return TestCase(description='"" -> "" (edge)', expected=0, inputs={"word1": "", "word2": ""})


def _identical_edge():
    return TestCase(
        description='"abc" -> "abc" (edge)', expected=0, inputs={"word1": "abc", "word2": "abc"}
    )


def _horse_ros():
    return TestCase(
        description='"horse" -> "ros"', expected=3, inputs={"word1": "horse", "word2": "ros"}
    )


def _intention_execution():
    return TestCase(
        description='"intention" -> "execution"',
        expected=5,
        inputs={"word1": "intention", "word2": "execution"},
    )


def _large_perf_replacements():
    """Large deterministic: 'a'*2000 -> 'b'*2000

    Transformation is pure replacements, distance = 2000.
    """
    n = 2000
    w1 = "a" * n
    w2 = "b" * n
    expected = n
    return TestCase(
        description=f'"a"*{n} -> "b"*{n} (large performance)',
        expected=expected,
        inputs={"word1": w1, "word2": w2},
    )


def generate_test_data():
    """Generate edit distance test data."""

    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_both_empty_edge),
            TestDataGeneratorConfig(generator_function=_identical_edge),
            TestDataGeneratorConfig(generator_function=_horse_ros),  # keep original classics
            TestDataGeneratorConfig(generator_function=_intention_execution),
            TestDataGeneratorConfig(generator_function=_large_perf_replacements),
        ],
        "dynamic_programming/edit_distance.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

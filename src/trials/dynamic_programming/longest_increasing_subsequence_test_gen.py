# -*- coding: utf-8 -*-
"""Longest Increasing Subsequence (Length) Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _empty_edge():
    # Edge: empty list -> LIS length 0
    return TestCase(description="empty (edge)", expected=0, inputs={"nums": []})


def _classic():
    return TestCase(
        description="[10,9,2,5,3,7,101,18]",
        expected=4,  # [2,3,7,101]
        inputs={"nums": [10, 9, 2, 5, 3, 7, 101, 18]},
    )


def _mix():
    return TestCase(
        description="[0,1,0,3,2,3]",
        expected=4,  # [0,1,2,3]
        inputs={"nums": [0, 1, 0, 3, 2, 3]},
    )


def _all_equal_edge():
    return TestCase(description="all equal (edge)", expected=1, inputs={"nums": [7, 7, 7, 7, 7]})


def _large_perf_increasing_then_reverse():
    """Large deterministic LIS length:

    nums = [1..5000] + [5000..1] -> LIS = 5000
    """

    inc = list(range(1, 5001))
    dec = list(range(5000, 0, -1))
    nums = inc + dec
    expected = 5000
    return TestCase(
        description=f"large inc+dec (len={len(nums)})",
        expected=expected,
        inputs={"nums": nums},
    )


def generate_test_data():
    """Generate longest increasing subsequence test data."""

    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_empty_edge),
            TestDataGeneratorConfig(generator_function=_classic),
            TestDataGeneratorConfig(generator_function=_mix),
            TestDataGeneratorConfig(generator_function=_all_equal_edge),
            TestDataGeneratorConfig(generator_function=_large_perf_increasing_then_reverse),
        ],
        "dynamic_programming/longest_increasing_subsequence.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

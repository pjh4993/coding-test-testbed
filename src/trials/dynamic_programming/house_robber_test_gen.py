# -*- coding: utf-8 -*-
"""House Robber Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _single():
    return TestCase(description="single element", expected=5, inputs={"nums": [5]})


def _basic1():
    return TestCase(description="[1,2,3,1]", expected=4, inputs={"nums": [1, 2, 3, 1]})


def _basic2():
    return TestCase(description="[2,7,9,3,1]", expected=12, inputs={"nums": [2, 7, 9, 3, 1]})


def _tie_break():
    return TestCase(description="[2,1,1,2] (pick ends)", expected=4, inputs={"nums": [2, 1, 1, 2]})


def _large_perf():
    """Large, deterministic optimum:

    Pattern [1, 1000] repeated N times -> optimal = 1000 * N (pick all 1000s).

    """

    N = 500  # total length = 1000
    nums = []
    for _ in range(N):
        nums.extend([1, 1000])
    expected = 1000 * N
    return TestCase(
        description=f"large alternating (len={len(nums)})", expected=expected, inputs={"nums": nums}
    )


def generate_test_data():
    """Generate house robber test data."""

    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_single),
            TestDataGeneratorConfig(generator_function=_basic1),
            TestDataGeneratorConfig(generator_function=_basic2),
            TestDataGeneratorConfig(generator_function=_tie_break),
            TestDataGeneratorConfig(generator_function=_large_perf),
        ],
        "dynamic_programming/house_robber.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

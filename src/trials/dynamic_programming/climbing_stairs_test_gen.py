# -*- coding: utf-8 -*-
"""Climbing Stairs Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _n0_edge():
    # Edge: 0 steps -> 1 way (do nothing)
    return TestCase(description="n=0 (edge)", expected=1, inputs={"n": 0})


def _n1():
    return TestCase(description="n=1 (base)", expected=1, inputs={"n": 1})


def _n2():
    return TestCase(description="n=2 (base)", expected=2, inputs={"n": 2})


def _n5():
    return TestCase(description="n=5 (Fibonacci-like)", expected=8, inputs={"n": 5})


def _n45_large_perf():
    # Large (but fits 32-bit): ways = Fib(n+1). For n=45 -> Fib(46) = 1836311903
    return TestCase(description="n=45 (large performance)", expected=1836311903, inputs={"n": 45})


def generate_test_data():
    """Generate climbing stairs test data."""

    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_n0_edge),
            TestDataGeneratorConfig(generator_function=_n1),
            TestDataGeneratorConfig(generator_function=_n2),
            TestDataGeneratorConfig(generator_function=_n5),
            TestDataGeneratorConfig(generator_function=_n45_large_perf),
        ],
        "dynamic_programming/climbing_stairs.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

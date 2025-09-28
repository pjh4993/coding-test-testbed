# -*- coding: utf-8 -*-
"""Coin Change (Min Coins) Test Generator."""

from utils.data_generator import TestCase, TestDataGenerator, TestDataGeneratorConfig


def _basic():
    return TestCase(
        description="coins=[1,2,5], amount=11",
        expected=3,  # 5 + 5 + 1
        inputs={"coins": [1, 2, 5], "amount": 11},
    )


def _impossible_edge():
    # Edge: gcd(coins)=2, amount odd -> impossible
    return TestCase(
        description="coins=[4,6], amount=7 (edge, impossible)",
        expected=-1,
        inputs={"coins": [4, 6], "amount": 7},
    )


def _zero_amount_edge():
    return TestCase(
        description="coins=[2,5], amount=0 (edge)",
        expected=0,
        inputs={"coins": [2, 5], "amount": 0},
    )


def _combo():
    return TestCase(
        description="coins=[1,3,4], amount=6",
        expected=2,  # 3 + 3
        inputs={"coins": [1, 3, 4], "amount": 6},
    )


def _large_perf():
    """Large but deterministic: canonical US-like coins -> greedy equals optimal.

    amount=10000 with [1,5,10,25] -> min coins = 10000//25 = 400
    """
    coins = [1, 5, 10, 25]
    amount = 10000
    expected = amount // 25  # 400
    return TestCase(
        description=f"large canonical coins amount={amount}",
        expected=expected,
        inputs={"coins": coins, "amount": amount},
    )


def generate_test_data():
    """Generate coin change test data."""

    TestDataGenerator.generate_test_data(
        [
            TestDataGeneratorConfig(generator_function=_basic),
            TestDataGeneratorConfig(generator_function=_impossible_edge),
            TestDataGeneratorConfig(generator_function=_zero_amount_edge),
            TestDataGeneratorConfig(generator_function=_combo),
            TestDataGeneratorConfig(generator_function=_large_perf),
        ],
        "dynamic_programming/coin_change.parquet",
    )


if __name__ == "__main__":
    generate_test_data()

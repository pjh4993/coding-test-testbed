# -*- coding: utf-8 -*-
"""Coin Change Test."""

from trials.dynamic_programming.coin_change import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="dynamic_programming/coin_change.parquet",
    input_keys=["coins", "amount"],
    expected_key="expected",
)
def test_coin_change(coins, amount, expected, description):
    """Test Coin Change."""

    run_and_assert(solution, (coins, amount), expected, description)

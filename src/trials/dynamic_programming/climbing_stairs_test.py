# -*- coding: utf-8 -*-
"""Climbing Stairs Test."""

from trials.dynamic_programming.climbing_stairs import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="dynamic_programming/climbing_stairs.parquet",
    input_keys=["n"],
    expected_key="expected",
)
def test_climbing_stairs(n, expected, description):
    """Test Climbing Stairs."""

    run_and_assert(solution, (n,), expected, description)

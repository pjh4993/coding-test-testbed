# -*- coding: utf-8 -*-
"""House Robber Test."""

from trials.dynamic_programming.house_robber import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="dynamic_programming/house_robber.parquet",
    input_keys=["nums"],
    expected_key="expected",
)
def test_house_robber(nums, expected, description):
    """Test House Robber."""

    run_and_assert(solution, (nums,), expected, description)

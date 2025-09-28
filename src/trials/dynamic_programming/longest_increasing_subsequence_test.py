# -*- coding: utf-8 -*-
"""Longest Increasing Subsequence Test."""

from trials.dynamic_programming.longest_increasing_subsequence import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="dynamic_programming/longest_increasing_subsequence.parquet",
    input_keys=["nums"],
    expected_key="expected",
)
def test_longest_increasing_subsequence(nums, expected, description):
    """Test Longest Increasing Subsequence."""

    run_and_assert(solution, (nums,), expected, description)

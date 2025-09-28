# -*- coding: utf-8 -*-
"""Edit Distance Test."""

from trials.dynamic_programming.edit_distance import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="dynamic_programming/edit_distance.parquet",
    input_keys=["word1", "word2"],
    expected_key="expected",
)
def test_edit_distance(word1, word2, expected, description):
    """Test Edit Distance."""

    run_and_assert(solution, (word1, word2), expected, description)

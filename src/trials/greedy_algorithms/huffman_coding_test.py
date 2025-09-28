"""Huffman Coding Test."""

from trials.greedy_algorithms.huffman_coding import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="greedy_algorithms/huffman_coding.parquet",
    input_keys=["frequencies"],
    expected_key="expected",
)
def test_huffman_coding(frequencies, expected, description):
    """Test Huffman Coding."""

    run_and_assert(solution, (frequencies,), expected, description)

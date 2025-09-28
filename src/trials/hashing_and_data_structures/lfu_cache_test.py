"""LFU Cache Test."""

from trials.hashing_and_data_structures.lfu_cache import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


@TestDataLoader.parametrize(
    path_or_fixture="hashing_and_data_structures/lfu_cache.parquet",
    input_keys=["size", "cmds", "args"],
    expected_key="expected",
)
def test_lfu_cache(size, cmds, args, expected, description):
    """Test LFU Cache."""

    run_and_assert(solution, (size, cmds, args), expected, description)

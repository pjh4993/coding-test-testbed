"""Group Anagrams Test."""

from trials.hashing_and_data_structures.group_anagrams import solution
from utils.data_loader import TestDataLoader
from utils.runner import run_and_assert


def validator(expected: list[list[str]], actual: list[list[str]]) -> bool:
    """Validate group anagrams."""

    sorted_expected = sorted(expected, key=lambda x: sorted(x))
    sorted_actual = sorted(actual, key=lambda x: sorted(x))

    return sorted_expected == sorted_actual


@TestDataLoader.parametrize(
    path_or_fixture="hashing_and_data_structures/group_anagrams.parquet",
    input_keys=["strs"],
    expected_key="expected",
)
def test_group_anagrams(strs, expected, description):
    """Test group anagrams."""

    run_and_assert(solution, (strs,), expected, description)

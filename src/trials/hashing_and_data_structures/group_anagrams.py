"""Group Anagrams.

Given an array of strings, group the anagrams together.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from collections import defaultdict


def _anagram_signature(s: str) -> str:
    """Generate an anagram signature for a string.

    Args:
        s: str

    Returns:
        str

    """

    return "".join(sorted(s))


def solution(strs: list[str]) -> list[list[str]]:
    """Group Anagrams.

    Args:
        strs: list[str]

    Returns:
        list[list[str]]

    """

    anagram_groups = defaultdict(list)

    for element in strs:
        signature = _anagram_signature(element)
        anagram_groups[signature].append(element)

    return list(anagram_groups.values())

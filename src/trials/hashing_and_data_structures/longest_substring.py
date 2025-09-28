"""Longest substring Without Repeating Characters.

Find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""


def solution(s: str) -> int:
    """Find the length of the longest substring without repeating characters.

    Args:
        s: str

    Returns:
        int: The length of the longest substring without repeating characters.

    """

    last_index_map = {}
    left_index, best_length = 0, 0

    for idx, char in enumerate(s):
        if char in last_index_map:
            left_index = last_index_map[char] + 1

        last_index_map[char] = idx
        best_length = max(best_length, idx - left_index + 1)

    return best_length

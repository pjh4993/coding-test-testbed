# -*- coding: utf-8 -*-
"""Edit Distance.

Given two strings, find the minimum number of operations to convert one string to the other.

Example:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: horse -> rorse (replace 'h' with 'r'), rorse -> rose (remove 'r'), rose -> ros (remove 'e')

"""


def _trivial_solution(word1: str, word2: str) -> int:
    """Trivial solution.

    Args:
        word1: str
        word2: str
    """

    if word1 == word2:
        return 0

    if len(word1) == 0:
        return len(word2)

    if len(word2) == 0:
        return len(word1)

    return None


def _fill_trivial_solution(states: list[list[int]], x_state_size: int, y_state_size: int) -> None:
    """Fill trivial solution.

    Args:
        states: list[list[int]]
        x_state_size: int
        y_state_size: int

    """

    for i in range(x_state_size):
        states[i][0] = i

    for i in range(y_state_size):
        states[0][i] = i

    return states


def solution(word1: str, word2: str) -> int:
    """Edit Distance.

    Args:
        word1: str
        word2: str

    Returns:
        int: minimum number of operations to convert one string to the other

    """

    trivial_solution = _trivial_solution(word1, word2)
    if trivial_solution is not None:
        return trivial_solution

    x_state_size = len(word1)
    y_state_size = len(word2)
    states = [[0] * (y_state_size + 1) for _ in range(x_state_size + 1)]
    states = _fill_trivial_solution(states, x_state_size + 1, y_state_size + 1)

    for i in range(1, x_state_size + 1):
        for j in range(1, y_state_size + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            states[i][j] = min(
                states[i - 1][j] + 1,
                states[i][j - 1] + 1,
                states[i - 1][j - 1] + cost,
            )

    return states[x_state_size][y_state_size]

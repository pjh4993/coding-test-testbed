# -*- coding: utf-8 -*-
"""Longest Increasing Subsequence.

Given an integer array, find the length of the longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 (2,3,7,101)

"""

from bisect import bisect_left


def _trivial_solution(nums: list[int]) -> int:
    """Trivial solution.

    Args:
        nums: list[int]

    """

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    return None


def solution(nums: list[int]) -> int:
    """Longest Increasing Subsequence.

    Args:
        nums: list[int]

    """

    return solution_dp(nums)


def solution_patience_sorting(nums: list[int]) -> int:
    """Longest Increasing Subsequence.

    Args:
        nums: list[int]

    """

    tails = []
    for x in nums:
        i = bisect_left(tails, x)

        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x

    return len(tails)


def solution_dp(nums: list[int]) -> int:
    """Longest Increasing Subsequence.

    Args:
        nums: list[int]

    Returns:
        int: length of the longest increasing subsequence

    """

    trivial_solution = _trivial_solution(nums)
    if trivial_solution is not None:
        return trivial_solution

    state_size = len(nums)
    states = [1] * state_size

    for i in range(1, state_size):
        states[i] = 1 + max((states[j] for j in range(i) if nums[j] < nums[i]), default=0)

    return max(states)

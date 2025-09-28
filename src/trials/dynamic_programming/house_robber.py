# -*- coding: utf-8 -*-
"""House Robber.

You are a robber planning to rob houses along a street. Each house has some amount of money, but you cannot rob two adjacent houses. Find the maximum amount you can rob.

Example:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob houses 2 + 9 + 1

"""


def _trivial_solution(nums: list[int]) -> int:
    """Trivial solution.

    Args:
        nums: list[int]

    """

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    if len(nums) == 3:
        return max(nums[1], nums[0] + nums[2])

    return None


def solution(nums: list[int]) -> int:
    """House Robber.

    Args:
        nums: list[int]

    Returns:
        int

    """

    trivial_solution = _trivial_solution(nums)
    if trivial_solution is not None:
        return trivial_solution

    state_size = max(len(nums), 3)

    states = [0] * state_size
    states[0] = nums[0]
    states[1] = max(nums[0], nums[1])
    states[2] = max(nums[1], nums[0] + nums[2])

    for i in range(3, len(nums)):
        states[i] = max(states[i - 1], states[i - 2] + nums[i])

    return states[len(nums) - 1]

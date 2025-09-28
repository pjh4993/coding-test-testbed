"""Subarray sum equal to k.

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals k.

Example 1:

Input: nums = [1,2,3], k = 3
Output: 2

Problem type:
Counting / Frequency

"""

from collections import defaultdict


def solution(nums: list[int], k: int) -> int:
    """Subarray sum equal to k.

    Args:
        nums: list[int]
        k: int

    Returns:
        int

    """

    count = 0
    prefix_sum = 0
    prefix_sum_freq_map = defaultdict(int)
    prefix_sum_freq_map[0] = 1

    for num in nums:
        prefix_sum += num
        count += prefix_sum_freq_map[prefix_sum - k]
        prefix_sum_freq_map[prefix_sum] += 1

    return count

"""Kth Largest Element in array.

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

"""


def solution(nums: list[int], k: int) -> int:
    """Find the kth largest element in the array.

    Args:
        nums: List[int]
        k: int

    Returns:
        int

    """

    target = len(nums) - k
    left_idx, right_idx = 0, len(nums) - 1

    while True:
        pivot_value = nums[right_idx]
        pivot_idx = left_idx

        # partition the array by the pivot
        for i in range(left_idx, right_idx):
            if nums[i] <= pivot_value:
                nums[pivot_idx], nums[i] = nums[i], nums[pivot_idx]
                pivot_idx += 1
        nums[pivot_idx], nums[right_idx] = nums[right_idx], nums[pivot_idx]

        # if the pivot is the target, return the pivot
        if pivot_idx == target:
            return nums[pivot_idx]
        # if the pivot is less than the target, move the left pointer to the right
        elif pivot_idx < target:
            left_idx = pivot_idx + 1
        # if the pivot is greater than the target, move the right pointer to the left
        else:
            right_idx = pivot_idx - 1

    raise ValueError("Kth largest element not found")

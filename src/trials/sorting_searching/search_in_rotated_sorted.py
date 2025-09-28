"""Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


"""


def is_sorted(left_value: int, right_value: int) -> bool:
    return left_value <= right_value


def is_in_range(left_value: int, right_value: int, target: int) -> bool:
    return left_value <= target <= right_value


def solution(nums: list[int], target: int) -> int:
    """Search in the rotated sorted array.

    Args:
        nums: List[int]
        target: int

    Returns:
        int

    """

    left_idx, right_idx = 0, len(nums) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_value = nums[mid_idx]

        if target == mid_value:
            return mid_idx

        is_left_sorted = is_sorted(nums[left_idx], mid_value)
        is_right_sorted = is_sorted(mid_value, nums[right_idx])
        is_target_in_left = is_in_range(nums[left_idx], mid_value, target)
        is_target_in_right = is_in_range(mid_value, nums[right_idx], target)

        # Left side is sorted and target is in the left side
        if is_left_sorted and is_target_in_left:
            right_idx = mid_idx - 1
        # Right side is sorted and target is in the right side
        elif is_right_sorted and is_target_in_right:
            left_idx = mid_idx + 1
        # Left side is sorted and target is in the right side
        elif is_left_sorted and not is_target_in_left:
            left_idx = mid_idx + 1
        # Right side is sorted and target is in the left side
        elif is_right_sorted and not is_target_in_right:
            right_idx = mid_idx - 1

    return -1

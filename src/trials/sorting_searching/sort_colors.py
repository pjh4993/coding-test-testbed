"""Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

from enum import Enum


class Color(Enum):
    RED = 0
    WHITE = 1
    BLUE = 2


def solution(nums: list[int]):
    """Sort the colors in-place.

    Args:
        nums: List[int]

    Returns:
        None

    """

    low_end = mid_end = 0
    right_start = len(nums) - 1

    while mid_end < right_start:
        if nums[mid_end] == Color.RED.value:
            # Swap with the low part and advance low pointer
            nums[low_end], nums[mid_end] = nums[mid_end], nums[low_end]
            low_end += 1
            mid_end += 1
        elif nums[mid_end] == Color.WHITE.value:
            # Advance mid pointer
            mid_end += 1
        elif nums[mid_end] == Color.BLUE.value:
            # Swap with the high part and advance high pointer
            nums[mid_end], nums[right_start] = nums[right_start], nums[mid_end]
            right_start -= 1

    return nums

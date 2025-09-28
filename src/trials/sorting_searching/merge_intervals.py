"""Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""


def solution(intervals: list[[tuple[int, int]]]):
    """Merge the intervals.

    Args:
        intervals: List[List[int]]

    Returns:
        List[List[int]]
    """

    intervals.sort(key=lambda x: x[0])  # Sort by start time

    merged = [intervals[0]]
    current = merged[0]

    for s, e in intervals[1:]:
        if s <= current[1]:
            current[1] = max(current[1], e)
        else:
            merged.append([s, e])
            current = merged[-1]

    return merged

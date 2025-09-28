"""Meeting Rooms II

Given an array of meeting time intervals `[[s1,e1],[s2,e2],...]`, find the minimum number of conference rooms required.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: 2
"""


def solution(intervals: list[list[int]]) -> int:
    """Find the minimum number of conference rooms required.

    Args:
        intervals: List[List[int]]

    Returns:
        int

    """

    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)

    earliest_start_idx, earliest_end_idx = 0, 0
    max_num_rooms, num_current_rooms = 0, 0

    while earliest_start_idx < len(starts):
        if starts[earliest_start_idx] < ends[earliest_end_idx]:
            num_current_rooms += 1
            max_num_rooms = max(max_num_rooms, num_current_rooms)
            earliest_start_idx += 1
        else:
            num_current_rooms -= 1
            earliest_end_idx += 1

    return max_num_rooms

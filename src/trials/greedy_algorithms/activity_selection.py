"""Activity Selection Problem.

Given an array of activities with start and end times, select the maximum number of non-overlapping activities that can be performed by a single person.

Example:
Input: [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
Output: 4   # Activities: (1,3), (4,6), (6,7), (8,9)

Hint:
Sort activities by their end time, then keep picking the next activity that starts after the previous one ends.

Grade:
Easy-Medium

"""


def solution(activities: list[tuple[int, int]]) -> int:
    """Select the maximum number of non-overlapping activities.

    Args:
        activities: List[Tuple[int, int]]

    Returns:
        int

    """

    activities.sort(key=lambda x: x[1])
    num_activities = 1
    current_end = activities[0][1]

    for start, end in activities:
        if start >= current_end:
            num_activities += 1
            current_end = end

    return num_activities

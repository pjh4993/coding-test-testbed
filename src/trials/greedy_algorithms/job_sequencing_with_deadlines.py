"""Job Sequencing with Deadlines.

Given a set of jobs with deadlines and profits, schedule jobs to maximize total profit.

Example:
Input: jobs = [(1, 2, 50), (2, 1, 100), (3, 2, 200), (4, 1, 300)]
Output: 3

"""


def _laziest_slot_available(slots: list[bool], deadline: int) -> int | None:
    """Check if the slot is available."""

    for i in range(deadline, 0, -1):
        if not slots[i]:
            return i

    return None


def _sort_by_deadline_and_profit(job: tuple[int, int, int]) -> tuple[int, int]:
    """Sort by deadline and profit."""

    _, deadline, profit = job

    return -profit, deadline


def solution(jobs: list[tuple[int, int, int]]) -> int:
    """Job Sequencing with Deadlines.

    Args:
        jobs: list[tuple[int, int, int]]

    Returns:
        int

    """

    if not jobs:
        return 0

    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(deadline for _, deadline, _ in jobs)
    slots = [False] * (max_deadline + 1)

    max_profit = 0

    for _, deadline, profit in jobs:
        slot_id = _laziest_slot_available(slots, deadline)
        if slot_id is None:
            continue

        max_profit += profit
        slots[slot_id] = True

    return max_profit

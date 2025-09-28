# -*- coding: utf-8 -*-
"""Course Schedule (Topological Sort).

You are given n courses and a list of prerequisite pairs. Return whether it is
possible to finish all courses.

Example:
Input: n = 4, prerequisites = [(1,0),(2,1),(3,2)]
Output: True
Explanation: Order can be 0→1→2→3.

Input: n = 2, prerequisites = [(0,1),(1,0)]
Output: False
Explanation: Cycle detected.

Hint:
Think of courses as nodes in a DAG. Use Kahn's Algorithm (BFS) or DFS cycle detection.

Grade:
Medium

"""

from typing import List, Tuple


def solution(n: int, prerequisites: List[Tuple[int, int]]) -> bool:
    """Determine if it's possible to finish all courses given prerequisites.

    Args:
        n: Number of courses (0 to n-1)
        prerequisites: List of (course, prerequisite) pairs

    Returns:
        True if all courses can be finished, False otherwise

    """
    # TODO: Implement course schedule using topological sort
    # Hint: Think of courses as nodes in a DAG. Use Kahn's Algorithm (BFS) or DFS cycle detection
    pass

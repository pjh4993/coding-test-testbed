# -*- coding: utf-8 -*-
"""Detect Cycle in an Undirected Graph.

Given an undirected graph with n nodes, determine if the graph contains a cycle.

Example:
Input: n = 4, edges = [(0,1),(1,2),(2,0),(2,3)]
Output: True
Explanation: 0→1→2→0 forms a cycle.

Hint:
Use DFS with parent tracking or Union-Find (Disjoint Set Union).

Grade:
Easy

"""

from typing import List, Tuple


def solution(n: int, edges: List[Tuple[int, int]]) -> bool:
    """Detect if an undirected graph contains a cycle.

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of (u, v) tuples representing undirected edges

    Returns:
        True if cycle exists, False otherwise

    """
    # TODO: Implement cycle detection
    # Hint: Use DFS with parent tracking or Union-Find (Disjoint Set Union)
    pass

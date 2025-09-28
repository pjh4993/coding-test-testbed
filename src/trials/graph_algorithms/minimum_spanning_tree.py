# -*- coding: utf-8 -*-
"""Minimum Spanning Tree (Kruskal's Algorithm).

You are given a connected undirected graph with weighted edges. Find the weight
of the minimum spanning tree.

Example:
Input: n = 4, edges = [(0,1,1),(1,2,2),(0,2,2),(2,3,1),(1,3,3)]
Output: 4
Explanation: MST = edges (0,1),(2,3),(1,2) with weight 1+1+2=4.

Hint:
Sort edges by weight and use Union-Find to avoid cycles.

Grade:
Medium-Hard

"""

from typing import List, Tuple


def solution(n: int, edges: List[Tuple[int, int, int]]) -> int:
    """Find the weight of the minimum spanning tree using Kruskal's algorithm.

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of (u, v, weight) tuples

    Returns:
        Weight of the minimum spanning tree

    """
    # TODO: Implement Kruskal's algorithm for MST
    # Hint: Sort edges by weight and use Union-Find to avoid cycles
    pass

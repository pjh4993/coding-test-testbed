# -*- coding: utf-8 -*-
"""Shortest Path in a Weighted Graph (Dijkstra's Algorithm).

You are given a directed weighted graph with n nodes. Find the shortest distance
from a given source node s to every other node.

Example:
Input: n = 5, edges = [(0,1,2),(0,2,4),(1,2,1),(1,3,7),(2,4,3)], s = 0
Output: [0,2,3,9,6]
Explanation: Shortest paths are
0→1 (2), 0→1→2 (3), 0→1→3 (9), 0→1→2→4 (6)

Hint:
Use a priority queue (min-heap) to always expand the nearest unvisited node.

Grade:
Medium

"""

from collections import defaultdict
from typing import Dict, List, Tuple


def build_graph(
    n: int, edges: List[Tuple[int, int, int]], directed=False, weighted=False
) -> Dict[int, List[Tuple[int, int]]]:
    """Build adjacency list from edges."""

    graph = defaultdict(list)

    for u, v, *w in edges:
        if weighted:
            weight = w[0]
            graph[u].append((v, weight))
            if not directed:
                graph[v].append((u, weight))
        else:
            graph[u].append(v)
            if not directed:
                graph[v].append(u)

    return graph


def solution(n: int, edges: List[Tuple[int, int, int]], s: int) -> List[int]:
    """Find shortest distances from source node s to all other nodes using Dijkstra's algorithm.

    Args:
        n: Number of nodes (0 to n-1)
        edges: List of (from, to, weight) tuples
        s: Source node

    Returns:
        List of shortest distances from s to each node

    """
    # TODO: Implement Dijkstra's algorithm
    # Hint: Use a priority queue (min-heap) to always expand the nearest unvisited node
    pass

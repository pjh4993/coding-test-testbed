"""Huffman Coding.

Given characters with frequencies, build a binary tree to encode characters such that the total encoding cost is minimized.

Example:
Input: {a:5, b:9, c:12, d:13, e:16, f:45}
Output: Huffman tree with average code length minimized (codes may vary)

Hint:
Use a min-heap: repeatedly combine the two lowest-frequency nodes until one tree remains.

Grade:
Hard

"""

import heapq


def solution(frequencies: dict[str, int]) -> int:
    """Huffman Coding.

    Args:
        freqencies: dict[str, int]

    Returns:
        int

    """

    heap = [freq for freq in frequencies.values() if freq is not None and freq > 0]

    if not heap:
        return 0

    if len(heap) == 1:
        return 0

    heapq.heapify(heap)
    total_cost = 0

    for _ in range(len(heap) - 1):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        total_cost += s
        heapq.heappush(heap, s)

    return total_cost

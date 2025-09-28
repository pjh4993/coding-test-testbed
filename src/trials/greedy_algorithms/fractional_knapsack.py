"""Fractional Knapsack.

Given weights and values of `n` items, and a maximum capacity `W`, choose items to maximize total value. You can break items (fractions allowed).

Example:
Input: W = 50, values = [60,100,120], weights = [10,20,30]
Output: 240.0

"""


def _cost_per_weight(weight: int, value: int) -> float:
    return value / weight


def solution(weights: list[int], values: list[int], capacity: int) -> float:
    """Fractional Knapsack.

    Args:
        weights: list[int]
        values: list[int]
        capacity: int

    Returns:
        float

    """

    cost_per_weight = [
        (_cost_per_weight(w, v), v, w) for w, v in zip(weights, values, strict=True) if w > 0
    ]
    cost_per_weight.sort(reverse=True, key=lambda x: x[0])

    total = 0.0

    for ratio, _, w in cost_per_weight:
        if capacity == 0:
            break

        take = min(w, capacity)
        total += ratio * take
        capacity -= take

    return total

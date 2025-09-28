# -*- coding: utf-8 -*-
"""Coin Change.

You are given coins of different denominations and a target amount. Find the minimum number of coins needed to make the target. If it’s not possible, return `-1`.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3 (11 = 5 + 5 + 1)

"""


def _trivial_solution(coins: list[int], amount: int) -> int:
    """Trivial solution.

    Args:
        coins: list[int]
        amount: int

    """

    if amount == 0:
        return 0

    if amount in coins:
        return 1

    if amount < min(coins):
        return -1

    return None


def solution(coins: list[int], amount: int) -> int:
    """Coin Change.

    Args:
        coins: list[int]
        amount: int

    Returns:
        int: minimum number of coins needed to make the target

    """

    trivial_solution = _trivial_solution(coins, amount)

    if trivial_solution is not None:
        return trivial_solution

    state_size = max(amount + 1, max(coins) + 1)

    states = [-1] * state_size
    states[0] = 0

    for coin in coins:
        states[coin] = 1

    for i in range(1, state_size):
        if i in coins:
            continue
        states[i] = min(
            (states[i - coin] + 1 for coin in coins if (i - coin) >= 0 and states[i - coin] != -1),
            default=-1,
        )

    return states[amount]

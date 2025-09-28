# -*- coding: utf-8 -*-
"""Climbing Stairs.

You are climbing a staircase. It takes *n* steps to reach the top. Each time you can climb either **1** or **2** steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: (1+1+1), (1+2), (2+1)

Hint:
This is essentially the Fibonacci sequence. Define `dp[i] = number of ways to reach step i`.

Grade:
Easy

"""


def solution(n: int) -> int:
    """Climbing Stairs.

    Args:
        n: int

    Returns:
        int: number of ways to climb to the top

    """

    state_size = max(n + 1, 3)

    states = [0] * state_size
    states[0] = 1
    states[1] = 1
    states[2] = 2

    for i in range(3, n + 1):
        states[i] = states[i - 1] + states[i - 2]

    return states[n]

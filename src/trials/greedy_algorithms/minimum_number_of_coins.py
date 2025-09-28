"""Minimum Number of Coins.

You are given denominations `[1, 2, 5, 10, 20, 50, 100, 500, 1000]`. For a given amount, find the minimum number of coins/notes required.

Example:
Input: amount = 93
Output: 5   # 50 + 20 + 20 + 2 + 1

Hint:
Always pick the largest possible denomination first (greedy choice).

Grade:
Easy

"""


def solution(denominations: list[int], amount: int) -> int:
    """Minimum Number of Coins.

    Args:
        amount: int
        denominations: list[int]

    Returns:
        int

    """

    if amount == 0:
        return 0

    denominations.sort(reverse=True)
    count = 0

    for denomination in denominations:
        if denomination <= amount:
            k = amount // denomination
            count += k
            amount -= k * denomination
        if amount == 0:
            break

    return count

#!/usr/bin/python3
""" Documentation """
from collections import deque


def makeChange(coins, total):
    """
    Calculates the minimum number of coins
    needed to make change for a given total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount for which change needs to be made.

    Returns:
        int: The minimum number of coins needed
        to make change for the given total.
             Returns -1 if it is not possible
             to make change for the given total.
    """

    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set()

    while queue:
        current_total, num_coins = queue.popleft()

        for coin in coins:
            new_total = current_total + coin

            if new_total == total:
                return num_coins + 1
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                queue.append((new_total, num_coins + 1))

    return -1

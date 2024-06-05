#!/usr/bin/python3
"""
This module provides a function to make change for a given amount of money.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.

    Args:
        coins: A list of integers representing the coin values.
        total: An integer representing the total amount of money to make.

    Returns:
        An integer representing the fewest number of coins needed to make the
        total. If the total cannot be made, return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total %= coin

    if total != 0:
        return -1

    return num_coins

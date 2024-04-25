#!/usr/bin/python3
"""
This module provides a function that calculates the minimum number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    This function calculates the minimum number of operations needed to
    result in exactly n H characters in the file.

    Arguments:
        n -- the number of H characters to result in

    Returns:
        The minimum number of operations needed to result in exactly n H
        characters in the file.
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n / divisor
            operations += divisor
        else:
            divisor += 1

    return operations

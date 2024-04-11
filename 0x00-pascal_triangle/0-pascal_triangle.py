#!/usr/bin/python3
"""
This module provides a function that defines
the Pascal's Triangle given a size.
"""


def pascal_triangle(n):
    """
    Creates a list representing a Pascal's Triangle.

    Args:
        n (int): The size of the triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

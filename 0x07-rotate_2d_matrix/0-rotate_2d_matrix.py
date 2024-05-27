#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix by 90 degrees.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in place by 90 degrees.

    Args:
        matrix (list): A 2D matrix.

    Returns:
        Nothing.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

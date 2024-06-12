#!/usr/bin/python3
"""
This module provides a function that calculates the perimeter of an island
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island

    Arguments:
        grid -- a list of list of integers

    Returns:
        The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    # Define directions to check neighboring cells
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:  # Land cell found
                for direction in directions:
                    # Check all neighboring cells
                    neighbor_row = row + direction[0]
                    neighbor_column = column + direction[1]
                    if (
                        neighbor_row < 0
                        or neighbor_row == rows
                        or neighbor_column < 0
                        or neighbor_column == columns
                        or grid[neighbor_row][neighbor_column] == 0
                    ):
                        # Neighbor is out of bounds or is water
                        perimeter += 1

    return perimeter

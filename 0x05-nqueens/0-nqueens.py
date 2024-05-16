#!/usr/bin/python3
"""
This module provides a solution to the N queens problem.
"""
import sys


def main():
    """
    Implementation of the backtracking algorithm to solve the N queens problem.

    Usage:
        ./0-nqueens.py N

    Args:
        N: an integer greater or equal to 4.

    Returns:
        None.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """
        Check if a queen can be placed on board[row][col].

        Args:
            board: a list of lists containing the state of the board.
            row: the row to check.
            col: the column to check.

        Returns:
            True if the queen can be placed, False otherwise.
        """
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        """
        Solve the N queens problem using backtracking.

        Args:
            board: a list of lists containing the state of the board.
            col: the current column to check.

        Returns:
            True if the problem is solved, False otherwise.
        """
        if col == N:
            print([[i, row.index(1)] for i, row in enumerate(board)])
            return True
        res = False
        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                res = solve(board, col + 1) or res
                board[i][col] = 0
        return res

    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve(board, 0):
        print("Solution does not exist")


if __name__ == "__main__":
    main()

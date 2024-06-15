#!/usr/bin/python3
"""
This module provides a script that solves a complex game.
"""


def isWinner(x, nums):
    """
    Determines the winner of a game between Maria and Ben.

    Arguments:
        x: An integer representing the number of rounds.
        nums: A list of integers representing the numbers in each round.

    Returns:
        A string representing the winner of the game.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Step 1: Use Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def can_win(n):
        """
        Determines if Maria can win the game with the given number.

        Arguments:
            n: An integer representing the number to play with.

        Returns:
            A boolean indicating if Maria can win the game.
        """
        if n < 2:
            return False  # No primes to pick

        moves = [False] * (n + 1)

        for i in range(2, n + 1):
            if sieve[i]:
                for j in range(i, n + 1, i):
                    moves[j] = True  # Mark multiples of i

        primes_in_range = [p for p in primes if p <= n]
        if not primes_in_range:
            return False  # No primes in the range

        # Use dynamic programming to determine winning positions
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            if sieve[i]:
                for j in range(i, n + 1, i):
                    if not dp[j]:
                        dp[j] = True
                        break

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

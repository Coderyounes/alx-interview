#!/usr/bin/python3
""" DOcumantation """


def minOperations(n):
    """
    Calculates the minimum number of
    operations required to reach a given number.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations

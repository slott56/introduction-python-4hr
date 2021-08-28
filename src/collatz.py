"""
Collatz Conjecture stuff.
"""
from typing import Iterator

def hotpo(n: int) -> int:
    """
    Half-or-Three-Plus-One function

    :param n: input value
    :return: output, either n/2 or 3n+1

    >>> hotpo(10)
    5
    >>> hotpo(5)
    16

    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def iterate_from(n: int) -> Iterator[int]:
    yield n
    while n != 1:
        n = hotpo(n)
        yield n

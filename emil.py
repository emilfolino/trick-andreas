"""
Does stuff with some numbers
"""

import math
import sys
import time


def a(n):
    """
    Returns things based on the percentage used.
    """
    return n % 2 == 0

def q(n):
    """
    Returns some other stuff based on a crocodiles mouth.
    """
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def query(z, e, l, d, a, h):
    """
    Well don't even get started with this one.
    """
    start = time.time()
    return z

b = [x**2 for x in range(2, 100) if a(x)]

c = [z + 1 for z in range(len(b)) if a(z)]

print(c)

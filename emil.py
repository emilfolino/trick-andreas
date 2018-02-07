"""
Does stuff with some random numbers
"""

import math

def a(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

b = [x for x in range(2, 100) if a(x)]

c = [b[z]**2 + b[z+1]**2 for z in range(len(b) - 1)]

print(c)

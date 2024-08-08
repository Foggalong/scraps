#!/usr/bin/env python3

"""
A random walk in n-dimensions eventually returns to the origin
with probability 100% for n = 1, 2. For n > 2 it's proven that
the probability is less than 100%.
"""

from random import randint

dim = 3
loc = [0] * dim

while True:
    loc[randint(0, dim-1)] += [-1, 1][randint(0, 1)]
    print(loc)
    if loc == [0] * dim:
        break

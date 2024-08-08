#!/usr/bin/env python3

# print the automorphic numbers
# https://oeis.org/A003226

a = 1

while True:
    if str(a**2).endswith(str(a)):
        print(a)
    a += 1

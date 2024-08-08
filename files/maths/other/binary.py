#!/usr/bin/env python3

# returns the given string as a list of 5-bit binary numbers

while True:
    string, ints = input("> ").upper(), []
    for char in string:
        if char == " ":
            ints.append(format(27, '05b'))
        else:
            ints.append(format(ord(char)-65, '05b'))

    ints.append('11100')
    print(ints)


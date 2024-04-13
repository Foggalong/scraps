#!/usr/bin/env python3

"""
This file contains various functions for applying markdown formatting
to strings and then viewing that formatting in a terminal. This is done
using ANSI SRG parameters.
"""

from textwrap import fill
from os import get_terminal_size


# ANSI codes equivalent to various markdown commands
bf_y = "\x1B[1m"    # bold on (**)
bf_n = "\x1B[22m"   # bold off (**)
it_y = "\x1B[3m"    # italics on (_)
it_n = "\x1B[23m"   # italics off (_)
so_y = "\x1B[9m"    # strike out on (~)
so_n = "\x1B[29m"   # strike out off (~)


def mdswitch(active, on, off, string):
    """
    Private function for formatter: a given formatting features variables
    as input and then peforms the needed switch.
    """
    if active:
        string += off
    else:
        string += on
    active = not active
    return active, string


def escaped(string, i):
    """
    takes a string and integer i as input and returns a bool indicating
    whether the character at i was escaped by preceding backslashes or not.
    """
    i = i-1
    bs_count = 0
    while i >= 0:
        if string[i] != "\\":
            break
        bs_count += 1
        i -= 1
    # even number of backslashes means not escaped
    return bool(bs_count%2)


def formatter(string):
    """
    Takes a string as input and returns a version of that string with any
    included markdown formatting applied, using ANSI SRG parameters.
    """

    # skip empty or 1 character strings
    if (len(string) < 2):
        return string

    # formatting booleans
    italic = bold = uline = strike = False
    # string which will be returned
    newstring = ""
    # current character
    i = 0

    # case of first character needs treating individually
    if (string[0:2] == "* "):
        newstring += "• "  # add unicode bullet points
        i += 1
    elif (string[0:2] == "**"):
        newstring += bf_y  # bold
        bold = True
        i += 1
    elif (string[0] in ["_", "*"]):
        newstring += it_y  # italics
        italic = True
    elif (string[0] == "~"):
        newstring += so_y  # stike out
        strike = True
    elif (string[0] == "\\"):
        if (string[1] in ["*", "_", "~"]):
            pass
        else:
            newstring += "\\"
    else:
        newstring += string[0]

    # iterate over remaining characters
    i += 1
    while i < len(string):
        # handle backslash
        if (string[i] == "\\"):
            if escaped(string, i):
                newstring += "\\"
            elif (i+1 < len(string) and string[i+1] in ["*", "_", "~"]):
                pass
            else:
                newstring += "\\"
        # handle underscore (italics)
        elif (string[i] == "_"):
            if escaped(string, i):
                newstring += "_"
            else:
                italic, newstring = mdswitch(italic, it_y, it_n, newstring)
        # handle asterisk (could be bold or italics)
        elif (string[i] == "*"):
            if escaped(string, i):
                newstring += "*"
            elif (i+1 < len(string) and string[i+1] == "*"):
                bold, newstring = mdswitch(bold, bf_y, bf_n, newstring)
                # non-standard check which re-enables itallics
                if italic:
                    newstring += it_y
                i += 1
            else:
                italic, newstring = mdswitch(italic, it_y, it_n, newstring)
        # handle tilde (strike out)
        elif (string[i] == "~"):
            if escaped(string, i):
                newstring += "~"
            else:
                strike, newstring = mdswitch(strike, so_y, so_n, newstring)
        # otherwise it's just a normal character
        else:
            newstring += string[i]
        i += 1

    return newstring


def echo(string):
    """
    Takes a string as input and prints out a version of that string
    with any markdown formatting applied. It will also wrap according
    to the width of the terminal
    """
    cols = get_terminal_size().columns
    print(fill(formatter(string), width=cols))


def mdfile(filename):
    """
    Takes a filename as string input and then prints out a version of
    that file using echo as above.
    """
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]
    for line in lines:
        echo(line)


def demo():
    with open("test.md", "r") as file:
        lines = [line.strip() for line in file]

    print("PLAIN")
    for line in lines:
        print(line)

    print("\nMARKDOWN")
    mdfile("test.md")


demo()

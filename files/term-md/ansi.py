#!/usr/bin/env python3

"""
Various functions for formatting strings in Python using ANSI escape
code SRG (Select Graphics Rendition) parameters.
"""


# SRG codes used in this file, sorted by type in code:off-code format.
SRGs = {
    # Text Formatting
    1: 22,  # bold (22 also resets colour)
    2: 22,  # faint (22 als resets colour)
    3: 23,  # italic
    4: 24,  # underline
    5: 25,  # blink
    9: 29,  # crossed out  ## BUG not suppoted by urxvt
    21: 24,  # double underline
    53: 55,  # overlined
    # Font colouring
    30: 39,  # black font
    31: 39,  # red font
    32: 39,  # green font
    33: 39,  # orange font
    34: 39,  # blue font
    35: 39,  # pink font
    36: 39,  # cyan font
    37: 39,  # white font
    # Background colouring
    40: 49,  # black background
    41: 49,  # red background
    42: 49,  # green background
    43: 49,  # orange background
    44: 49,  # blue background
    45: 49,  # pink background
    46: 49,  # cyan background
    47: 49,  # white background
    # Other
    0: 0,  # resets all formatting effects
    7: 22,  # invert colours (22 also resets font weight)
}


def SRG(string, codes):
    """
    Takes a string and list of SRG codes (integers) as input and returns
    that string with those SRG formatting parameters applied.
    """

    # each on-code will have a correspponding off-code
    oncodes, offcodes = [], []
    for code in codes:
        oncodes.append(str(code))
        offcodes.append(str(SRGs[code]))

    # SRG codes can be stacked if semi-colon separated
    onstr = ";".join(oncodes)
    offstr = ";".join(offcodes)

    # print the formatted string using ANSI escape codes
    return("\x1B[{}m{}\x1B[{}m".format(onstr, string, offstr))


def demo():
    print(SRG("Hello, world!", [35, 5, 1]))

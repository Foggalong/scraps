#! /usr/bin/python3

"""
Simple anagram game. Fetches articles from Wikipedia and uses the article
name for the anagram and the first line of that article for a clue.
"""

from subprocess import call
from random import shuffle


def clean(test_str):
    """
    Takes a string from the HTML source of a website, cleans out any
    text which appears between tags (< and >), and then returns the
    output as a string.
    """

    ret = ""
    skip1c = 0
    for i in test_str:
        if i == "<":
            skip1c += 1
        elif i == ">" and skip1c > 0:
            skip1c -= 1
        elif skip1c == 0:
            ret += i
    return ret


def shuffle_word(word):
    """
    Shuffle the character order of a given word.
    """
    word = list(word)
    shuffle(word)
    return "".join(word)


while True:
    randomLink = "https://en.wikipedia.org/wiki/Special:Random"
    call(["wget", "-q", "-O", "article", randomLink])

    with open("article", "r") as file:
        lines = [line.strip() for line in file]

    first_line = ""
    for x in range(0, len(lines)):
        if lines[x] == "</table>":
            if lines[x+1].startswith("<p>"):
                first_line = lines[x+1]

    try:
        if first_line == "":
            raise Exception
        answer = clean(first_line.split("<b>")[1].split("</b>")[0]).strip()
    except Exception:
        call(["rm", "article"])
        continue

    first_line_clean = clean(first_line)

    options = []
    splits = [
        " is a ",
        " is an ",
        " is the ",
        " was a ",
        " was an ",
        " was the ",
        " were a ",
        " were an ",
        " were the ",
    ]

    for string in splits:
        try:
            options.append(len(first_line_clean.split(string)[0]))
        except:
            pass

    choice = splits[options.index(min(options))]

    if (choice in first_line) and answer:
        question = clean(first_line.split(choice)[1].split(".")[0]).strip()
        print("\n'" + question + "'\n\nClue: '" + shuffle_word(answer) + "'\n")
    else:
        call(["rm", "article"])
        continue

    user_ans = input("> ").strip().lower()

    if user_ans == answer.lower():
        print("Correct!\n")
    else:
        print("Wrong! The correct answer was '" + answer + "'\n\n----\n")

    call(["rm", "article"])

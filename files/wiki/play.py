#! /usr/bin/python3

from subprocess import call
from random import shuffle

call(["wget", "-q", "-O", "article",
    "https://en.wikipedia.org/wiki/Special:Random"])

with open("article", "r") as file:
    lines = [line.strip() for line in file]

first_line = ""
for x in range(0, len(lines)):
    if lines[x] == "</table>":
        if lines[x+1].startswith("<p>"):
            first_line = lines[x+1]

if first_line == "":
    call(["rm", "article"])
    exit()

def clean(test_str):
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

try:
	answer = clean(first_line.split("<b>")[1].split("</b>")[0]).strip()
except:
	call(["rm", "article"])
	exit()

first_line_clean = clean(first_line)

options = []
splits = [
	" is a ",
	" is an ",
	" is the ",
	" was a ",
	" was an",
	" was the "
]

for string in splits:
	try:
		options.append(len(first_line_clean.split(string)[0]))
	except:
		pass

choice = splits[options.index(min(options))]

if choice in first_line:
	question = clean(first_line.split(choice)[1].split(".")[0]).strip()

def shuffle_word(word):
   word = list(word)
   shuffle(word)
   return "".join(word)

if answer and question:
	print("'" + question + "'\n\nClue: '" + shuffle_word(answer) + "'\n")

user_ans = input("> ").strip().lower()

if user_ans == answer.lower():
	print("Correct!")
else:
	print("Wrong! The correct answer was '" + answer + "'")

call(["rm", "article"])

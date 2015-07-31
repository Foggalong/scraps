#!/usr/bin/python3

# This script does some testing on multiplayer Rock, Paper Scissors games to
# see at how many players it becomes unsustainable to do.

from itertools import permutations

players = 7
shapes = ["r", "p", "s"]


# Creates list of outcomes for given variables

options = list(set([e for e in permutations(shapes*players, players)]))
options = [list(e) for e in options]

def all_same(items):
    return all(x == items[0] for x in items)

def outcome(result):
    res = {"r": 0, "p": 0, "s": 0}
    for shape in result:
        res[shape] += 1 
    if (res["r"] * res["p"] * res["s"]) != 0:
        return "draw"
    elif all_same(list(result)) is True:
        return "draw"
    else:
        return "win"

wins = 0
draw = 0 
for x in options:
    if outcome(x) == "draw":
        draw += 1
    else:
        wins += 1

print("WINS:", round(wins/len(options), 2))
print("DRAW:", round(draw/len(options), 2))

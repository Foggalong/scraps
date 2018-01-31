#!/usr/bin/python3

"""
This script was used as proof that a lecturer had accidentally unannonymised
the data from tests by releasing a list of students and their ID numbers.
"""

# Extract data from names.txt
name_ids, names = [], []
with open('names.txt', 'r') as file:
    for line in file:
        if "-" in list(line):
            name_ids.append(line.split(" - ")[0])
            names.append(line.split(" - ")[1])
        else:
            pass

# Extract data from scores.txt
score_ids, scores = [], []
with open('scores.txt', 'r') as file:
    for line in file:
        if "-" in list(line):
            score_ids.append(line.split(" - ")[0])
            scores.append(line.split(" - ")[1])
        else:
            pass

# Generates data for people in both
with open('data.csv', 'w+') as file:
    both_ids = list(set(name_ids) & set(score_ids))
    for sid in both_ids:
        forename = names[name_ids.index(sid)].strip().split(",")[1]
        surname = names[name_ids.index(sid)].strip().split(",")[0]
        score = scores[score_ids.index(sid)].strip()
        file.write(forename + "," + surname + "," + sid + "," + score + "\n")

#!/usr/bin/env python3

ranks = [
    [(1, 3), (2, 3), (3, 2), (4, 3)],
    [(1, 4), (4, 1), (3, 3), (2, 2)],
    [(2, 2), (1, 4), (3, 4), (4, 1)],
    [(4, 1), (2, 2), (3, 1), (1, 4)]
]


# DATA PREPARATION

# Extract boy (row) data
boyRanks = []
for row in ranks:
    boy = [r[0] for r in row]
    prefs = sorted(zip(boy, range(len(ranks[0]))))
    boyRanks.append([girl for rank, girl in prefs])

# Get transform of ranks matrix
cols = [[] for _ in ranks[0]]
for row in ranks:
    for i in range(len(row)):
        cols[i].append(row[i])

# Extract girl (col) data
girlRanks = []
for col in cols:
    girl = [c[1] for c in col]
    prefs = sorted(zip(girl, range(len(cols[0]))))
    girlRanks.append([boy for rank, boy in prefs])


# CALCULATING MATCHING

# Initialise offstring and string lists
offstring = list(range(len(boyRanks)))
choices = ["" for girl in girlRanks]

while offstring:
    for girl in girlRanks:
        ind = girlRanks.index(girl)

        # Each boy proposes to first girl in list
        proposals = []
        for boy in offstring:
            if boyRanks[boy][0] == ind:
                proposals.append(boy)

        # If girl has someone on string, add them too
        if choices[ind] != "":
            proposals.append(choices[ind])

        # If girl has no proposal, skip
        if not proposals:
            continue

        # Proposer with highest rank wins
        propRanks = [girl.index(boy) for boy in proposals]
        winner = sorted(zip(propRanks, proposals))[0][1]

        # If winner wasn't on string, update string & offstring
        if winner in offstring:
            # Add previous string to offstring
            if choices[ind] != "":
                offstring.append(choices[ind])
            offstring.remove(winner)
            choices[ind] = winner

        # Remove winner from proposals
        proposals.remove(winner)
        for boy in proposals:
            boyRanks[boy].remove(ind)

        if not offstring:
            break


# FINAL OUTPUT
print(list(zip(list(range(len(girlRanks))), choices)))

#!/usr/bin/python3

# This is a solution to the Liar's Problem, for numbers between 0
# and 15 with 7 questions. The answers must be given as Y for yes
# and N for no and can contain exactly one lie.


def flip(var):
    if var == "Y":
        return "N"
    elif var == "N":
        return "Y"

ans = []
for x in range(1, 5):
    ans.append(input("Q%s: is your number on the left branch from here? " % x))
ans.append(input("Q5: did you tell the truth for Q1, Q2, and Q4? "))
ans.append(input("Q6: did you tell the truth for Q1, Q3, and Q4? "))
ans.append(input("Q7: did you tell the truth for Q2, Q3, and Q4? "))

if ans[4:7].count("N") in (2, 3):
    # Lie in first 4 questions
    combs = [
        ["N", "N", "Y"],  # Q1 was a lie
        ["N", "Y", "N"],  # Q2 was a lie
        ["Y", "N", "N"],  # Q3 was a lie
        ["N", "N", "N"],  # Q4 was a lie
    ]
    ans[combs.index(ans[4:7])] = flip(ans[combs.index(ans[4:7])])
elif ans[4:7].count("N") == 1:
    # Lie in the last 3 questions
    ans[4:7] = ["Y" if x == "N" else x for x in ans[4:7]]
else:
    # No lie
    pass

# Sequence of first 4 Y & N is a binary representation of chosen number
binary = ["0" if x == "Y" else "1" for x in ans[0:4]]
print("Your number was", (int("".join(binary), 2)))

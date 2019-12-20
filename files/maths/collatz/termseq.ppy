#!/usr/bin/env python3


def collatz(n):
    """
    Returns the next integer after input n following
    the rules of the Collatz conjecture.
    """
    if (n % 2):
        return(3*n + 1)
    else:
        return(int(n/2))


with open("hailstones.csv", "r") as file:
    # skip through to the last line
    for line in file:
        pass
    # continue from the next integer
    start = int(line.strip().split(",")[0]) + 1


# compute 10 hailstone sequences
print("Computing hailstone sequences")
sequences = []
for i in range(start, start+10000):
    print("Running for {}".format(i), end="\r")
    sequence = [i]
    # hailstone sequence ends when it reaches 1
    while sequence[-1] != 1:
        sequence.append(collatz(sequence[-1]))
    sequences.append(sequence)


with open("hailstones.csv", "a") as file:
    for sequence in sequences:
        # CSV string of the hailstone sequence
        string = ",".join([str(s) for s in sequence])
        # update the data file to include that sequence
        file.write(string + "\n")

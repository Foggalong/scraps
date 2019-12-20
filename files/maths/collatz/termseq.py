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


# compute 10 hailstone sequences
print("Computing hailstone sequences")
caught = []
sequences = []
for i in range(1, 10000):
    print("Running for {}".format(i), end="\r")
    sequence, x = [], i
    # hailstone sequence ends when it reaches 1
    while x not in caught:
        x = collatz(sequence[-1])
        sequence.append(x)
        if x in caught:
            break
    sequences.append(sequence)


with open("hailstones.csv", "a") as file:
    for sequence in sequences:
        # CSV string of the hailstone sequence
        string = ",".join([str(s) for s in sequence])
        # update the data file to include that sequence
        file.write(string + "\n")

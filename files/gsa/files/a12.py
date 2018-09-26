n = 8
x = (2, 5, 6, 9, 10, 12, 14, 15)
r = (1, 1, 3, 1, 3, 2, 1, 1)


def radius(i, j, x, r):
    """
    Takes two integer inputs and returns True if the explosion indexed
    i is in the blast radius of the explosion indexed j.
    """

    return x[j]-r[j] <= x[i] <= x[j]+r[j]


def finder(n, x, r):
    """
    Takes a number of explosives, their positions, and blast radii as
    input and then as output returns a list of sets of explosives which
    are chained to the explosive indexed by that sets index.
    """

    # Set i contains all the explosives in the radiues of i
    links = [{i for i in range(n) if radius(i, j, x, r)} for j in range(n)]

    while True:
        chains = [set(l) for l in links]

        # Iterate over the elements in each chain and add all the
        # explosives which are linked to that element to the chain
        for c in chains:
            for i in set(c):
                c.update(links[i])

        # If your list of chains hasn't changed, we're done
        if chains == links:
            return chains
        links = chains[:]


def solution(n, x, r):
    """
    Takes a number of explosives, their positions, and blast radii as
    input and then calculates the minimum number of detonations needed
    to cause them all to explode. It returns that multiplied by 10,000
    """

    chains = finder(n, x, r)
    tocheck = {i: chains[i] for i in range(n)}
    prev = dict(tocheck)
    boomers = []

    while tocheck:
        prev = dict(tocheck)
        checking = max(tocheck, key=tocheck.get)
        boomers.append(chains[checking])
        for i in chains[checking]:
            for j in prev:
                if i in prev[j]:
                    tocheck.pop(j, None)

    return len(boomers) * 10000


print(solution(n, x, r))

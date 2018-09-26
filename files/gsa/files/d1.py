# This takes too long to execute, needs optimising


def swap(l, t):
    temp = list(l)
    a = temp[t[0]]
    temp[t[0]] = temp[t[1]]
    temp[t[1]] = a
    return temp


def configs(n, c):
    boxes = [i for i in range(n)]
    combs = [boxes]
    #swaps = [(c[2*i], c[2*i+1]) for i in range(len(c)//2)]

    tocheck = [boxes]
    while tocheck:
        for l in tocheck:
            for s in c:
                t = swap(l, s)
                if t not in combs:
                    combs.append(t)
                    tocheck.append(t)
            tocheck.remove(l)

    return combs


def solution(n, c):
    return len(configs(n, c)) % (10**9 + 7)

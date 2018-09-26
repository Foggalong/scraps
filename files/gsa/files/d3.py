def palscore(s):
    """
    Takes a string as input and returns the length of the longest
    possible palindrome which uses characters from that string.
    """

    chars = "abcdefg"
    points = 0
    odd = False

    for c in chars:
        n = s.count(c)
        if n % 2:
            odd = True
        if n > 1:
            points += (n // 2) * 2
    if odd:
        points += 1

    return points


def solution(s):
    bins = [[], [], [], []]
    chars = "abcdefg"
    counts = {c: s.count(c) for c in chars}

    while counts:
        m = max(counts, key=counts.get)
        for i in range(counts[m]):
            bins[i % 4].append(m)
        counts.pop(m, None)

    return bins

print(solution("abcbg"))

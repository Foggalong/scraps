def super(s):
    """
    Takes a string as input and returns True if that string is
    super colourful and False otherwise.
    """

    # Must contain every colour
    if any(c not in s for c in "YRB"):
        return False

    # Two colours can't be equally frequent
    counts = [s.count(c) for c in "YRB"]
    if len(set(counts)) != len(counts):
        return False

    return True


def subset(A, N):
    """
    Takes a string A and an integer N as input and returns all the
    possible substrings of A of length N which are super colourful
    """

    subs, p = [], 0

    while p + N != len(A) + 1:
        if super(A[p:p+N]):
            subs.append(A[p:p+N])
        p += 1

    return subs


def solution(s):
    """
    Takes a given string as input and returns the number of
    super colourful substrings plus 10,000.
    """

    count = 0

    # Super colourful strings will have length > 5
    for n in range(6, len(s)+1):
        count += len(subset(s, n))

    return count + 10000


print(solution("RBRRYBRYYRBBRYR"))

def almost(a):
    """
    Takes an integer as input and returns True if it is almost
    square (that is, it's possible to turn it into a square by
    removing a single digit) or False otherwise.
    """

    digits, almosts = str(a), []

    for i in range(len(digits)):
        n = int(digits[:i] + digits[i+1:])
        if n**.5 == int(n**.5):
            almosts.append(n)

    if almosts:
        return True
    return False


def solution(a):
    """
    Takes an integer as input and then returns the number of
    almost square numbers between 10 and that input.
    """

    i = 0
    for s in range(10, a+1):
        if almost(s):
            i += 1
    return i


print(solution(1234))

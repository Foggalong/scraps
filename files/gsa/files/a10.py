def validMoves(n, r, s):
    """
    Takes size of pile and players 'to avoid' divisors and returns
    a list of valid moves a player could make.
    """

    return [m for m in range(1, 4) if (n-m) % r and (n-m) % s]


def play(n, a, b, x, y):
    """
    Takes size of pile and two players 'to avoid' divisors as input
    and returns True if when both play optimally player one wins or
    False if player two wins.
    """

    p = 1  # Alice=1, Bob=2

    while True:
        # Take whole pile if possible
        if n < 4:
            if p == 1:
                return True
            return False

        # Find a list of valid moves
        if p == 1:
            valid = validMoves(n, a, b)
        elif p == 2:
            valid = validMoves(n, x, y)

        # If no valid move player loses
        if not valid:
            if p == 1:
                return False
            return True

        # Otherwise try and leave opponent with no moves
        for m in valid:
            if p == 1 and not validMoves(n-m, x, y):
                return True
            elif p == 2 and not validMoves(n-m, a, b):
                return False

        # Otherwise take least possible and switch player
        n -= valid[0]
        p = 3 - p


def solution(t_n, t_a, t_b, t_x, t_y):
    """
    Takes 5 5-tuples of integers as inputs and returns 123 plus
    how many games player one would win playing optimally when
    using those tuples as the initial game states.
    """

    wins = 0
    for i in range(5):
        if play(t_n[i], t_a[i], t_b[i], t_x[i], t_y[i]):
            wins += 1

    return wins + 123


# Play
n = 7

a, b = 5, 6  # Alice's numbers
x, y = 4, 3  # Bob's numbers

print(play(n, a, b, x, y))

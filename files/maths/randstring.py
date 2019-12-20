from random import choice


def random_string(chars, length):
    """
    Takes two integers as input (number of letters to use in string
    and length of string to generate) and returns a random string.
    """
    alphabet = [chr(i) for i in range(65,65+chars)]
    s = ""
    for i in range(0, length):
        s += choice(alphabet)
    return s


def string_similarity(string1, string2):
    """
    Takes two strings of the same length and returns a proportion
    of how many characters they have the same in each position.
    """
    count = 0
    for i in range(0, len(string1)):
        if string1[i] == string2[i]:
            count += 1
    return count/len(string1)


m = 10**8
for n in range(1, 27):
    s1 = random_string(n, m)
    s2 = random_string(n, m)
    print(n, 1/n, string_similarity(s1, s2))

#!/usr/bin/python3

# As part of a guessing game with a friend I made up a secret code. The
# code was given in the form (x, y, z) where x, y, z are in the range 0
# to 255. This script goes through the process of decoding such encoded
# messages. The output is a name so it's possible you could optimise it
# further using a list but this is just a quick example of decoding.


from binascii import unhexlify
from gmpy2 import digits
from itertools import product


# the encoded message
encoded = (86, 121, 205)


# generates list of hex digits used
digits = []
for num in encoded:
    b16 = str("{0:x}".format(num))
    if len(b16) == 1:
        digits.extend(["0", str(b16)])
    else:
        digits.extend(list(b16))


# if list contains duplicates input was wrong
if len(digits) != len(set(digits)):
    print("Invalid input")
    exit(1)


# conver a given number into code
def word(number, chrlist):
    output = ""
    for digit in [int(x) for x in list(number)]:
        output += chrlist[digit-1]
    return output


# find all digit combinations that are ascii letters
alphabet, letters = [chr(x) for x in range(97, 123)], []
for pair in product(digits, repeat=2):
    try:
        character = unhexlify("".join(pair)).decode("ascii")
    except UnicodeDecodeError:
        pass
    if character in alphabet:
        letters.append(character)

# searches all letter combinations from decryption
count, decoded = 1, ""
while True:
    for combination in product(letters, repeat=count):
        decoded = "".join(combination)
        print(decoded+"\r")
    count += 1

#!/usr/bin/python3

# This script is used for automating the process of determining
# that any given number is not a Lychrel number. For more info
# see this link: https://en.wikipedia.org/wiki/Lychrel_number


def rev(num):
    # reverses a character order of an int
    return int(''.join([i for i in reversed(list(str(num)))]))


def output(num, count):
    # general formatting for output
    with open("lychrel.csv", "a") as file:
        file.write(str(num) + "," + str(count) + "\n")
    print(num, count)


def check(num):
    # checks lychrel properties of an int
    count, var = 0, num
    while var != rev(var):
        var = var + rev(var)
        count += 1
    output(num, count)


with open("lychrel.csv", "w+") as file:
    file.write("Number,Count\n")

num = 0
while True:
    check(num)
    num += 1

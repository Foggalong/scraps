#!/usr/bin/python

# quick script for checking if a number is prime

print "Prime Tester"

def isint(n):
	if int(n) == n:
		return 1
	else:
		return 0

# Needs starter of 2
primes = [2]

num = int(raw_input("Number: "))

n = 3
while n < num+1:
	sqrt = n**0.5
	x, plist = 0, []
	while primes[x] <= sqrt:
		plist.append(primes[x])
		x+=1
	check = 1
	for number in plist:
		if float(n) % number == 0:
			check = 0
			break
	if check == 1:
		primes.append(n)
	n+=1

if num in primes:
	print "%d is a prime." % num
elif num not in primes:
	print "%d is not a prime." % num
else:
	"Somethings's gone wrong!"

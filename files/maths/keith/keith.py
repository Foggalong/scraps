#!/usr/bin/python
print "This program lists all the Keith numbers in a ceratin range.\n"
lower, upper = int(raw_input("Lower bound: ")), int(raw_input("Upper bound: "))
print "\nList of Keith numbers between %s and %s:" % (lower, upper)

def AddDigits(list):
	total = 0
	for number in list:
		total += int(number)
	return total

for number in range(lower,upper+1):
	output, check, list1 = 0, 0, list(str(number))
	while int(output) < int(number):
		list1.append(AddDigits(list1)); list1.pop(0); output = list1[len(str(number))-1]
		if int(output) == int(number):
			print number
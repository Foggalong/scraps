#!/usr/bin/python
print "List of Keith numbers:"

def AddDigits(list):
	total = 0
	for number in list:
		total += int(number)
	return total

number = 1
while number > 0:
	output, check, list1 = 0, 0, list(str(number))
	while int(output) < int(number):
		list1.append(AddDigits(list1)); list1.pop(0); output = list1[len(str(number))-1]
		if int(output) == int(number):
			print number
	number += 1
#!/usr/bin/python3

def collatz(number, parameters):
	# parameters:
	# 		n - print number 
	# 		s - print sequence
	# 		l - print lenght
	#		t - show labels

	if 'n' in parameters:
		if 't' in parameters:
			return "Number:", number
		else:
			return number


	if 's' in parameters:
		hail = []
		hail.append(str(number))

		while number != 1:
			if number%2 == 1:
				number = number*3+1
			elif number%2 == 0:
				number = int(number/2)
			hail.append(str(number))

		if 't' in parameters:
			return "Sequence:", ", ".join(hail)
		else:
			return ", ".join(hail)
		if 'l' in parameters:
			if 't' in parameters:
				return "Length:", len(hail)
			else:
				return len(hail)


	if 'l' in parameters and 's' not in parameters:
		count = 1

		while number != 1:
			if number%2 == 1:
				number = number*3+1
			elif number%2 == 0:
				number = int(number/2)
			count += 1

		if 't' in parameters:
			return "Length:", count
		else:
			return count

for number in range(0, 11):
	print(str(collatz(3**number, 'l')))

# Ted's End Script
from time import sleep
while (exit):
	sleep(10)

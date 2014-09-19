from random import randint

print("Mastermind\n")
print("The mastermind has thought of a number")
print("between 0000 and 9999. In 20 turns you")
print("must guess this number. You may begin.")

print("o means correct number correct placed\n- means correct number wrong place")

number = []
for n in range(0, 4):
	number.append(str(randint(1, 6)))

guess, count = [], 0
while count <= 20:
	count += 1
	guess = list(str(input("\nGuess %d: " % count)))
	if guess == ['c','h','e','a','t']:
		print(number)
	else:
		result = []
		for x in range(0,4):
			if guess[x] == number[x]:
				result.append("o ")
			elif guess[x] in number:
				result.append("- ")
		print(''.join(result))
		if number == guess:
			break

if count <= 20:
	print("\nCongratulations, you broke the code!")
elif count > 20:
	print("\nYou were unable to crack the code this time.")

# Ted's End Code
from time import sleep
print("\n\nFin.")
while (exit):
	sleep(10)

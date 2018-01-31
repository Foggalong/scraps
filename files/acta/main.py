#!/usr/bin/python3

# Importing AC Modules
from modules import std
from modules import dev


# Version
version = "Indev 0.3"



# Messages
options_message = """
There is currently no option message. As the game develops
a customisable settings list will be implemented. The target
is to have this at least partly implemented by alpha release.
"""

gameplay_message = """
Unfortunately this early in development there's no
gameplay help/tutorials available. It generally just
works as you'd expect a text adventure might: commands
are things like "walk east", "dig crack"
"""

bugs_message = ("""
The game is still version %s so bugs are bound to crop
up all over the place. If you find any and you feel like
reporting me just email me at joshua.h.fogg@gmail.com
with the subject "AC:TT BUG". Thank you!
""" % version)

about_message = """
"Animal Corssing: Terminal Town" is a text adventure game 
based on the Nintendo classic series "Animal Corssing"
created by programmer in training Joshua Fogg as a learning
exercise. The game is still in it's early stages but feel
free to give it a spin and tell me what you think!

LEGAL NOTE
The content is not designed for commercial use
and all coded is licensed under the GPL. All content from
Nintendo is used under intended "fair use" but if this turns
out not to be the case contact me at joshua.h.fogg@gmail.com
and I will make all amdendments nessicary.
"""



# Main Program
print("\n"+"-"*30)
print("Animal Crossing: Terminal Town\n")
print("      Version: %s      " % (version))
print("-"*30)
run1 = 1
while run1 == 1:
	print("\nMAIN MENU")
	print("1. Start")
	print("2. Options")
	print("3. Help")
	print("4. Quit")
	start_ans = std.usr_input()
	if 	start_ans in ["1", "start"]:
		exec(open('game.py', "rb").read())
	elif start_ans in ["2", "options"]:
		run2 = 1
		while run2 == 1:
			print("\nOPTIONS MENU")
			print("1. Options)")
			print("2. Back")
			options_ans = std.usr_input()
			if 	options_ans in ["1", "options"]:
				print(options_message)
			elif options_ans in ["2", "back"]:
				run2 = 0
				pass
			else:
				std.mistake(options_ans)
				pass
	elif start_ans in ["3", "help"]:
		run2 = 1
		while run2 == 1:
			print("\nHELP MENU")
			print("1. Gameplay")
			print("2. Bugs")
			print("3. About")
			print("4. Back")
			help_ans = std.usr_input()
			if 	help_ans in ["1", "gameplay"]:
				print(gameplay_message)
				std.pause()
			elif help_ans in ["2", "bugs"]:
				print(bugs_message)
				std.pause()
			elif help_ans in ["3", "about"]:
				print(about_message)
				std.pause()
			elif help_ans in ["4", "back"]:
				run2 = 0
				pass
			else:
				std.mistake(help_ans)
				pass
	elif start_ans in ["4", "quit"]:
		run1 = 0
	else:
		std.mistake(start_ans)
		pass

# Program Ending
print("Thanks for playing!")
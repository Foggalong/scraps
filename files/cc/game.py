#!/usr/bin/python3

import time
from random import randint

# Game Vars
# Health
hvar = 100
svar = 100


# Fight
# stats not final

# player

# weapons
weaponls = ['bare hands', 'sword', 'axe', 'staff']
wpninpackls = [1, 1 ,1, 0]
wpnhealthls = [100, 20, 30, 50]
wpndamagels = [5, 7, 10, 20]
wpnchancels = [8, 7, 5, 6]

# monsters
monsterls = ['goblin', 'troll', 'warlock']
monhealthls = [10, 20, 50]
mondamagels = [5, 10, 15]
monchancels = [2, 5, 8] # value out of ten

#/Fight


class funct:
	def info(self, item):
		if item in monsterls:
			print("Name:", item)
			print("Type: monster")
			print("Health:", monhealthls[monsterls.index(item)])
			print("Damage:", mondamagels[monsterls.index(item)])
			print("Chance:", monchancels[monsterls.index(item)])
		elif item in weaponls:
			print("Name:", item)
			print("Type: weapon")
			print("Health:", wpnhealthls[weaponls.index(item)])
			print("Damage:", wpndamagels[weaponls.index(item)])
			print("Chance:", wpnchancels[weaponls.index(item)])
		else:
			print("No information could be found.")
	

	def fight(self, monster):
		global hvar
		ind = monsterls.index(monster)
		monhealth, mondamage, monchance = monhealthls[ind], mondamagels[ind], monchancels[ind]
		run = 1
		while run == 1:
			action = input("\n> ")
			# if 'attack' in action:
				# any(word in str1 for word in weapon)
			if action == 'fight':
				roll = randint(0, 10)
				if roll > monchance:
					monhealth -= 7
					print("You landed a blow!")
				elif roll == monchance:
					print("You and the", monster, "clashed!")
				elif roll < monchance:
					print("The", monster, "landed a blow!")
					hvar -= mondamage
				if monhealth < 1 or hvar < 1:
					if monhealth < 1:
						print("You killed the "+monster+"!\n")
					elif hvar < 1:
						print("The "+monster+" killed you!\n")
					break
			elif action == 'battle info':
				print("Your health:", hvar)
				print(monster+"'s health:", monhealth, "\n")
			elif action.split()[0] == 'info':
				try:
					funct.info(self, action.split()[1])
				except:
					print("Information about what?")

monster = monsterls[randint(0, len(monsterls)-1)]

action = input("A wild "+monster+" appears!\n> ")
if action == 'fight':
	funct.fight(funct, monster)
elif action == 'run':
	print("You ran away from the "+monster+"! WUSS!")



print("\nDebug died!")
print("Program fin.\nIt will close in\n1 mintue.")
time.sleep(60)


# A nice example of classes
"""
Paul 12
>>> class tut:
...     def name(self, name):
...             print(name, age)
...     age = 12
...
>>> tut.name("Paul")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: name() takes exactly 2 arguments (1 given)
>>> tut.name(tut, "Paul")
Paul 12
>>>
"""
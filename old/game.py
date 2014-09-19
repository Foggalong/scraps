import time
from random import randint

# Game Vars
# Health
hvar = 100
def health(hvar, n):
	hvar += int(n)
	if hvar > 100:
		hvar = 100
	elif hvar < 1:
		hvar = 0
	return hvar

# Stamina (when ready)
svar = 100
def stamina(svar, n):
	svar += int(n)
	if svar > 100:
		svar = 100
	elif svar < 1:
		svar = 0
	return svar

# Fight
weapon = ['bare hands', 'sword']
monsterls = ['goblin', 'troll']
monhealthls = [10, 20]
mondamagels = [-5, -10]
monchancels = [2, 5]			# Out of 10 based on difficulty
def fight(monster):
	ind = monsterls.index(monster)
	monhealth, mondamage, monchance = monhealthls[ind], mondamagels[ind], monchancels[ind]

	fight, otpt = 1, ""
	while fight == 1:
		action = input("> ")
		roll = randint(0, 10)
		if roll > monchance:
			print("You landed a blow!")
			monhealth -= 7
			if monhealth < 1:
				otpt, fight = 0, 0
		elif roll == monchance:
			print("You and the", monster, "clashed!")
		elif roll < monchance:
			print("The", monster, "landed a blow!")
			hvar = health(hvar, mondamage)
			if hvar == 0:
				otpt, fight = 1, 0
			
	return otpt

run = 1
while run == 1:
	monster = monsterls[randint(0, len(monsterls)-1)]
	ginpt = input("A wild "+monster+" appears!\n> ")
	if ginpt == 'fight':
		fight(monster)
		if fight(monster) == 0:
			print("You killed the "+monster+"!")
		elif fight(monster) == 1:
			print("The "+monster+" killed you!")
	else:
		break

print("You died!")




print("\n\n\nProgram fin.\nIt will close in\n1 mintue.")
time.sleep(60)

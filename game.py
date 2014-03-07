#!/usr/bin/python3

# Importing General Modules
from os import getcwd

# Importing AC Modules
from modules import std
from modules import dev
from modules import gam

# Importing Data
from data import mapd


# Main Program
location = [1,2]
print("Starting at",location)
while True:
	command = std.usr_input()
	if command.split()[0] == "quit":
		break
	elif command.split()[0] == "walk":
		direction = command.split()[1]
		# Old Area
		id_now = mapd.no_list[int(str(location).replace("[","").replace("]","").replace(",","").replace(" ",""))]
		current_area = mapd.areas[id_now-1]
		if current_area[direction+"_edge"] in ["nul","bridge","slope"]:
			# New Area
			location = gam.walk(location, direction)
			id_new = mapd.no_list[int(str(location).replace("[","").replace("]","").replace(",","").replace(" ",""))]
			new_area = mapd.areas[id_new-1]
			if current_area[direction+"_edge"] == "bridge":
				print("You walked across the bridge from %s to %s!" % (current_area["type"], new_area["type"]))
			elif current_area[direction+"_edge"] == "slope":
				print("You along the slope from %s to %s!" % (current_area["type"], new_area["type"]))
			else:
				print("Walked from %s to %s!" % (current_area["type"], new_area["type"]))
		else:
			print("Can't walk that way: there's a %s in the way!" % current_area[direction+"_edge"])
		print("Now at",location)
	elif command.split()[0] == "enter":
		try:
			building = command.split()[1]
			id_now = mapd.no_list[int(str(location).replace("[","").replace("]","").replace(",","").replace(" ",""))]
			current_area = mapd.areas[id_now-1]
			if building == current_area["type"]:
				# BUG: At the minute you can access any building from any area
				# BUG sort of FIXED - not sure how to deal with villager houses...or buildings that aren't correct
				exec(open(getcwd()+"/buildings/"+building+"/main.py", "rb").read())
			else:
				print("The %s isn't around here!" % building)
		except:
			print("Oh no! That's not a valid building")
	else:
		print("Oh no! %s is not a valid command" % command)
#!/usr/bin/python3

# Module Information
# ----------------------
# This module contains all the function which are used as
# specifically in the game

def foo():
	pass

def walk(coord, direction):
	if direction == "north":
		if (coord[1]+1) > 5:
			print("Can't walk any further north.")
		else:
			coord[1] += 1
	elif direction == "east":
		if (coord[0]+1) > 5:
			print("Can't walk any further east.")
		else:
			coord[0] += 1
	elif direction == "south":
		if (coord[1]-1) < 1:
			print("Can't walk any further south.")
		else:
			coord[1] -= 1
	elif direction == "west":
		if (coord[0]-1) < 1:
			print("Can't walk any further west.")
		else:
			coord[0] -= 1
	return coord

# def walk(location, direction):
	# direction = command.split()[1]
	#Old Area
	# id_now = mapd.no_list[int(str(location).replace("[","").replace("]","").replace(",","").replace(" ",""))]
	# current_area = mapd.areas[id_now-1]
	# if current_area[direction+"_edge"] in ["nul","bridge","slope"]:
		#New Area
		# location = gam.walk(location, direction)
		# id_new = mapd.no_list[int(str(location).replace("[","").replace("]","").replace(",","").replace(" ",""))]
		# new_area = mapd.areas[id_new-1]
		# if current_area[direction+"_edge"] == "bridge":
			# print("You walked across the bridge from %s to %s!" % (current_area["type"], new_area["type"]))
		# elif current_area[direction+"_edge"] == "slope":
			# print("You along the slope from %s to %s!" % (current_area["type"], new_area["type"]))
		# else:
			# print("Walked from %s to %s!" % (current_area["type"], new_area["type"]))
	# else:
		# print("Can't walk that way: there's a %s in the way!" % current_area[direction+"_edge"])
	# print("Now at",location)
coord = [1,2]

while True:
	direction = input("Walk? ").lower().strip()
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
	print(coord)

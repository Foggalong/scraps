#!/usr/bin/python3

# Module Information
# ----------------------
# This module contains all the function which are used in
# the development process. These will only be used in the
# game until it's final beta then they will be removed ( 
# appart from the snapshot releases)

# notes
# -----------
# could refine this by only displaying the south edge as
# the top most north edge is completely predictable
# also when upping to the 6x6 (7x6 for the gate?) could
# switch it to a preset east edge with river in the middle
# then the rest being random?

area_11 = {
		"id": 11,
		"type": "beach",
		"north_edge": "cliff",
		"east_edge": "nul",
		"south_edge": "sea",
		"west_edge": "sea"
		}

area_12 = {
		"id": 12,
		"type": "home",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "cliff",
		"west_edge": "bound"
		}

area_13 = {
		"id": 13,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "river",
		"south_edge": "nul",
		"west_edge": "bound"
		}

area_14 = {
		"id": 14,
		"type": "villager_1",
		"north_edge": "river",
		"east_edge": "river",
		"south_edge": "nul",
		"west_edge": "bound"
		}

area_15 = {
		"id": 15,
		"type": "grass",
		"north_edge": "bound",
		"east_edge": "nul",
		"south_edge": "river",
		"west_edge": "bound"
		}

area_21 = {
		"id": 21,
		"type": "beach",
		"north_edge": "slope",
		"east_edge": "nul",
		"south_edge": "sea",
		"west_edge": "nul"
		}

area_22 = {
		"id": 22,
		"type": "grass",
		"north_edge": "river",
		"east_edge": "nul",
		"south_edge": "slope",
		"west_edge": "nul"
		}

area_23 = {
		"id": 23,
		"type": "museum",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "river",
		"west_edge": "river"
		}

area_24 = {
		"id": 24,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "river"
		}

area_25 = {
		"id": 25,
		"type": "villager_2",
		"north_edge": "bound",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_31 = {
		"id": 31,
		"type": "beach",
		"north_edge": "cliff",
		"east_edge": "cliff",
		"south_edge": "sea",
		"west_edge": "nul"
		}

area_32 = {
		"id": 32,
		"type": "grass",
		"north_edge": "river",
		"east_edge": "nul",
		"south_edge": "cliff",
		"west_edge": "nul"
		}

area_33 = {
		"id": 33,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "river",
		"west_edge": "nul"
		}

area_34 = {
		"id": 34,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_35 = {
		"id": 35,
		"type": "gate",
		"north_edge": "gate",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_41 = {
		"id": 41,
		"type": "villager_3",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "cliff",
		"west_edge": "cliff"
		}

area_42 = {
		"id": 42,
		"type": "grass",
		"north_edge": "bridge",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_43 = {
		"id": 43,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "bridge",
		"west_edge": "nul"
		}

area_44 = {
		"id": 44,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_45 = {
		"id": 45,
		"type": "town_hall",
		"north_edge": "bound",
		"east_edge": "nul",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_51 = {
		"id": 51,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "bound",
		"south_edge": "bound",
		"west_edge": "nul"
		}

area_52 = {
		"id": 52,
		"type": "tom_nook",
		"north_edge": "river",
		"east_edge": "bound",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_53 = {
		"id": 53,
		"type": "grass",
		"north_edge": "nul",
		"east_edge": "bound",
		"south_edge": "river",
		"west_edge": "nul"
		}

area_54 = {
		"id": 54,
		"type": "pond",
		"north_edge": "nul",
		"east_edge": "bound",
		"south_edge": "nul",
		"west_edge": "nul"
		}

area_55 = {
		"id": 55,
		"type": "grass",
		"north_edge": "bound",
		"east_edge": "bound",
		"south_edge": "nul",
		"west_edge": "nul"
		}

areas = [
	area_11, area_12, area_13, area_14, area_15,
	area_21, area_22, area_23, area_24, area_25,
	area_31, area_32, area_33, area_34, area_35,
	area_41, area_42, area_43, area_44, area_45,
	area_51, area_52, area_53, area_54, area_55
	]

no_list = {
	11: 1, 12: 2, 13: 3, 14: 4, 15: 5,
	21: 6, 22: 7, 23: 8, 24: 9, 25: 10,
	31: 11, 32: 12, 33: 13, 34: 14, 35: 15,
	41: 16, 42: 17, 43: 18, 44: 19, 45: 20,
	51: 21, 52: 22, 53: 23, 54: 24, 55: 25,
	}
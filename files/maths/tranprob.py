#!/usr/bin/python3

# Transportation Problem Solver
print("This a program for solving basic Transportation Problems.\n")
print("It relys on all stock and demand values being known integers,")
print("and all the unit costs also being known.\n")
print("It will take all the nesisary data inputs for its calculations")
print("to find an optimal solution to the problem.")

# Supply Data Entry
supply_name, supply_stock, entry, count = [], [], 1, 1
while entry == 1:
	print("\nSupply Point %d" % count)
	ans = 0
	while ans == 0:		
		try:
			supply_name.append(str(input("Name: ")))
			supply_stock.append(int(input("Stock: ")))
			break
		except:
			print("Answer not understood.\nPlease try again.")
	ans = 0
	while ans == 0:
		q = input("Enter more data? (y/n)").lower().strip()
		if q == "y":
			ans = 1
		elif q == "n":
			entry = 0
			ans = 1
		else:
			print("Answer not understood.\nPlease try again.")
	count+=1

# Demand Data Entry
demand_name, demand_demand, entry, count = [], [], 1, 1
while entry == 1:
	print("\nDemand Point %d" % count)
	ans = 0
	while ans == 0:		
		try:
			demand_name.append(str(input("Name: ")))
			demand_demand.append(int(input("Demand: ")))
			break
		except:
			print("Answer not understood.\nPlease try again.")
	ans = 0
	while ans == 0:
		q = input("Enter more data? (y/n)").lower().strip()
		if q == "y":
			ans = 1
		elif q == "n":
			entry = 0
			ans = 1
		else:
			print("Answer not understood.\nPlease try again.")
	count+=1

# Test for unbalanced situation
supply_total, demand_total = 0, 0
for stock in supply_stock:
	supply_total += stock
for demand in demand_demand:
	demand_total += demand
if supply_total == demand_total:
	print("\nThis is a balanced problem.")
elif supply_total > demand_total:
	print("\nThis is an unbalanced problem.")
	print("A dummy demand point has been created.")
	ans = 0
	while ans == 0:
		q = input("Do you wish to name the dummy demand point? (y/n)").lower().strip()
		if q == "y":
			ans = 0
			while ans == 0:		
				try:
					demand_name.append(str(input("Name: ")))
					demand_demand.append(supply_total-demand_total)
					ans = 1; break
				except:
					print("Answer not understood.\nPlease try again.")
					ans = 1
		elif q == "n":
			demand_name.append("dummy")
			demand_demand.append(supply_total-demand_total)
			ans = 1
		else:
			print("Answer not understood.\nPlease try again.")
elif supply_total < demand_total:
	print("\nThis problem has no solution.")
	print("This is because the total demand is greater than")
	print("the total stock. Please start this program again")
	print("and try using a higher stock or lower demand.")
	# End Script
	from time import sleep
	while (exit):
		sleep(10)

# Route Data Entry
from itertools import product
routes, route_name, route_cost, rename, ans, count = [], [], [], 0, 0, 0
for combination in product(supply_name, demand_name):
	routes.append(combination)
while ans == 0:
	q = input("\nDo you wish to rename the routes? (y/n)").lower().strip()
	if q == "y":
		rename, ans = 1, 1
	elif q == "n":
		ans = 1
	else:
		print("Answer not understood.\nPlease try again.")
for route in routes:
	print("\nRoute %s (%d routes remaining)" % (str(route).replace("(","").replace(")","").replace(",","").replace("'","").replace(" "," to "), len(routes)-count))
	ans = 0
	while ans == 0:		
		try:
			if rename == 1:
				route_name.append(str(input("Name: ")))
			elif rename == 0:
				route_name.append(str(route).replace("(","").replace(")","").replace(",","").replace("'","").replace(" "," to "))
			route_cost.append(int(input("Cost: ")))
			break
		except:
			print("Answer not understood.\nPlease try again.")
	count+=1


# Test output
print("supply_stock", supply_stock)
print("demand_demand", demand_demand)
print("Pos", position)
print("Sup", supply_stock[position%len(supply_stock)])
print("Dem", demand_demand[position%len(demand_demand)])
print("Sol", initial_solution)


# Finding an Initial Solution
initial_solution, position = [], 0
while position != len(routes)-1:
	if supply_stock[position%len(supply_stock)] > demand_demand[position%len(demand_demand)]:
		initial_solution.append([routes[position], supply_stock[position%len(supply_stock)]-demand_demand[position%len(demand_demand)]])
		supply_stock[position%len(supply_stock)], demand_demand[position%len(demand_demand)] = supply_stock[position%len(supply_stock)]-demand_demand[position%len(demand_demand)], 0
		position += 1
	elif supply_stock[position%len(supply_stock)] < demand_demand[position%len(demand_demand)]:
		initial_solution.append([routes[position], supply_stock[position%len(supply_stock)]])
		demand_demand[position%len(demand_demand)], supply_stock[position%len(supply_stock)] = demand_demand[position%len(demand_demand)]-supply_stock[position%len(supply_stock)], 0
		position += len(demand_name)-1
	elif supply_stock[position%len(supply_stock)] == demand_demand[position%len(demand_demand)]:
		initial_solution.append([routes[position], supply_stock[position%len(supply_stock)]])
		demand_demand[position%len(demand_demand)], supply_stock[position%len(supply_stock)] = 0, 0
		position += len(demand_name)
	print("Pos", position)
	print("Sup", supply_stock[position%len(supply_stock)])
	print("Dem", demand_demand[position%len(demand_demand)])
	print("Sol", initial_solution)

# Input Variables Test Output
print()
print("Supply:", supply_name, supply_stock)
print("Demand:", demand_name, demand_demand)
print("Route:", route_name, route_cost)

# Teds End Script
print("\n\nProgram finished.")
from time import sleep
while (exit):
	sleep(10)

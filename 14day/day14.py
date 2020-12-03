#! /bin/usr/env python3

import sys
import queue

filename = "14day-input.txt"

if len(sys.argv) > 1:
	filename = sys.argv[1]

recipes = {}
ore_total = 0
materials = {}
mat_q = []

with open(filename, "r") as fp:
	
	for line in fp:

		temp = line.split(',')
		temp2 = temp[-1:][0].split(' ')[-2:]
		product = str(temp2[1][:-1])

		recipes[product] = [int(temp2[0]), {}]
		
		for chem in temp:
			
			if "=>" in chem:
				chem = chem.split('=')[0]

			chem = chem.strip().split(' ')
	
			recipes[product][1][chem[1]] = int(chem[0])
			
			materials[chem[1]] = 0


materials["FUEL"] = 1
mat_q.append("FUEL")

while len(mat_q) > 0:

	prod = mat_q.pop(0)
	if prod in mat_q:
		continue

	recipe = recipes[prod]
	multiplier = 1

	while recipe[0] * multiplier < materials[prod]:
		multiplier += 1

	for ingredient in recipe[1]:
		
		if ingredient == "ORE":
			ore_total += recipe[1]["ORE"] * multiplier

		else:
			materials[ingredient] += recipe[1][ingredient] * multiplier
			mat_q.append(ingredient)

		materials[prod] = 0

	print(f"####prod: {prod:<5} - {mat_q}")
	print(materials)

print(f"Total ORE needed: {ore_total}")

#! /bin/usr/env python3

import sys
from functools import reduce


class Planet:

	def __init__(self, name="   "):
		self.name = name
		self.orbiters = []
		self.orbit_val = 0

	def orbiter_toString(self):

		out_str = ""

		for body in self.orbiters:
			out_str = out_str + f" {body.name}"

		return out_str


def find_orbit_vals(planet, depth):

	total = 0

	for body in planet.orbiters:
		total += find_orbit_vals(body, depth+1)

	return total+depth


orbit_list = dict()

with open("6day-input.txt", "r") as fp:
	
	for line in fp:
		bodies = line[0:-1].split(')')

		if bodies[0] not in orbit_list:
			orbit_list[bodies[0]] = Planet(bodies[0])

		if bodies[1] not in orbit_list:
			orbit_list[bodies[1]] = Planet(bodies[1])

		orbit_list[bodies[0]].orbiters.append(orbit_list[bodies[1]])

		print(f"{orbit_list[bodies[0]].name} ){orbit_list[bodies[0]].orbiter_toString()}")

print(f"Orbital Total: {find_orbit_vals(orbit_list['COM'], 0)}")



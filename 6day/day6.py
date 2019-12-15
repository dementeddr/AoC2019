#! /bin/usr/env python3

import sys
from functools import reduce


class Planet:

	def __init__(self, name="   "):
		self.name = name
		self.orbiters = []
		self.orbit_val = 0
		self.orbiting = None
		self.height_from_body = -1

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


def find_body_height(planet, height):

	print(f"{planet.name}: {planet.height_from_body}, {height}")

	if planet.height_from_body > -1:
		return planet.height_from_body + height

	elif planet.name == 'COM':
		return -1;

	else: 
		planet.height_from_body = height
		return find_body_height(planet.orbiting, height+1)


orbit_list = dict()

with open("6day-input.txt", "r") as fp:
	
	for line in fp:
		bodies = line[0:-1].split(')')

		if bodies[0] not in orbit_list:
			orbit_list[bodies[0]] = Planet(bodies[0])

		if bodies[1] not in orbit_list:
			orbit_list[bodies[1]] = Planet(bodies[1])

		orbit_list[bodies[0]].orbiters.append(orbit_list[bodies[1]])
		orbit_list[bodies[1]].orbiting = orbit_list[bodies[0]]


for body in orbit_list.values():
	orbiting = "   "

	if body.orbiting is not None:
		orbiting = body.orbiting.name

	print(f"{orbiting} ) -{body.name}- ){body.orbiter_toString()}")

print(f"Orbital Total: {find_orbit_vals(orbit_list['COM'], 0)}\n")

find_body_height(orbit_list['SAN'].orbiting, 0)

total_jumps = find_body_height(orbit_list['YOU'].orbiting, 0)

print(f"Jumps to Santa: {total_jumps}")


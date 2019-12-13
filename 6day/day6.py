#! /bin/usr/env python3

import sys


orbit_list = []

with open("6day-input.txt", "r") as fp:
	
	for line in fp:
		orbit = line.split(')')

		orbit_list.append((orbit[0], orbit[1][:-1]))
		
		print(orbit_list[-1])


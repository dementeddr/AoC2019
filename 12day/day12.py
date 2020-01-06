#! /bin/urs/env python3

import sys
import itertools

filename = "12day-input.txt"

if len(sys.argv) > 1:
    filename = sys.argv[1]

#moon_combos = list(itertools.permutations(range(4),2))
moon_combos = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
moon_pos = []
moon_vel = [[0 for axis in range(3)] for moon in range(4)]

print(moon_combos)

with open(filename, "r") as fp:
    
    for line in fp:
        nums = line.split(',')
        pos = [0,0,0]
        pos[0] = int(nums[0][3:])
        pos[1] = int(nums[1][3:])
        pos[2] = int(nums[2][3:-2])
        moon_pos.append(pos)
        print(pos)


for tick in range(100000):
    
    delta_vel = [[0 for axis in range(3)] for moon in range(4)]

    for pair in moon_combos:
        for axis in range(3):
    
            if moon_pos[pair[0]][axis] > moon_pos[pair[1]][axis]:
                moon_vel[pair[0]][axis] -= 1
                moon_vel[pair[1]][axis] += 1
            elif moon_pos[pair[0]][axis] < moon_pos[pair[1]][axis]:
                moon_vel[pair[0]][axis] += 1
                moon_vel[pair[1]][axis] -= 1
            else:
                pass
                

    for moon in range(4):
        for axis in range(3):
            moon_pos[moon][axis] += moon_vel[moon][axis]

    outstring1 = ""
    outstring2 = ""

    for moon in range(len(moon_pos)):
        outstring1 = outstring1 + f"P - {str(moon_pos[moon]):15s} "
        outstring2 = outstring2 + f"V -- {str(moon_vel[moon]):15s} "

    print(outstring1)
    #print(outstring2)

total_energy = 0


for moon in range(4):

    kinetic = 0
    potential = 0

    for axis in range(3):
        kinetic += abs(moon_pos[moon][axis])
        potential += abs(moon_vel[moon][axis])

    total_energy += kinetic * potential

print(f"Total Energy = {total_energy}")

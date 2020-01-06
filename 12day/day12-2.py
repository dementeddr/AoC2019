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

with open(filename, "r") as fp:
    
    for line in fp:
        nums = line.split(',')
        pos = [0,0,0]
        pos[0] = int(nums[0][3:])
        pos[1] = int(nums[1][3:])
        pos[2] = int(nums[2][3:-2])
        moon_pos.append(pos)
        print(pos)

state_loop = [0, 0, 0]

for axis in range(3):

    loop_found = False
    tick = 1
    #state_history = {}

    while tick < 2000000 and not loop_found:

        for pair in moon_combos:
            if moon_pos[pair[0]][axis] > moon_pos[pair[1]][axis]:
                moon_vel[pair[0]][axis] -= 1
                moon_vel[pair[1]][axis] += 1
            elif moon_pos[pair[0]][axis] < moon_pos[pair[1]][axis]:
                moon_vel[pair[0]][axis] += 1
                moon_vel[pair[1]][axis] -= 1
            else:
                pass
        
        for moon in range(4):
            moon_pos[moon][axis] += moon_vel[moon][axis]
        
        vels = list(map(lambda moon: moon[axis], moon_vel))
        
        if len(list(filter(lambda moon: moon!=0, vels))) == 0:
            loop_found = True
            state_loop[axis] = tick * 2

        state = list(map(lambda moon: moon[axis], moon_pos))
        state =  state + list(map(lambda moon: moon[axis], moon_vel))

        print(f"{axis}  {tick}  {state}")

        tick += 1

print(state_loop)


#! /bin/usr/env python3

import sys
import os
import math
import cmath
import heapq

filename = "10day-input.txt"
#output_file = "output.txt"
broids = {}
real_broids = {}
base = [17,23]
field = []

#os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

if len(sys.argv) > 3:
    base = [int(sys.argv[2]), int(sys.argv[3])]


with open(filename, "r") as fp:

    for line in fp:
        field.append(line)

for i in range(len(field)):
    for j in range(len(field[i])):

        if field[i][j] == '#':
            x = j - base[0]
            y = -(i - base[1])
            
            if x == 0 and y == 0:
                continue

            coord = complex(y, x) #to make the math easier, flip the real and imaginary portions 
            #print(f"({j:3},{i:3}) = ({x:3},{y:3}) = {coord}")
            coord = cmath.polar(coord)
            phi = (coord[1] + math.tau) % math.tau #normalize the phase to [0,tau]
            r = coord[0]
            
            if phi not in broids:
                broids[phi] = []

            heapq.heappush(broids[phi], r)
            real_broids[(r,phi)] = (j,i)

"""
for phi in sorted(broids.keys()):
    print(f"{phi:7f} -{broids[phi]}")
"""

num = 1

while len(broids) > 0:
    
    for phi in sorted(broids.keys()):
        r = heapq.heappop(broids[phi])

        if len(broids[phi]) == 0:
            del broids[phi]

        coord = real_broids[(r,phi)]

        if num == 200:
            print(f"{num:4d} = ({r:7f} , {phi:7f}) = {coord}")

        num += 1
    




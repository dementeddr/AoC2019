#! /bin/usr/env python3

import sys
import os
import math

filename = "10day-input.txt"
#output_file = "output.txt"
broids = []

#os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, "r") as fp:

    i = 0
    for line in fp:
        for j in range(len(line)):

            if line[j] == '#':
                broids.append((i,j))

        i += 1

max_viewable = 0
best_candidate = (-1,-1)

for cand in broids:
    #print(cand)
    views = set()

    for ass in broids:
        x = ass[0] - cand[0]
        y = ass[1] - cand[1]

        angle = math.atan2(x,y) #TRIG FTW

        #print(angle)
        views.add(angle)

    if max_viewable < len(views):
        max_viewable = len(views)
        best_candidate = cand

print(f"best={best_candidate}  max={max_viewable}")

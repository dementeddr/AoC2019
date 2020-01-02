#! /bin/usr/env python3

import sys
import os
import math

filename = "10day-input.txt"
#output_file = "output.txt"
broids = []
field = []
#os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

with open(filename, "r") as fp:

    for line in fp:
        field.append(line)

for i in range(len(field)):
    for j in range(len(field[i])):

        if field[i][j] == '#' or field[i][j] == 'O':
            broids.append((j,i))


max_viewable = 0
best_candidate = (-1,-1)

for cand in broids:
    #print(cand)
    views = set()

    for ass in broids:
        x = ass[0] - cand[0]
        y = -(ass[1] - cand[1])

        if x == 0 and y == 0:
            continue

        angle = math.atan2(y,x) #TRIG FTW

        #print(angle)
        views.add(angle)

    if max_viewable < len(views):
        max_viewable = len(views)
        best_candidate = cand

print(f"best={best_candidate}  max={max_viewable}")

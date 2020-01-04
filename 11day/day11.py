#! /bin/usr/env python3

import sys
import os
from intcomp import IntComp
from intcomp import Status
from field import Field
from field import coord

filename = "11day-input.txt"
output_file = "output.txt"

if os.path.exists(output_file):
    os.remove(output_file)


if len(sys.argv) > 1:
    filename = sys.argv[1]

comp = IntComp(filename)
hull = Field()

status = Status.INPUT_REQUIRED
pos = coord(0,0)
rot = 0  #0 = up, increasing clockwise
count = set()

# Day 11.2
hull.set_val(1, pos)

while status == Status.INPUT_REQUIRED:
    
    paint = hull.get_val(pos)
    outs = comp.execute_tape(paint)

    status = outs[0]
    turn = outs[1][1]

    hull.set_val(outs[1][0], pos)
    count.add((pos.x, pos.y))

    if turn == 0:
        rot = (rot - 1) % 4
    elif turn == 1:
        rot = (rot + 1) % 4

    if rot == 0:
        pos.y += 1
    elif rot == 1:
        pos.x += 1
    elif rot == 2:
        pos.y -= 1
    elif rot == 3:
        pos.x -= 1
    else:
        print(f"ERROR: rotation = {rot}. That's not right, chief")
        exit(1)

    #print(f"paint={paint}, pos={pos}, rot={rot}")

    
print(f"{status} count = {len(count)}")

with open(output_file, "w+") as outfp:
    plane = hull.get_full()

    for row in plane:
        line = ""
        for col in row:
            if col == 0:
                line += '.'
            else:
                line += '#'
       
        line += '\n'
        outfp.write(line)

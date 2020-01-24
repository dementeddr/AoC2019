#! /bin/usr/env python3

import sys
import os
from intcomp import IntComp
from intcomp import Status
from field import Field
from field import coord

filename = "15day-input.txt"
output_file = "output.txt"

if os.path.exists(output_file):
    os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

comp = IntComp(filename)
halls = Field()

status = Status.INPUT_REQUIRED
pos = coord(0,0)
move = coord(0,0)

mapping = {-1:'#', 0:'.', 65537:'@'}


def set_dist(loc):

    dist = 2**16

    adjacent = []
    adjacent.append(halls.get_val(loc.x, loc.y+1))
    adjacent.append(halls.get_val(loc.x, loc.y-1))
    adjacent.append(halls.get_val(loc.x+1, loc.y))
    adjacent.append(halls.get_val(loc.x-1, loc.y))

    for adj in adjacent:
        if adj > 0 and adj < dist:
            dist = adj

    halls.set_val(dist+1, loc)

    return dist



oxy_dist = 0

while status == Status.INPUT_REQUIRED:

    button = "0"
    move = coord(pos.x, pos.y)

    while (button not in "wasdqe") or (len(button) != 1):
        button = input("Button: ").strip().lower()

    if button == 'w':
        button = 1
        move.y += 1
    elif button == 's':
        button = 2
        move.y -= 1
    elif button == 'a':
        button = 3
        move.x -=1
    elif button == 'd':
        button = 4
        move.x += 1
    elif button == 'q':
        halls.display(mapping)
        continue
    elif button == 'e':
        halls.display()
        print(f"Center: {halls.center}")
        continue
    else:
        print(f"ERROR. Unrecognized button {str(button)}")

    outs = comp.execute_tape(button)
    print(outs)
    status = outs[0]

    if outs[1][0] == 0:
        halls.set_val(-1, move)
    elif outs[1][0] == 1:
        pos = move
        if halls.get_val(pos) != 0:
            oxy_dist = halls.get_val(pos)
        elif pos.x != 0 or pos.y != 0:
            oxy_dist += 1
            halls.set_val(oxy_dist, pos)
        else:
            oxy_dist = 0
        #set_dist(pos)

    elif outs[1][0] == 2:
        pos = move
        oxy_dist += 1
        #oxy_dist = set_dist(pos)
        print(f"Success!")
        break

    print(f"@ {pos} = {outs[1][0]}")


print(f"Oxy is at {pos}. Dist = {oxy_dist}")
halls.display()

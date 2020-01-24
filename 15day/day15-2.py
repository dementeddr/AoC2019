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



def turn_cc(rot):
    if   rot == 1:
        return 3
    elif rot == 2:
        return 4
    elif rot == 3:
        return 2
    elif rot == 4:
        return 1
    else:
        print(f"ERROR: Bad Rotation {rot}")
    

def turn_cw(rot):
    if   rot == 1:
        return 4
    elif rot == 2:
        return 3
    elif rot == 3:
        return 1
    elif rot == 4:
        return 2
    else:
        print(f"ERROR: Bad Rotation {rot}")
    

comp = IntComp(filename)
halls = Field()

status = Status.INPUT_REQUIRED
pos = coord(0,0)
move = coord(0,0)
oxy_pos = coord(0,0)

mapping = {-1:'#', 0:'.', -2:'@', -3:'O'}
oxy_found = False
oxy_dist = 0
max_dist = 0
num_attempts = 0
right_hand = 1
iteration = 1


halls.set_val(-2, pos)


while status == Status.INPUT_REQUIRED:

    button = 0
    move = coord(pos.x, pos.y)

    if num_attempts == 0:
        button = right_hand
    elif num_attempts == 1:
        button = turn_cc(right_hand)
    elif num_attempts >= 2:
        right_hand = turn_cc(right_hand)
        button = turn_cc(right_hand)
        num_attempts = 1

    if button == 1:
        move.y += 1
    elif button == 2:
        move.y -= 1
    elif button == 3:
        move.x -= 1
    elif button == 4:
        move.x += 1
    else:
        print(f"ERROR. Unrecognized button {str(button)}")

    outs = comp.execute_tape(button)
    #print(outs)
    status = outs[0]

    if outs[1][0] == 0:
        halls.set_val(-1, move)
        num_attempts += 1

    elif outs[1][0] == 1:
        pos = move
        if num_attempts == 0:
            right_hand = turn_cw(right_hand)
        else: 
            num_attempts = 0

        if oxy_found:
            if  pos == coord(0,0):
                oxy_dist += 1
            elif pos == oxy_pos:
                oxy_dist = 0
                break
            elif halls.get_val(pos) > 0:
                oxy_dist = halls.get_val(pos)
            elif halls.get_val(pos) == 0:
                oxy_dist += 1
                halls.set_val(oxy_dist, pos)
            else:
                halls.display(mapping)


        if oxy_dist > max_dist:
            max_dist = oxy_dist

    elif outs[1][0] == 2:
        pos = move
        oxy_pos = pos
        halls.set_val(-3,oxy_pos)
        if not oxy_found:
            oxy_found = True
            halls.display(mapping)
            input(f"Found! Oxy is at {pos}.")
        else:
            break
        

    #print(f"{iteration:>4d}  @ {pos} = {outs[1][0]}  hand = {right_hand}  moxy = {max_dist}")
    iteration += 1

    """
    if iteration % 100 == 0:
        halls.display(mapping)
    """

halls.display(mapping)
print(f"Time to full oxygen diffusion: {max_dist} minutes")

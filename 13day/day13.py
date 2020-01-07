#! /bin/usr/env python3

import sys
import os
from intcomp import IntComp
from intcomp import Status


def display_arcade(arcade):
    for row in arcade:
        outstr = ""
        for col in row:
        
            char = ""

            if col == 0:
                char = ' '
            elif col == 1:
                char = '@'
            elif col == 2:
                char = '#'
            elif col == 3:
                char = '='
            elif col == 4:
                char = 'O'

            outstr += char

        print(outstr)



filename = "13day-input.txt"
output_file = "output.txt"

if os.path.exists(output_file):
    os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

comp = IntComp(filename)
outs = comp.execute_tape()

arcade = [[0 for row in range(38)] for col in range(21)]

print(outs[0])
print(type(outs[1][0]))

for tile in range(0,len(outs[1]),3):
    data = outs[1][tile:tile+3]
    #coord = tuple(data[0:2])
    #print(f"{data}  {coord}")
    #arcade[coord] = data[2]
    arcade[data[1]][data[0]] = data[2]

"""
tiles = sorted(arcade.keys())

for i in tiles:
    print(i)
"""

block_count = 0


#!/usr/bin/env python3

import sys
import copy
import time

def draw_up(delta, grid, mark, head):

    syms = {' ', mark}
    crosses = []

    for i in range(1,delta+1):
        
        if grid[head["x"]][head["y"]+i] not in syms:
            crosses.append({"x": head["x"], "y": head["y"]+i})
            grid[head["x"]][head["y"]+i] = '+'
        else:
            grid[head["x"]][head["y"]+i] = mark

    return crosses
        

def draw_wire(grid, segs, mark, origin):

    if mark == '+' or mark == ' ':
        print("bad mark: " + mark)
        exit(1)

    print(str(segs))

    head = copy.deepcopy(origin)

    for wire in segs:

        print(wire)
        print(str(wire[1:]))
        delta = int(wire[1:])

        if wire[0] == 'U':
            draw_up(delta, grid, mark, head)
        if wire[0] == 'D':
            print(".")
        if wire[0] == 'R':
            print(".")
        if wire[0] == 'L':
            print(".")
        else:
            print("unknown direction character: " + wire[0])
            exit(2)
        

def output_grid(grid):

    with open("3day-output.txt", "w+") as ofp:
        
        for col in grid:
            for row in col:
                base = ""
                ofp.write(base.join(row) + '\n')

    print("Write complete")


def main():

    print("Start Main")
    cur = time.time()
    grid_size = 100
    grid = [[' ' for col in range(grid_size*2)] for row in range(grid_size*2)]
    print("Well shit. dt = " + str(time.time() - cur))

    origin = {"x": grid_size, "y": grid_size}
    head1 = copy.deepcopy(origin)
    head2 = copy.deepcopy(origin)

    wires = []

    with open("test-input.txt", "r") as fp:
        line = fp.readline()

        while line:

            segs = line.split(',')
            wires.append(segs)
            line = fp.readline()

    crosses = []

    draw_wire(grid, wires[0], '1', origin)
    #draw_wire(grid, segs[1], '2', origin)

    output_grid(grid)


if __name__ == "__main__":
    main()

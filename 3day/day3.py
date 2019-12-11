#!/usr/bin/env python3

import sys
import time
import heapq


def move_head(seg, head):
    if seg[0] == 'U':
        head[1] += 1

    elif seg[0] == 'D':
        head[1] -= 1

    elif seg[0] == 'R':
        head[0] += 1

    elif seg[0] == 'L':
        head[0] -= 1

    else:
        print ("unknown direction character: " + seg[0])
        exit(2)

    return (head[0], head[1])


def main():

    wire1 = set()
    wire1d = {}
    wirelen = 0
    head = [0,0]
    lines = []

    filename = "3day-input.txt"

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename, "r") as fp:
        text = fp.readlines()

        lines.append(text[0].split(','))
        lines.append(text[1].split(','))
    
    for seg in lines[0]:
        delta = int(seg[1:])
    
        for i in range(1,delta+1):

            wirelen += 1
            coord = move_head(seg, head)
            wire1.add(coord)
            wire1d[coord] = wirelen
            #print(coord)
        
    #print(str(wire1))

    head = [0,0]
    wirelen = 0
    crosses = []

    for seg in lines[1]:
        delta = int(seg[1:])
        
        for i in range(1, delta+1):
            wirelen += 1
            coord = move_head(seg, head)

            if (coord in wire1):
                heapq.heappush(crosses, (wirelen, coord))

            #print(coord)

    min_delay = wirelen**2
    min_matt = wirelen**2

    # I want to point out that I know this reiteration is strictly unnecessary and that I could
    # have done it while looping through the second wire. I just wanted to see where all the
    # crosses were. For science.
    for cross in crosses:

        manhattan = abs(cross[1][0]) + abs(cross[1][1])
        delay = cross[0] + wire1d[cross[1]] 

        if delay < min_delay:
            min_delay = delay

        if manhattan < min_matt:
            min_matt = manhattan

        print(f"{str(cross):25s}Manhattan: {manhattan:-6d}  Delay: {delay:-8d}")

    print(f"Minimum Manhattan Distance: {min_matt:-6d} Minimum Signal Delay: {min_delay:-8d}")


if __name__ == "__main__":
    
    print("Start Main")
    cur = time.time()

    main()

    print("End Main: dt = " + str(time.time() - cur))

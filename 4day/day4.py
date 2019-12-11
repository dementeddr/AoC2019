#!/usr/bin/env python3

import sys
import os

floor = 246540
ceiling = 787419
output = "4day-output.txt"

if len(sys.argv) > 2:
    floor = int(sys.argv[1])
    ceiling = int(sys.argv[2])

    if ceiling < floor:
        print("Bad Inputs")
        sys.exit(1)

os.remove(output)

count = 0

with open(output, "w+") as fp:

    for n in range (floor,ceiling+1,1):

        txt = str(n)

        if list(txt) != sorted(txt):
            continue

        adjacency = 0

        for i in range(len(txt)-1):
            if txt[i] == txt[i+1]:
                adjacency = 1
                break

        if adjacency == 0:
            continue
        
        count += 1
        fp.write(f"{txt}\n")

print(f"Range: {floor}-{ceiling}  Count: {count}")
           

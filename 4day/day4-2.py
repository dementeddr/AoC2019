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

        histo = {}

        for c in txt:
            if c in histo.keys():
                histo[c] += 1
            else:
                histo[c] = 1

        if 2 not in histo.values():
            continue
        
        count += 1
        fp.write(f"{txt}\n")

print(f"Range: {floor}-{ceiling}  Count: {count}")
           

#! /bin/usr/env python3

import sys
import os
from intcomp import IntComp

filename = "9day-input.txt"
output_file = "output.txt"

os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

comp = IntComp(filename)

with open(output_file, "w+") as fp:

    #try:
    outs = comp.execute_tape()
    print(outs)

    outs = comp.execute_tape([1])
    print(outs)
    """
    except:
        print("OH NO AN EXCEPTION")
        for i in comp.tape:
            fp.write(f"{i}\n")
    """

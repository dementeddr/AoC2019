#! /bin/usr/env python3

import sys
import os
from intcomp import IntComp
from intcomp import Status
from field import Field
from field import coord

filename = "17day-input.txt"
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

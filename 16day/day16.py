#! /bin/usr/env python3

import sys
import os
import numpy as np

filename = "16day-input.txt"
output_file = "output.txt"

if os.path.exists(output_file):
    os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

signal = ""

with open(filename, "r") as fp:
    signal = np.array(list(map(int, list(fp.readline()[:-1]))))

print(signal)

patterns = []

for i in range(signal.size):
    base  = [ 0 for x in range(i+1)]
    base += [ 1 for x in range(i+1)]
    base += [ 0 for x in range(i+1)]
    base += [-1 for x in range(i+1)]

    mod = []
    
    while len(mod) < signal.size+1:
        mod += base 

    patterns.append(np.array(mod[1: signal.size + 1]))
    #print(patterns[-1])


patterns = np.array(patterns)

#phase2 = np.dot(patterns, signal)
#phase2 = np.array(list(map(lambda val: abs(val) % 10, phase2)))

phase = signal

for i in range(100):
    phase = np.array(list(map(lambda val: abs(val) % 10, np.dot(patterns, phase)))) #Have I mentioned I love python?
    print(f"{i+1:3d} = {phase}")

print(f"Final = {phase[:8]}")

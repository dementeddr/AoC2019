#! /bin/usr/env Python3

from intcomp2 import IntComp
from intcomp2 import Status
import itertools

phase_vals = [5, 6, 7, 8, 9]
filename = "7day-input.txt"
phase_perms = list(itertools.permutations(phase_vals))
amp_outputs = []
max_output = 0

#phase_perms = [[9,7,8,5,6]]  #TEST INPUT PLEASE IGNORE

for phases in phase_perms:

    amps = []

    for i in range(5):
        a = IntComp(filename)
        a.execute_tape([phases[i]])
        amps.append(a)

    status = Status.OK
    prev = 0
    index = 0

    while status < 3:
        
        outs = amps[index].execute_tape([prev])
        status = outs[0]
        
        if len(outs[1]) > 0: 
            prev = outs[1][0]
        
        print(f"{index} - {outs}")

        if status == Status.FINISHED and index == 4: # If it's stupid and it works, it's not stupid
            break

        index = (index + 1) % 5
    
    amp_outputs.append(prev)

    if prev > max_output:
        max_output = prev


for i in range(len(amp_outputs)):
    print(f"{phase_perms[i]} = {amp_outputs[i]}")

print(max_output)

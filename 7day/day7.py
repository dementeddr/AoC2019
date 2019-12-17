#! /bin/usr/env Python3

import intcomp
import itertools

tape = intcomp.read_input("7day-input.txt")
phases = [0, 1, 2, 3, 4]

phase_perms = list(itertools.permutations(phases))
max_thrust = 0
max_thrust_seq = []

for phase_seq in phase_perms:
    prev = 0

    for p in phase_seq:
        outputs = intcomp.execute_tape(tape, [p, prev])
        prev = outputs[0]

    print(f"{phase_seq}: {prev}")

    if prev > max_thrust:
        max_thrust = prev
        max_thrust_seq = phase_seq

print(f"Phase Sequence {max_thrust_seq} achieves thrust {max_thrust}")

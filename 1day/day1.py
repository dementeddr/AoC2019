#! /usr/bin/env python3

mass = 0

with open("1day-input.txt","r") as fp:

    for line in fp:
        mass += (int(line) // 3) -2

print(mass)

#! /usr/bin/env python3

fuel = 0
base_mass = 0

with open("1day-input.txt","r") as fp:

    for line in fp:
        prev = int(line)
        
        while prev > 0:
            prev = (prev // 3) -2
        
            if prev > 0:
                    fuel += prev
        

print(fuel)

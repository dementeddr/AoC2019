#! /bin/usr/env python3

import sys
import queue

filename = "14day-input.txt"

if len(sys.argv) > 1:
    filename = sys.argv[1]

recipes = {}
materials = {}
ore_total = 0
nodes = queue.SimpleQueue()
#excess = {}

with open(filename, "r") as fp:
    
    for line in fp:

        temp = line.split(',')
        temp2 = temp[-1:][0].split(' ')[-2:]
        product = str(temp2[1][:-1])

        recipes[product] = [int(temp2[0]), {}]
        
        for chem in temp:
            
            if "=>" in chem:
                chem = chem.split('=')[0]

            chem = chem.strip().split(' ')
            #print(chem)
    
            recipes[product][1][chem[1]] = int(chem[0])
            materials[chem[1]] = 0
            #excess[chem[1]] = 0



materials["ORE"] = 0
materials["FUEL"] = 0
nodes.put("FUEL")

while nodes.qsize() > 0:

    prod = nodes.get()






for key in sorted(recipes.keys()):
    print(f"{key:5s} = {recipes[key]}")


while 

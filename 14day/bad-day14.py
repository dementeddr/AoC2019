#! /bin/usr/env python3

import sys

filename = "14day-input.txt"

if len(sys.argv) > 1:
    filename = sys.argv[1]

recipes = {}
requirements = {}
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
            requirements[chem[1]] = 0
            #excess[chem[1]] = 0

requirements["ORE"] = 1
requirements["FUEL"] = 0

for key in sorted(recipes.keys()):
    print(f"{key:5s} = {recipes[key]}")



def sum_ore(prod):


    if prod == "ORE":
        print(f"P ORE   = 1")
        return 1
    
    for comp in recipes[prod][1].keys():
        
        if requirements[comp] == 0:
            requirements[prod] += sum_ore(comp) * recipes[prod][1][comp] 
        else:
            requirements[prod] += requirements[comp]

        #print(f"C {comp:5s} = {requirements[comp]}")
    
    print(f"P {prod:5s} = {requirements[prod]}")
    return requirements[prod]
   

total = sum_ore("FUEL")
"""
for key in sorted(requirements.keys()):
    print(f"{key:5s} = {requirements[key]}")
"""
print(f"FUEL  = {total}")

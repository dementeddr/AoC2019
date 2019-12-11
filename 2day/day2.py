#!/usr/bin/env python

import sys

def tape_op(tape, address):
    
    op = tape[address]
    var1 = tape[tape[address+1]]
    var2 = tape[tape[address+2]]
    dest = tape[address+3]

    if op == 1:
        tape[dest] = var1 + var2
    elif op == 2:
        tape[dest] = var1 * var2
    else:
        print("ERROR: Unrecognized opcode: " + op)
        print("DUMP: address - " + address)
        print(str(tape))

#    out = [address, tape[address], tape[address+1], tape[address+2], var1, var2, dest, tape[dest]] #debug
#    print(str(out)) #debug


def check_input(noun, verb):

    fin = open("2day-input.txt", "r")

    in_str = ""

    if fin.mode == 'r':
        in_str = fin.read()

#    print(str(in_str)) #debug

    tape = list(map(int,in_str.split(',')))
    tape[1] = noun
    tape[2] = verb

#    print(str(tape)) #debug

    address = 0

    while tape[address] != 99:
#        print(tape[address]) #debug
        tape_op(tape, address)
#        out = [tape[address], tape[address+1], tape[address+2], tape[address+3]]
#        print(str(address) + "  " + str(out)) 
        address += 4

#    print(str(tape))

    return tape[0]

def main():
   
    for i in range(70, 71, 1):
        for j in range(14,15,1):

            out = check_input(i,j)
            cat = ""

            if out == 19690720:
                cat = "!"

            print("f" + str([i, j]) + " = " + str(out) + " " + cat)



if __name__ == "__main__":
    main()

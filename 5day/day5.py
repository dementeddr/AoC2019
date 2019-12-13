#!/usr/bin/env python3

import sys


"""
Determines the literal values of all parameters for an intcode instruction.

INPUTS:
    tape: list of integers in the form of an intcode program
    index: currently executing opcode of the intcode program
    inst_len: the number of integers in tape that are part of the instruction
    write_param: indicates which parameter is the address of the instruction output. Is the index of the parameter list. (this is gross, but I haven't figured out anything better)

RETURN:
    params: list of integers, containing the literal inputs to the instruction calling this function.
"""
def get_params(tape, index, inst_len, write_param):

	mode_digits = str(tape[index])[-3::-1]
	params = tape[index+1:index+inst_len]
	modes = []
	#print(f"mode_digits: {mode_digits}  params: {params}")

	for i in range(inst_len-1):
		#print (f"i: {i}  modes: {modes}")
		if len(mode_digits) > i:
			#print(f"mode_digits length: {len(mode_digits)}")
			modes.append(int(mode_digits[i]))
		else:
			modes.append(0)
			#print(f"modes append: {modes}")


	for i in range(len(params)):
		if write_param != i and modes[i] == 0:
			params[i] = tape[params[i]]
			#print(f"i: {i}  write_p: {write_param}  params: {params}")		

	#print(f"{tape}  {index}  {params}")
	return params



def instr_add(tape, index):
    
    inst_len = 4
    params = get_params(tape, index, inst_len, 2)

    tape[params[2]] = params[0] + params[1]

    return index + inst_len



def instr_multiply(tape, index):
    
    inst_len = 4
    params = get_params(tape, index, inst_len, 2)

    tape[params[2]] = params[0] * params[1]

    return index + inst_len



def instr_input(tape, index):

    inst_len = 2

    get_params(tape, index, inst_len, 0) # For test output purposes only.

    while True:
        # Because humans are dumb.
        try:
            text = input("\nSHIP INPUT: ")
            num = int(text)
            tape[tape[index+1]] = num
            break

        except:
            print("BAD INPUT PLEASE TRY AGAIN")

    return index + inst_len



def instr_output(tape, index):

    inst_len = 2
    params = get_params(tape, index, inst_len, -1)
    
    print(f"\nSHIP OUTPUT: {params[0]}")

    return index + inst_len



def instr_jump_if(tape, index, if_true):
	
	inst_len = 3
	params = get_params(tape, index, inst_len, -1)
	ip = index

	if (params[0] == 0) != if_true:
		ip = params[1]
	else:
		ip = index + inst_len

	return ip



def instr_less_than(tape, index):
	
	inst_len = 4
	params = get_params(tape, index, inst_len, 2)
	
	if params[0] < params[1]:
		tape[params[2]] = 1
	else:
		tape[params[2]] = 0

	return index + inst_len



def instr_equals(tape, index):
	
	inst_len = 4
	params = get_params(tape, index, inst_len, 2)
	
	if params[0] == params[1]:
		tape[params[2]] = 1
	else:
		tape[params[2]] = 0

	return index + inst_len



"""
Executes an intcode program

INPUT:
    tape: list of integers that form an intcode program
RETURN:
"""
def execute_tape(tape):

    index = 0

    while index >= 0 and index < len(tape):

        opcode = int(str(tape[index])[-2:]) #I love python.

        if opcode == 1:
            index = instr_add(tape, index)
        elif opcode == 2:
            index = instr_multiply(tape, index)
        elif opcode == 3:
            index = instr_input(tape, index)
        elif opcode == 4:
            index = instr_output(tape, index)
        elif opcode == 5:
            index = instr_jump_if(tape, index, True)
        elif opcode == 6:
            index = instr_jump_if(tape, index, False)
        elif opcode == 7:
            index = instr_less_than(tape, index)
        elif opcode == 8:
            index = instr_equals(tape, index)
        elif opcode == 99:
            index = -1
            break
        else:
            print(f"Unrecognized opcode \"{opcode}\" at index {index}.")
            exit(2)

    if index >= len(tape):
        print(f"Tape overflow with index {index}")
        exit(3)


"""
Given a filepath, opens the file and reads the text as tape.

INPUT:
    filename: a valid unix path to a list of comma-separated integers.

RETURN: list of integers
"""
def read_input(filename):

    text = ""

    with open(filename, "r") as fp:
        text = fp.readline()

    if text == "":
        print("No Input")
        exit(2) 

    tape = list(map(int,text.split(',')))

    return tape



def main():

    print("READING INTCODE PROGRAM")

    filename = ""

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    if filename == "":
        filename = "5day-input.txt"

    tape = read_input(filename)

    execute_tape(tape)

    print("\nEND OF INTCODE PROGRAM\n" + str(tape))



if __name__ == "__main__":
    main()

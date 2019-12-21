#!/usr/bin/env python3

import sys
from enum import Enum


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



class Status:
    FINISHED = 0
    OK = 1
    INPUT_REQUIRED = 2
    OUT_OF_BOUNDS = 3
    BAD_OPCODE = 4



class IntComp:

    """
    Determines the literal values of all parameters for an intcode instruction.

    INPUTS:
        tape: list of integers in the form of an intcode program
        head: currently executing opcode of the intcode program
        inst_len: the number of integers in tape that are part of the instruction
        write_param: indicates which parameter is the address of the instruction output. Is the head of the parameter list. (this is gross, but I haven't figured out anything better)

    RETURN:
        params: list of integers, containing the literal inputs to the instruction calling this function.
    """
    def get_params(self, inst_len, write_param):

        mode_digits = str(self.tape[self.head])[-3::-1]
        params = self.tape[self.head+1:self.head+inst_len]
        modes = []

        for i in range(inst_len-1):
            if len(mode_digits) > i:
                modes.append(int(mode_digits[i]))
            else:
                modes.append(0)


        for i in range(len(params)):
            if write_param != i and modes[i] == 0:
                params[i] = self.tape[params[i]]

        return params



    def instr_add(self):
        
        inst_len = 4
        params = self.get_params(inst_len, 2)

        self.tape[params[2]] = params[0] + params[1]

        self.head += inst_len
        return Status.OK



    def instr_multiply(self):
        
        inst_len = 4
        params = self.get_params(inst_len, 2)

        self.tape[params[2]] = params[0] * params[1]

        self.head += inst_len
        return Status.OK



    def instr_input(self, inputs):

        inst_len = 2

        if len(inputs) == 0:
            return Status.INPUT_REQUIRED
            
        num = inputs.pop(0)
        self.tape[self.tape[self.head+1]] = num
        
        self.head += inst_len
        return Status.OK



    def instr_output(self, outputs):

        inst_len = 2
        params = self.get_params(inst_len, -1)
        
        outputs.append(params[0])
        
        self.head += inst_len
        return Status.OK



    def instr_jump_if(self, if_true):
        
        inst_len = 3
        params = self.get_params(inst_len, -1)
        ip = self.head

        if (params[0] == 0) != if_true:
            ip = params[1]
        else:
            ip = self.head + inst_len

        if ip >= 0 and ip < len(self.tape):
            self.head = ip
            return Status.OK
        else:
            return Status.OUT_OF_BOUNDS



    def instr_less_than(self):
        
        inst_len = 4
        params = self.get_params(inst_len, 2)
        
        if params[0] < params[1]:
            self.tape[params[2]] = 1
        else:
            self.tape[params[2]] = 0

        self.head += inst_len
        return Status.OK



    def instr_equals(self):
        
        inst_len = 4
        params = self.get_params(inst_len, 2)
        
        if params[0] == params[1]:
            self.tape[params[2]] = 1
        else:
            self.tape[params[2]] = 0

        self.head += inst_len
        return Status.OK



    """
    Executes an intcode program

    INPUT:
        tape: list of integers that form an intcode program
        human_IO:   True if you want IO to interact with user. 
                False if you want IO to interact with another program.
    RETURN:
    """
    def execute_tape(self, inputs = []):

        outputs = []
        status = Status.OK

        while self.head >= 0 and self.head < len(self.tape):

            opcode = int(str(self.tape[self.head])[-2:]) #I love python.

            if opcode == 1:
                status = self.instr_add()
            elif opcode == 2:
                status = self.instr_multiply()
            elif opcode == 3:
                status = self.instr_input(inputs)
            elif opcode == 4:
                status = self.instr_output(outputs)
            elif opcode == 5:
                status = self.instr_jump_if(True)
            elif opcode == 6:
                status = self.instr_jump_if(False)
            elif opcode == 7:
                status = self.instr_less_than()
            elif opcode == 8:
                status = self.instr_equals()
            elif opcode == 99:
                status = Status.FINISHED
            else:
                print(f"Unrecognized opcode \"{opcode}\" at index {self.head}.")
                exit(2)

            if status != Status.OK:
                break

        if self.head >= len(self.tape):
            print(f"Tape overflow with head {self.head}")
            exit(3)

        return (status, outputs)



    def __init__(self, tape):
        self.tape = tape
        self.head = 0


    def __init__(self, filename):
        self.tape = read_input(filename)
        self.head = 0
        #self.Status = STATUS()


# end of class



"""
    def main():

        print("READING INTCODE PROGRAM")

        filename = ""

        if len(sys.argv) > 1:
            filename = sys.argv[1]

        if filename == "":
            filename = "7day-input.txt"

        comp = IntComp(filename)

        comp.execute_tape()

        print("\nEND OF INTCODE PROGRAM\n" + str(tape))



if __name__ == "__main__":
    IntComp.main()
"""

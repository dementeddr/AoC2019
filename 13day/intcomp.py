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



class Status(Enum):
    FINISHED = 0
    OK = 1
    INPUT_REQUIRED = 2
    NEG_INDEX = 3
    BAD_OPCODE = 4
    NOT_A_NUM = 5



class IntComp:

    """
    Extends the length of the tape list until it's long enough to encompass the tartget index

    INPUTS:
        target: An integer that is the head index that the tape needs to be long enough to contain.
    """
    def extend_tape(self, target):

        if target < 0:
            print(f"Attempted to access negative index {target}. Pretend this is an exception.") 
            return Status.NEG_INDEX

        while len(self.tape) <= target:
            self.tape.append(0)

        return Status.OK


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

        #print(f"GP S> L: {len(self.tape)}, H: {self.head}, W: {write_param},  {self.tape[self.head : self.head + inst_len]}  M: {modes}")

        for i in range(len(params)):
        
            if write_param != i:

                if modes[i] == 0:
                    self.extend_tape(params[i])
                    params[i] = self.tape[params[i]]
                elif modes[i] == 1:
                    pass # 1 is immediate mode, meaning no need to resolve an address.
                elif modes[i] == 2:
                    self.extend_tape(params[i] + self.rel_base)
                    params[i] = self.tape[params[i] + self.rel_base]
                else:
                    print(f"Invalid opcode {self.tape[self.head]} at head {self.head}")
                    return Status.BAD_OPCODE
            else:

                if modes[i] == 0:
                    self.extend_tape(params[i])
                if modes[i] == 1:
                    print(f"Invalid opcode {self.tape[self.head]} at head {self.head}")
                    return Status.BAD_OPCODE
                if modes[i] == 2:
                    params[i] += self.rel_base
                    self.extend_tape(params[i])

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
        
        params = self.get_params(inst_len, 0)
        num = inputs.pop(0)
        self.extend_tape(params[0])
        self.tape[params[0]] = num
        
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

        if ip < 0:
            return Status.NEG_HEAD
        
        self.extend_tape(ip)
        self.head = ip
        return Status.OK



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



    def instr_adj_base(self):
        
        inst_len = 2
        params = self.get_params(inst_len, -1)

        self.rel_base += params[0]

        self.head += inst_len
        return Status.OK



    """
    Executes the intcode program the IntCode object was created with.

    INPUT:
        inputs = []: You can optionally pass in a list of integers that will be used as input in 
            order each time opcode 3 is encountered. If no list is used or the end of the list is
            reached, the next time the program requires input, it will exit with Status.INPUT_REQUIRED 
    RETURN:
        A tuple with the following contents:
        [0] The status that the program exited with. If Status.INPUT_REQUIRED is output, run 
            execute_tape again with new inputs to continue execution.
        [1] A list of all the outputs produced by the program execution.
    """
    def execute_tape(self, inputs = []):

        outputs = []
        status = Status.OK

        """
        for i in inputs:
            if i isn't a number, return Status.NOT_A_NUM 
        """
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
            elif opcode == 9:
                status = self.instr_adj_base()
            elif opcode == 99:
                status = Status.FINISHED
            else:
                print(f"Unrecognized opcode \"{opcode}\" at index {self.head}.")
                exit(2)

            if status != Status.OK:
                break

            if self.head > len(self.tape) -1:
                self.extend_tape(head)

        if self.head >= len(self.tape):
            print(f"Tape overflow with head {self.head}")
            exit(3)

        return (status, outputs)



    def __init__(self, tape):
        self.tape = tape
        self.rel_base = 0
        self.head = 0


    def __init__(self, filename):
        self.tape = read_input(filename)
        self.rel_base = 0
        self.head = 0

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

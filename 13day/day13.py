#! /bin/usr/env python3

import sys
import os
import time
import intcomp
from intcomp import IntComp
from intcomp import Status


def display_arcade(arcade):
    for row in arcade:
        outstr = ""
        for col in row:
        
            char = ""

            if col == 0:
                char = ' '
            elif col == 1:
                char = '@'
            elif col == 2:
                char = '#'
            elif col == 3:
                char = '='
            elif col == 4:
                char = 'O'

            outstr += char

        print(outstr)



filename = "13day-input.txt"
output_file = "output.txt"

if os.path.exists(output_file):
    os.remove(output_file)

if len(sys.argv) > 1:
    filename = sys.argv[1]

#tape = read_input(filename)
#tape[0] = 0
#comp = IntComp(tape)
comp = IntComp(filename)
comp.tape[0] = 2

arcade = [[0 for row in range(38)] for col in range(21)]

status = Status.INPUT_REQUIRED
score = 0
ball = [0,0]
ball_prev = [0,0]
paddle = 0
button = 1
iteration = 0

while status == Status.INPUT_REQUIRED:

    """
    while button != "a" and button != "s" and button != " ":
        button = input("INPUT:")

    print(" - ")

    if button == "a":
        button = -1
    elif button == "s":
        button = 1
    elif button == " ":
        button = 0
    """

    outs = comp.execute_tape(button)
    status = outs[0]
    data = outs[1]

    for index in range(0,len(data),3):

        tile = data[index:index+3] 

        if tile[0] == -1 and tile[1] == 0:
            score = tile[2]
        else:
            arcade[tile[1]][tile[0]] = tile[2]

        if tile[2] == 4:
            ball_prev[0] = ball[0]
            ball = tile[0:2]
        elif tile[2] == 3:
            paddle = tile[0]

    ball_sides = [0,0]
    
    #if ball[0] > 0:
    ball_sides[0] = arcade[ball[1]][ball[0]-1]
    #if ball[0] < len(arcade[ball[1]]) - 1:
    ball_sides[1] = arcade[ball[1]][ball[0]+1]

    #Hashtag AI
    if ball_sides[0] in [1,2]:
        button = 1
    elif ball_sides[1] in [1,2]:
        button = -1
    elif paddle < ball[0]:
        button = 1
    elif paddle > ball[0]:
        button = -1
    elif paddle == ball[0]:
        if ball_prev[0] == ball[0]:
            button = 0
        elif ball_prev[0] < ball[0]:
            button = 1
        elif ball_prev[0] > ball[0]:
            button = -1

    #Hashtag Cheating
    if iteration == 865:
        button = -1
    if iteration == 1351:
        button = 1

    display_arcade(arcade)
    
    outstr = f"{paddle}:{button} - {ball_sides[0]} ({ball[0]},{ball[1]}) {ball_sides[1]}"
    print(f"DEBUG: {outstr:>30s}")
    print(f"ITER: {iteration:31}")
    print(f"SCORE: {score:30}\n")
    
    time.sleep(0.01)
    iteration += 1

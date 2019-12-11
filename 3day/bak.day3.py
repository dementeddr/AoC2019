#!/usr/bin/env python3

import sys

def find_dimensions(segs):

        Up = 0
        Dn = 0
        Rt = 0
        Lf = 0
        vert_cur = 0
        vert_max = 0
        vert_min = 0
        horz_cur = 0
        horz_max = 0
        horz_min = 0


        for w in segs:
            val = int(w[1:])
            
            if w[0] == 'U':
                Up += val
                vert_cur += val
            elif w[0] == 'D':
                Dn += val
                vert_cur -= val
            elif w[0] == 'R':
                Rt += val
                horz_cur += val
            elif w[0] == 'L':
                Lf += val
                horz_cur -= val
            else:
                print ("unknown direction character: " + w[0])
                exit(2)

            if vert_cur > vert_max:
                vert_max = vert_cur

            if vert_cur < vert_min:
                vert_min = vert_cur

            if horz_cur > horz_max:
                horz_max = horz_cur

            if horz_cur < horz_min:
                horz_min = horz_cur

        print(f"Up: {Up}\nDn: {Dn}\nLf: {Lf}\nRt: {Rt}\nVmax: {vert_max}\nVmin: {vert_min}\nHmax: {horz_max}\nHmin {horz_min}\n - ")

        return [vert_max, vert_min, horz_max, horz_min]


def main():

    dimensions = []
    wires = []

    with open("3day-input.txt", "r") as fp:
        line = fp.readline()

        while line:

            segs = line.split(',')

            dims = find_dimensions(segs)

            wires.append(segs)
            dimensions.append(dims)
    
            line = fp.readline()

    if wires == [] or dimensions == [] or len(wires) != len(dimensions):
        print("wires or dimensions missing or mismatched")
        exit(1)


if __name__ == "__main__":
    main()

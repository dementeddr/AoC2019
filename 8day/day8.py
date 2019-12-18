#! /bin/usr/env python3

width = 25
height = 6

text = ""

with open("8day-input.txt", "r") as fp:
    text = list(map(int, fp.readline()[:-1]))

pic = []
least_zs = width * height
least_zs_index = 0

print(f"{len(pic)}  {len(text)}")

for layer in range(0,len(text),width*height):
    dist = [0,0,0] #The only pixel values are 0, 1, and 2, so i get to be real clever here.

    for pixel in text[layer:layer+(width*height)]:
        dist[pixel] += 1

    pic.append(dist)
    print(dist)

    if least_zs > dist[0]:
        least_zs = dist[0]
        least_zs_index = len(pic)-1

print(f"CHECKSUM\nZeros: {pic[least_zs_index][0]}   Product: {pic[least_zs_index][1] * pic[least_zs_index][2]}")

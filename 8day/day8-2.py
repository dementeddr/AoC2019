#! /bin/usr/env python3

width = 25
height = 6

text = ""

with open("8day-input.txt", "r") as fp:
    text = list(map(int, fp.readline()[:-1]))

layer_len = width * height
num_layers = len(text) // layer_len

pic = [2] * layer_len

print(f"{len(text)}  {layer_len}  {num_layers}")

for pixel in range(layer_len):
    for bit in text[pixel::layer_len]:
        if bit < 2:
            pic[pixel] = bit
            break

render = ""

for i in range(layer_len):
    #render += str(pic[i])
    if pic[i] == 1:
        render = render + '#'
    else:
        render += ' '

for i in range(0,layer_len,width):
    print(render[i:i+width])

#print(render)

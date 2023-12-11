import math
import numpy as np
direction, doofe_linie, *nodes = open("input.txt").read().splitlines()
network = {}
for line in nodes:
    position, next_pos = line.split(" = ")
    next_pos = next_pos[1:-1]
    network[position] = next_pos.split(", ")

starting_pos = [pos for pos in network if pos.endswith("A")]

loops = []

for position in starting_pos:
    steps = 0
    loop = []
    i = 0
    z = None
    current_pos = position
    while True:
        while steps == 0 or not current_pos.endswith("Z"):
            steps += 1
            if direction[i] == "L":
                current_pos = network[current_pos][0]
            else:
                current_pos = network[current_pos][1]
            i += 1
            if i == len(direction):
                i = 0
                
        loop.append(steps)
        
        if z is None:
            z = current_pos
            steps = 0
        elif current_pos == z:
            break
            
    loops.append(loop)
print(loops)
single_nums = [loop[0] for loop in loops]
result = math.lcm(*single_nums)
print(result)




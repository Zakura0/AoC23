direction, doofe_linie, *nodes = open("input.txt").read().splitlines()
network = {}
for line in nodes:
    position, next_pos = line.split(" = ")
    next_pos = next_pos[1:-1]
    network[position] = next_pos.split(", ")

steps = 0
current_pos = "AAA"

i = 0
while current_pos != "ZZZ":
    steps += 1
    if direction[i] == "L":
        current_pos = network[current_pos][0]
    else:
        current_pos = network[current_pos][1]
    i += 1
    if i == len(direction):
        i = 0
print(steps)

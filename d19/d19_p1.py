def check_accepted(item, label):
    if label == "R":
        return False
    if label == "A":
        return True
    
    rules, end = workflows[label]

    for part, symbol, value, location in rules:
        if symbol == "<":
            if item[part] < value:
                return check_accepted(item, location)
        if symbol == ">":
            if item[part] > value:
                return check_accepted(item, location) 
    return check_accepted(item, end)

p1, p2 = open("input.txt").read().split("\n\n")
workflows = {}

for line in p1.splitlines():
    label, instructions = line[:-1].split("{")
    rules = instructions.split(",")
    workflows[label] = ([], rules[-1])
    rules.pop()
    for rule in rules:
        inequality, location = rule.split(":")
        part = inequality[0]
        symbol = inequality[1]
        value = int(inequality[2:])
        workflows[label][0].append((part, symbol, value, location))

accepted = 0

for line in p2.splitlines():
    item = {}
    for equations in line[1:-1].split(","):
        part, value = equations.split("=")
        item[part] = int(value)
    if check_accepted(item, "in"):
        accepted += sum(item.values())

print(accepted)

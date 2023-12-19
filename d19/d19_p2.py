p1, _ = open("input.txt").read().split("\n\n")
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

def count_possibilities(ranges, label):
    if label == "R":
        return 0
    if label == "A":
        product = 1
        for lb, ub in ranges.values():
            product *= ub - lb + 1
        return product
    
    rules, end = workflows[label]

    total_accepted = 0

    for part, symbol, value, location in rules:
        lb, ub = ranges[part]
        if symbol == "<":
            true_half = (lb, min(value - 1, ub))
            false_half = (max(lb, value), ub)
        else:
            true_half = (max(lb, value + 1), ub)
            false_half = (lb, min(value, ub))
        if true_half[0] <= true_half[1]:
            copied_ranges = dict(ranges)
            copied_ranges[part] = true_half
            total_accepted += count_possibilities(copied_ranges, location)
        if false_half[0] <= false_half[1]:
            ranges[part] = false_half
        else:
            break
    else:
        total_accepted += count_possibilities(ranges, end)
    return total_accepted


    
parts = {part: (1, 4000) for part in "xmas"}
print(count_possibilities(parts, "in"))

def find_mirror(pattern):
    for row in range(1, len(pattern)):
        upper = pattern[:row][::-1]
        lower = pattern[row:]
        
        upper = upper[:len(lower)]
        lower = lower[:len(upper)]
        
        if upper == lower:
            return row
        
    return 0
sum_p1 = 0

for pattern_block in open("input.txt").read().split("\n\n"):
    pattern = pattern_block.splitlines()
    row = find_mirror(pattern)
    sum_p1 += row * 100
    col = find_mirror(list(zip(*pattern)))
    sum_p1 += col
print(sum_p1)
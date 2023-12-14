def find_mirror(pattern):
    for row in range(1, len(pattern)):
        upper = pattern[:row][::-1]
        lower = pattern[row:]
        
        sum_faults_overall = 0
        for line1, line2 in zip(upper, lower):
            sum_faults_in_line = 0
            for char1, char2 in zip(line1, line2):
                if char1 == char2:
                    sum_faults_in_line += 0
                else:
                    sum_faults_in_line += 1
            sum_faults_overall += sum_faults_in_line
        if sum_faults_overall == 1:
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
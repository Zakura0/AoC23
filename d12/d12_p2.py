known_calcs = {}
def count_arrangements(pattern, nums):

    if pattern == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in pattern else 1
    
    config = (pattern, nums)
    
    if config in known_calcs:
        return known_calcs[config]
    
    sum_configs = 0
    if pattern[0] == "." or pattern[0] == "?":
        sum_configs += count_arrangements(pattern[1:], nums)
    
    if pattern[0] == "#" or pattern[0] == "?":
        if nums[0] <= len(pattern) and "." not in pattern[:nums[0]] and (len(pattern) == nums[0] or pattern[nums[0]] != "#"):
            sum_configs += count_arrangements(pattern[nums[0] + 1:], nums[1:])
    
    known_calcs[config] = sum_configs
    return sum_configs

sum_p1 = 0

for line in open("input.txt"):
    pattern, nums = line.split()
    nums += ("," + nums) * 4
    nums = tuple(map(int, nums.split(",")))
    pattern = "?".join([pattern] * 5)
    sum_p1 += count_arrangements(pattern, nums)
print(sum_p1)
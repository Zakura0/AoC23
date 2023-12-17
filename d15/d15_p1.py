def hash(string):
    value = 0    
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

initialization_sequence = open("input.txt").read().splitlines()[0].split(",")
#bastard
print(initialization_sequence)
print(sum(map(hash, initialization_sequence)))
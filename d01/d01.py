import re
with open("input.txt", "r") as input:
    split =  input.read().strip().split("\n")

#Part 1
sum = 0
for line in split:
    num_line = re.sub("\D", "", line)
    first = num_line[0]
    last = num_line[-1]
    sum += int(first + last)
print(sum)

#Part 2
# sum = 0
# digits = [["one",1], ["two",2] , ["three",3], ["four",4], ["five",5], ["six",6], ["seven",7], ["eight",8], ["nine",9]]
# for line in split:
#     for digit in digits:
#         line = line.replace(digit[0], str(digit[1]))
#     num_line = re.sub("\D", "", line)
#     first = num_line[0]
#     last = num_line[-1]
#     sum += int(first + last)
# print(sum)

#Part 2 Versuch 2
sum = 0
digits = [["one",1], ["two",2] , ["three",3], ["four",4], ["five",5], ["six",6], ["seven",7], ["eight",8], ["nine",9]]
for line in split:
    first = None
    last = None
    new_line = ""
    for char in line:
        number = None
        if char.isdigit():
            number = char
        else:
            new_line += char
            for digit in digits:
                if new_line.endswith(digit[0]):
                    number = str(digit[1])
        if number is not None:
            last = number
            if first is None:
                first = number
    sum += int(first + last)
print(sum)



    
        
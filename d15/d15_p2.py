def hash(string):
    value = 0    
    for char in string:
        value += ord(char)
        value *= 17
        value %= 256
    return value

focal_lengths = {}
boxes = [[] for i in range(256)]
for label in open("input.txt").read().splitlines()[0].split(","):
    if "-" in label:
        label = label[:-1]
        bucket_index = hash(label)
        if label in boxes[bucket_index]:
            boxes[bucket_index].remove(label)
    else:
        label, focal_length = label.split("=")
        focal_length = int(focal_length)        
        bucket_index = hash(label)
        if label not in boxes[bucket_index]:
            boxes[bucket_index].append(label)            
        focal_lengths[label] = focal_length
sum_p2 = 0

for i, box in enumerate(boxes):
    for slot, label in enumerate(box):
        sum_p2 += (i + 1) * (slot + 1) * focal_lengths[label]
print(sum_p2)

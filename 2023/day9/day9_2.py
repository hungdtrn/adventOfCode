from collections import defaultdict, deque
import heapq

input_path = "day9.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

ans = 0
for l in lines:
    data = to_list(l)
    is_continue = True
    first_value = []
    while is_continue:
        new_data = []
        prev = data[0]
        is_continue = False
        for d in data[1:]:
            new_data.append(d - prev)
            if new_data[-1] != 0:
                is_continue = True
            prev = d

        first_value.append(data[0])
        data = new_data
    
    for i in range(len(first_value)):
        if i % 2:
            first_value[i] = -first_value[i]
    ans += sum(first_value)

print(ans)
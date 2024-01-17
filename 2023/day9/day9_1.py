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
    last_value = []
    while is_continue:
        new_data = []
        prev = data[0]
        is_continue = False
        for d in data[1:]:
            new_data.append(d - prev)
            if new_data[-1] != 0:
                is_continue = True
            prev = d

        last_value.append(data[-1])
        data = new_data
    
    ans += sum(last_value)
print(ans)
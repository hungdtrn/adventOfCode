from collections import defaultdict, deque
import heapq

input_path = "demo.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

ans = 1
times = to_list(lines[0].replace("Time:", "").strip())
distances = to_list(lines[1].replace("Distance:", "").strip())
for i, max_time in enumerate(times):
    distance = distances[i]
    cnt = 0
    for j in range(max_time):
        if (max_time - j) * j > distance:
            cnt += 1 
            print(j, (max_time - j) * j)
    print("--")
    ans *= cnt

print(ans)

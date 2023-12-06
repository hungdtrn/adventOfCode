from collections import defaultdict, deque
import heapq
import math

input_path = "day6.txt"
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
max_time = int(lines[0].replace("Time:", "").strip().replace(" ", ""))
distance = int(lines[1].replace("Distance:", "").strip().replace(" ", ""))

min_bound = math.ceil(-math.sqrt(max_time**2 / 4 - distance) + max_time / 2)
max_bound = math.floor(math.sqrt(max_time**2 / 4 - distance) + max_time / 2)
print(max_bound - min_bound + 1, min_bound, max_bound)
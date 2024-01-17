from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day15.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    line = f.readlines()
    assert len(line) == 1
    line = line[0]


data = line.split(",")
ans = 0
for x in data:
    current_value = 0
    for c in x:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    
    ans += current_value

print(ans)
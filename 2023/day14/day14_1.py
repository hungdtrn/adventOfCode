from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "demo.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "").strip()   
        if line:     
            data.append(list(line))

lines = data
def to_list(s):
    return [int(i) for i in s.split(",") if i]



ROW, COL = len(lines), len(lines[0])
rows, cols = [], 
ans = 0
for col in range(COL):
    pos = deque([0])
    n_zeros = 0
    for row in range(ROW):
        if lines[row][col] == "#":
            pos.append(0)
        elif lines[row][col] == "O":
            pos[-1] += 1
    
    for row in range(ROW):
        if lines[row][col] == "#":
            pos.popleft()
        elif pos[0]:
            lines[row][col] = "O"
            pos[0] -= 1
        else:
            lines[row][col] = "."
    
    for row in range(ROW):
        if lines[row][col] == "O":
            ans += ROW - row


print(ans)

from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day11.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "").strip()   
        if line:     
            data.append(line)

lines = data
def to_list(s):
    return [int(i) for i in s.split(" ") if i]

symbol_graph = defaultdict(list)
ROW, COL = len(lines), len(lines[0])

offset_row = [0 for _ in range(ROW)]
offset_col = [0 for _ in range(COL)]
OFFSET = 1000000
cum_sum = 0
for col in range(COL):
    is_empty = True
    for row in range(ROW):
        if lines[row][col] == "#":
            is_empty = False
            break
    
    if is_empty:
        cum_sum += OFFSET - 1

    offset_col[col] = cum_sum
    cum_sum += 1

nodes = []
cum_sum = 0
for row in range(ROW):
    is_empty = True
    for col in range(COL):
        if lines[row][col] == "#":
            is_empty = False
            nodes.append((row, col))
    
    if is_empty:
        cum_sum += OFFSET - 1
    
    offset_row[row] = cum_sum
    cum_sum += 1


print(offset_row)
print(offset_col)

ans = 0
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        distance_row = abs(offset_row[nodes[i][0]] - offset_row[nodes[j][0]])
        distance_col = abs(offset_col[nodes[i][1]] - offset_col[nodes[j][1]])
        distance = distance_row + distance_col
        ans += distance

print(ans)
from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day10.txt"
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
print(ROW, COL)

# def check_and_add(i, j, row, col):
#     if not (0 <= row < ROW and 0 <= col < COL):
#         return
#     graph[(i, j)].add((row, col))
#     graph[(row, col)].add((i, j))

mapping = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    "S": [[1, 0], [0, 1], [0, -1], [-1, 0]],
}

graph = defaultdict(set)


for row, l in enumerate(lines):
    l = l.replace("\n", "").strip()
    if not l:
        continue
    for col, c in enumerate(l):
        if c == "S":
            nodes = [(row, col)]
        if c in mapping:
            for dir in mapping[c]:
                new_row, new_col = row + dir[0], col + dir[1]
                if ((0 <= new_row < ROW) and (0 <= new_col < COL) and lines[new_row][new_col] in mapping):
                    graph[(row, col)].add((new_row, new_col))

        
start_node = nodes.copy()
visited = defaultdict(int)
distances = 0
cnt = 0


def dfs(node, prev_node, visted):
    # print(node, distance)
    if node in visited:
        return 0

    visited[node] = True
    out = 0
    for next_node in graph[node]:
        if next_node != prev_node:
            out = max(dfs(next_node, node, visted) + 1, out)
    
    return out

visited = {}
print(dfs(start_node[0], (-1, -1), visited) // 2)
def dfs1(node, visited):
    if node in visited:
        return
    
    visited[node] = True
    for dir in [[0, 1/2], [0, -1/2], [-1/2,0], [1/2,0]]:
        new_row, new_col = node[0] + dir[0], node[1] + dir[1]
        if (0 <= new_row < ROW) and (0 <= new_col < COL):
            dfs1((new_row, new_col), visited)

for row, col in list(visited.keys()):
    if not (0 <= row < ROW and 0 <= col < COL):
        continue

    if lines[row][col] not in mapping:
        continue

    for dir in mapping[lines[row][col]]:
        new_row = row + dir[0] / 2
        new_col = col + dir[1] / 2
        if (0 <= new_row < ROW) and (0 <= new_col < COL):
            visited[(new_row, new_col)] = True

for row in range(ROW):
    dfs1((row, 0), visited)
    dfs1((row, COL - 1), visited)

for col in range(COL):
    dfs1((0, col), visited)
    dfs1((ROW - 1, col), visited)

for row in range(ROW):
    for col in range(COL):
        if (row, col) not in visited:
            ans += 1
print(ans)
# print(max(dfs(start_node[0], 0, {}).values()))
# print(max(all_distance.values()))

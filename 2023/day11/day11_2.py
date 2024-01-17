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

# while nodes:
#     new_nodes = []
#     for i in range(len(nodes)):
#         node = nodes.pop()
#         cnt += 1

#         visited[node] = distances
#         for next_node in graph[node]:
#             if next_node not in visited:
#                 new_nodes.append(next_node)
#     nodes = new_nodes
#     distances += 1

# visted = sorted(visited.items(), key=lambda x: x[1], reverse=True)
# # print(visited)
# distance = max(visited.values())
# print(max(distance, len(visited) - distance), len(visited) - distance, distance)
lefts = ["J", "7", "|"]
rights = ["L", "F", "|"]
bottoms = ["7", "F", "-"]
tops = ["L", "J", "-"]
directions = {
    "H": [[1, 0], [-1, 0]],
    "V": [[0, 1], [0, -1]],
}



labeld_graph = [["X" for col in range(COL)] for row in range(ROW)]

# def update_h(row, col, lefts, rights):
#     # print(lefts, rights)
#     if "H" in labeld_graph[row][col]:
#         return
#     if col + 1 < COL and lines[row][col + 1] in rights and lines[row][col] in lefts and ("O" in labeld_graph[row][col + 1]):
#         labeld_graph[row][col] += "H"
#     if col - 1 >= 0 and lines[row][col - 1] in lefts and lines[row][col] in rights and ("O" in labeld_graph[row][col - 1]):
#         labeld_graph[row][col] += "H"

# def update_v(row, col, tops, bottoms):
#     if "V" in labeld_graph[row][col]:
#         return
    
#     if (row + 1 < ROW) and (lines[row + 1][col] in bottoms) and (lines[row][col] in tops) and ("O" in labeld_graph[row + 1][col]):
#         labeld_graph[row][col] += "V"
#     if row - 1 >= 0 and lines[row - 1][col] in tops and lines[row][col] in bottoms and ("O" in labeld_graph[row - 1][col]):
#         labeld_graph[row][col] += "V"


# print(labeld_graph)
def label_loop1(row, col, visted):
    # print(node, distance)
    if (row, col) in visited:
        return

    labeld_graph[row][col] = "O"
    visited[(row, col)] = True
    for next_row, next_col in graph[(row, col)]:
        label_loop1(next_row, next_col, visted)
    
label_loop1(*start_node[0], {})


# def label_loop2(row, col, visted, lefts, rights, tops, bottoms):
#     # print(node, distance)
#     if (row, col) in visited:
#         return
    
#     visited[(row, col)] = True
#     if "H" in labeld_graph[row][col]:
#         for dir in directions["H"]:
#             new_row, new_col = row + dir[0], col + dir[1]
#             if ((0 <= new_row < ROW) and (0 <= new_col < COL)) and "O" in labeld_graph[new_row][new_col]:
#                 update_h(new_row, new_col, lefts, rights)
#                 label_loop2(new_row, new_col, visted, lefts, rights, tops, bottoms)
    
#     if "V" in labeld_graph[row][col]:
#         for dir in directions["V"]:
#             new_row, new_col = row + dir[0], col + dir[1]
#             if ((0 <= new_row < ROW) and (0 <= new_col < COL)) and "O" in labeld_graph[new_row][new_col]:
#                 update_v(new_row, new_col, tops, bottoms)
#                 label_loop2(new_row, new_col, visted, lefts, rights, tops, bottoms)
visited = {}
for row in range(ROW):
    for col in range(1, COL):
        if "O" in labeld_graph[row][col]:
            if col - 1 >= 0 and lines[row][col - 1] in lefts and lines[row][col] in rights:
                labeld_graph[row][col] += "H"

            if lines[row][col] in lefts and col + 1 < COL and "O" not in labeld_graph[row][col + 1] and "H" not in labeld_graph[row][col]:
                labeld_graph[row][col] += "H"

            if lines[row][col] in rights and COL - 1 >= 0 and "O" not in labeld_graph[row][col - 1] and "H" not in labeld_graph[row][col]:
                labeld_graph[row][col] += "H"

for row in range(1, ROW):
    for col in range(COL):
        if "O" in labeld_graph[row][col]:
            if row - 1 >= 0 and lines[row - 1][col] in tops and lines[row][col] in bottoms:
                labeld_graph[row][col] += "V"



def print_graph():
    for row in range(ROW):
        for col in range(COL):
            print(labeld_graph[row][col], end="\t")
        print("\n")

print_graph()
print("---")
# def graph_loop
def dfs(row, col, visited):    
    if (row, col) in visited or labeld_graph[row][col] == "O" or labeld_graph[row][col] == "B":
        return

    visited[(row, col)] = True
    if labeld_graph[row][col] == "X":
        labeld_graph[row][col] = "HV"

    labeld_graph[row][col] += "=="
    print_graph()
    print("---")
    labeld_graph[row][col] = labeld_graph[row][col].replace("==", "")
    input()
        
    for k in directions.keys():
        if k in labeld_graph[row][col]:
            # print(row, col, k, labeld_graph[row][col])
            for dir in directions[k]:
                new_row, new_col = row + dir[0], col + dir[1]
                if ((0 <= new_row < ROW) and (0 <= new_col < COL)) and (not "O" in labeld_graph[new_row][new_col] or k in labeld_graph[new_row][new_col]):
                    dfs(new_row, new_col, visited)

visited = {}
for i in range(ROW):
    dfs(i, 0, visited)
    dfs(i, COL - 1, visited)

for j in range(COL):
    dfs(0, j, visited)
    dfs(ROW - 1, j, visited)

ans = 0
for row in range(ROW):
    for col in range(COL):
        if labeld_graph[row][col] == "X":
            ans += 1
print_graph()
print(ans)
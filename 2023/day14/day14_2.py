from collections import defaultdict, deque
import heapq
import sys
import math
sys.setrecursionlimit(100000)

input_path = "day14.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "").strip()   
        if line:     
            data.append(list(line))

def to_list(s):
    return [int(i) for i in s.split(",") if i]

def move_north(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    for col in range(COL):
        pos = deque([0])
        for row in range(ROW):
            if matrix[row][col] == "#":
                pos.append(0)
            elif matrix[row][col] == "O":
                pos[-1] += 1
        
        for row in range(ROW):
            if matrix[row][col] == "#":
                pos.popleft()
            elif pos[0]:
                matrix[row][col] = "O"
                pos[0] -= 1
            else:
                matrix[row][col] = "."
    return matrix

def move_south(matrix):
    ROW, COL = len(matrix), len(matrix[0])

    for col in range(COL):
        pos = deque([0])
        for row in range(ROW-1, -1, -1):
            if matrix[row][col] == "#":
                pos.append(0)
            elif matrix[row][col] == "O":
                pos[-1] += 1
        
        for row in range(ROW-1, -1, -1):
            if matrix[row][col] == "#":
                pos.popleft()
            elif pos[0]:
                matrix[row][col] = "O"
                pos[0] -= 1
            else:
                matrix[row][col] = "."
    return matrix

def move_west(matrix):
    ROW, COL = len(matrix), len(matrix[0])

    for row in range(ROW):
        pos = deque([0])
        for col in range(COL):
            if matrix[row][col] == "#":
                pos.append(0)
            elif matrix[row][col] == "O":
                pos[-1] += 1
        
        for col in range(COL):
            if matrix[row][col] == "#":
                pos.popleft()
            elif pos[0]:
                matrix[row][col] = "O"
                pos[0] -= 1
            else:
                matrix[row][col] = "."
    return matrix

def move_east(matrix):
    ROW, COL = len(matrix), len(matrix[0])

    for row in range(ROW):
        pos = deque([0])
        for col in range(COL-1, -1, -1):
            if matrix[row][col] == "#":
                pos.append(0)
            elif matrix[row][col] == "O":
                pos[-1] += 1
        
        for col in range(COL-1, -1, -1):
            if matrix[row][col] == "#":
                pos.popleft()
            elif pos[0]:
                matrix[row][col] = "O"
                pos[0] -= 1
            else:
                matrix[row][col] = "."
    return matrix


def move(matrix):
    matrix = move_north(matrix)
    matrix = move_west(matrix)
    matrix = move_south(matrix)
    matrix = move_east(matrix)
    return matrix

def to_str(matrix):
    
    ans = ""
    for line in matrix:
        ans += "".join(line) + "\n"
    return ans

def to_matrix(str_graph):
    return [list(line) for line in str_graph.split("\n") if line]

def cnt(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    print(ROW, COL)
    ans = 0
    for col in range(COL):
        for row in range(ROW):
            if matrix[row][col] == "O":
                ans += ROW - row
    return ans

def print_graph(matrix):
    for line in matrix:
        print("".join(line))
    print()

visited = {}
start = None
for i in range(1000000000):
    move(data)
    matrix_str = to_str(data)
    if matrix_str in visited:
        start = visited[matrix_str]
        break

    visited[matrix_str] = i

repeated_pattern = list(visited.keys())[start:]
target_index = (1000000000 - (start + 1)) % len(repeated_pattern)

print(cnt(to_matrix(repeated_pattern[target_index])))


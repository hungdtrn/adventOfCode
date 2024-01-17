from collections import deque
import sys
sys.setrecursionlimit(100000)

input_path = "demo.txt"
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "").strip()   
        if line:     
            data.append(list(line))

ROW, COL = len(data), len(data[0])
print(ROW, COL)

next_direction = {
    (0, 1): [(1, 0), (-1, 0)],
    (0, -1): [(1, 0), (-1, 0)],
    (1, 0): [(0, 1), (0, -1)],
    (-1, 0): [(0, 1), (0, -1)]
}

def recurisve(row, col, direction, distance, visited):
    if row == 0 and col == 0:
        return 0
    if not (0 <= row < ROW and 0 <= col < COL):
        return float("inf")
    
    
    if (row, col, direction, distance) in visited:
        return visited[(row, col, direction, distance)]

    print((row, col, direction, distance))
    visited[(row, col, direction, distance)] = float("inf")

    ans = float("inf")
    for next_dir in next_direction[direction]:
        next_row, next_col = row + next_dir[0], col + next_dir[1]
        ans = min(ans, recurisve(next_row, next_col, next_dir, 1, visited))

    if distance < 3:
        ans = min(ans, recurisve(row + direction[0], col + direction[1], direction, distance + 1, visited))
    
    ans += int(data[row][col])
    visited[(row, col, direction, distance)] = min(ans, visited[(row, col, direction, distance)])
    # if visited[(row, col, direction, distance)] != float("inf"):
    #     print(visited[(row, col, direction, distance)], (row, col), data[row][col])
    return visited[(row, col, direction, distance)]

ans = float("inf")
cached = {}
for direction in next_direction:
    ans = min(ans, recurisve(COL-1, ROW-1, direction, 1, cached))
print(ans)
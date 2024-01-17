from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day13.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line)

processed = [[]]
for line in data:
    if line == "\n":
        processed.append([])
    else:
        line = line.replace("\n", "").strip()
        if line:
            processed[-1].append(line)

processed = [x for x in processed if x]
data = [x for x in processed if x]

def to_list(s):
    return [int(i) for i in s.split(",") if i]

def equal_col(lines, col1, col2, ROW, COL):
        for i in range(ROW):
            if lines[i][col1] != lines[i][col2]:
                return False
        
        return True

def equal_row(lines, row1, row2, ROW, COL):
    for i in range(COL):
        if lines[row1][i] != lines[row2][i]:
            return False
    
    return True


for k, lines in enumerate(processed):
    print("----")
    ROW, COL = len(lines), len(lines[0])
    # print(ROW, COL)
    current_sum = 0
    current_length = 0
    for i in range(COL):        
        left, right = i, i + 1
        while 0 <= left < COL and  0 <= right < COL and equal_col(lines, left, right, ROW, COL):
            left -= 1
            right += 1

        # if right - left - 1 > 1:
        #     print("col",i+1, right - left - 1, left, right)

        if right - left - 1 > 1 and ((left == -1) or (right == COL)):
            current_sum = i + 1

        # if right - left - 1 > 1 and right - left - 1 >= current_length:
        #     current_length = right - left - 1
        #     current_sum = i + 1
        #     print("max col", i+1, current_length, COL, left, right)


    for i in range(ROW):
        left, right = i, i + 1
        while 0 <= left < ROW and  0 <= right < ROW and equal_row(lines, left, right, ROW, COL):
            left -= 1
            right += 1

        # if right - left - 1 > 1:
        #     print("row",i+1, right - left - 1, left, right)

        if right - left - 1 > 1 and ((left == -1) or (right == ROW)):
            current_sum = (i + 1) * 100

        # if right - left - 1 > 1 and right - left - 1 >= current_length:
        #     current_length = right - left - 1
        #     current_sum = (i + 1) * 100
        #     print("max row",i+1, current_length, ROW, left, right)
    

    ans += current_sum
print(ans)
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

def n_col_diff(lines, col1, col2, ROW, COL):
        cnt = 0
        for i in range(ROW):
            if lines[i][col1] != lines[i][col2]:
                cnt += 1
        
        return cnt

def n_row_diff(lines, row1, row2, ROW, COL):
    cnt = 0
    for i in range(COL):
        if lines[row1][i] != lines[row2][i]:
            cnt += 1
    
    return cnt


for k, lines in enumerate(processed):
    print("----")
    ROW, COL = len(lines), len(lines[0])
    # print(ROW, COL)
    current_sum = 0
    current_length = 0
    for i in range(COL - 1):        
        left, right = i, i + 1
        offset = 1
        n_diff = n_col_diff(lines, left, right, ROW, COL)
        while 0 <= left < COL and  0 <= right < COL and (n_diff - offset == 0 or n_diff == 0):
            if n_diff and offset:
                offset -= 1
            left -= 1
            right += 1

            if 0 <= left < COL and  0 <= right < COL:
                n_diff = n_col_diff(lines, left, right, ROW, COL)

        if right - left - 1 > 1 and ((left == -1) or (right == COL)) and not offset:
            print("col", i, right - left - 1, left, right)
            current_sum = i + 1

        # if right - left - 1 > 1 and right - left - 1 >= current_length:
        #     current_length = right - left - 1
        #     current_sum = i + 1
        #     print("max col", i+1, current_length, COL, left, right)

    for i in range(ROW - 1):
        left, right = i, i + 1
        offset = 1
        n_diff = n_row_diff(lines, left, right, ROW, COL)

        while 0 <= left < ROW and  0 <= right < ROW and (n_diff - offset == 0 or n_diff == 0):
            if n_diff and offset:
                offset -= 1
            
            left -= 1
            right += 1

            if 0 <= left < ROW and  0 <= right < ROW:
                n_diff = n_row_diff(lines, left, right, ROW, COL)

        # if right - left - 1 > 1:
        #     print("row",i+1, right - left - 1, left, right)

        if right - left - 1 > 1 and ((left == -1) or (right == ROW)) and not offset:
            print("row", i, right - left - 1, left, right)
            current_sum = (i + 1) * 100
            break

        # if right - left - 1 > 1 and right - left - 1 >= current_length:
        #     current_length = right - left - 1
        #     current_sum = (i + 1) * 100
        #     print("max row",i+1, current_length, ROW, left, right)
    


    ans += current_sum
print(ans)
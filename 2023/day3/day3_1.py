from collections import defaultdict
input_path = "day3.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        data.append(line)

ROW, COL = len(data), len(data[0])
ans = 0

def is_adjacent(pos_list):
    for row, col in pos_list:
        for direction in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
            new_row, new_col = row + direction[0], col + direction[1]
            if (0 <= new_row < ROW) and (0 <= new_col < COL):
                if not(data[new_row][new_col] == "." or data[new_row][new_col].isdigit()):
                    return True

    return False

for row in range(ROW):
    current_num = 0
    pos_list = []
    for col in range(COL):
        if data[row][col].isdigit():
            pos_list.append((row, col))
            current_num = current_num * 10 + int(data[row][col])
        else:
            if is_adjacent(pos_list):
                ans += current_num
            else:
                print(current_num)
            current_num = 0
            pos_list = []

        
    if data[row][-1].isdigit() and is_adjacent(pos_list):
        ans += current_num


print(ans)
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

gears = {}
def aterisks(pos_list):
    pos = []
    for row, col in pos_list:
        for direction in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
            new_row, new_col = row + direction[0], col + direction[1]
            if (0 <= new_row < ROW) and (0 <= new_col < COL):
                if data[new_row][new_col] == "*":
                    pos.append((new_row, new_col))

    return set(pos)

for row in range(ROW):
    current_num = 0
    pos_list = []
    for col in range(COL):
        if data[row][col].isdigit():
            pos_list.append((row, col))
            current_num = current_num * 10 + int(data[row][col])
        elif current_num:
            potential = aterisks(pos_list)
            for p in potential:
                if p not in gears:
                    gears[p] = []
                gears[p].append(current_num)
            current_num = 0
            pos_list = []

        
    if data[row][-1].isdigit() and aterisks(pos_list):
        potential = aterisks(pos_list)
        for p in potential:
            if p not in gears:
                gears[p] = []
            gears[p].append(current_num)

ans = 0
for k, v in gears.items():
    if len(v) > 1:
        assert len(v) == 2
        ans += v[0] * v[1]

print(ans)

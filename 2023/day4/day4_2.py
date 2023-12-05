from collections import defaultdict
input_path = "day4.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

ans = 0
remain = [1 for _ in range(len(data))]
for i, l in enumerate(data):
    card, data = l.split(":")
    win_number_str, hand_str = data.strip().split("|")
    win_nubmer_list = set(to_list(win_number_str))
    hand_list = to_list(hand_str)
    current_scores = 0
    cnt = 0
    for h in hand_list:
        if h in win_nubmer_list:
            cnt += 1

    for j in range(1, cnt+1):
        remain[i+j] += remain[i]

print(sum(remain))
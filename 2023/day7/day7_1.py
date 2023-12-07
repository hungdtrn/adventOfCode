from collections import defaultdict, deque
import heapq

input_path = "day7.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

ranks = {
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: [],
    0: [],
}
cards = "23456789TJQKA"

def get_rank(card):
    cnt = {}
    for c in card:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1
    
    if len(cnt) == 1:
        return 6
    elif len(cnt) == 2:
        max_cnt = max(cnt.values())
        if max_cnt == 4:
            return 5
        else:
            return 4
    elif len(cnt) == 3:
        max_cnt = max(cnt.values())
        if max_cnt == 3:
            return 3
        else:
            return 2
    elif len(cnt) == 4:
        return 1
    else:
        return 0

def transform(card):
    out = []
    for c in card:
        out.append(cards.index(c))
    return out

for i, l in enumerate(lines):
    if not l.strip():
        continue
    print(l, i)
    card, score = l.strip().split(" ")
    ranks[get_rank(card)].append((transform(card), int(score)))

current_rank = 1
ans = 0
for i in range(7):
    if ranks[i]:
        for _, score in sorted(ranks[i], key=lambda x: x[0]):
            ans += current_rank * score
            current_rank += 1

print(ans)
# print(ranks)
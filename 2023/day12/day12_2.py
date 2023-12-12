from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day12.txt"
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
    return [int(i) for i in s.split(",") if i]

def equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def recursive(line, i, current_cnt, targets, cached):
    # print(i, line, current_cnt, targets)
    if i == len(line) and equal(current_cnt, targets):
        return 1
    elif i == len(line):
        return 0
    
    if i and (i, tuple(current_cnt), "".join(line[i-1:i+1])) in cached:
        return cached[(i, tuple(current_cnt), "".join(line[i-1:i+1]))]
    
    if line[i] == "#":
        if i == 0 or (i > 0 and line[i-1] == "."):
            current_cnt.append(0)
        current_cnt[-1] += 1
        if len(current_cnt) > len(target) or current_cnt[-1] > targets[len(current_cnt) - 1]:
            return 0
        
        out = recursive(line, i+1, current_cnt, targets, cached)
    elif line[i] == ".":
        if len(current_cnt) > len(targets):
            return 0
        for j, cnt in enumerate(current_cnt):
            if cnt != targets[j]:
                return 0
        out = recursive(line, i+1, current_cnt, targets, cached)
    else:
        out = 0
        line[i] = "#"
        out1 = recursive(line, i, current_cnt.copy(), targets, cached)
        cached[(i, tuple(current_cnt), "".join(line[i-1:i+1]))] = out1

        line[i] = "."
        out2 = recursive(line, i, current_cnt.copy(), targets, cached)

        cached[(i, tuple(current_cnt), "".join(line[i-1:i+1]))] = out2
        line[i] = "?"

        out = out1 + out2

    return out
                
ans = 0
for l in data:
    l, target = l.split(" ")
    l = (l+"?")*5
    l = l[:-1]
    target = to_list(target)
    target = target * 5
    # print(l, target)
    # print(recursive(list(l), 0, [], target, {}))
    ans += recursive(list(l), 0, [], target, {})
print(ans)

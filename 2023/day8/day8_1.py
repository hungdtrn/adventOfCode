from collections import defaultdict, deque
import heapq

input_path = "demo.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

raw_instructions = data[0]
graph_data = data[2:]

graph = {}
for line in graph_data:
    line = line.strip()
    src, dst_tuple = line.split("=")
    left,right = dst_tuple.replace("(" , "").replace(")", "").split(",")
    graph[src.strip()] = {
        "L": left.strip(),
        "R": right.strip()
    }

instructions = raw_instructions
while True:
    start = "AAA"
    cnt = 0
    for d in instructions:
        start = graph[start][d]
        cnt += 1
        if start == "ZZZ":
            print(cnt)
            exit(0)
    
    instructions = instructions + raw_instructions

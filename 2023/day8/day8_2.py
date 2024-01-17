from collections import defaultdict, deque
import heapq
from math import lcm

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
starting_nodes = [k for k in graph.keys() if k[-1] == "A"]
starting_nodes = starting_nodes
def is_stop(start_arr):
    is_stop =  True
    for n in start_arr:
        if n[-1] != "Z":
            is_stop = False
            break 

    return is_stop

stop_node = []
for node in starting_nodes:
    is_stop = False
    while not is_stop:
        start = node
        cnt = 0
        for d in instructions:
            start = graph[start][d]
            cnt += 1
            if start[-1] == "Z":
                print(cnt)
                is_stop = True  
                break      
        instructions = instructions + raw_instructions
    stop_node.append(cnt)

print(stop_node)

print(lcm(*stop_node))
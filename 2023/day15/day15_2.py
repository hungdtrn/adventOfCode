from collections import defaultdict, deque
import heapq
import sys
sys.setrecursionlimit(100000)

input_path = "day15.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    line = f.readlines()
    assert len(line) == 1
    line = line[0]


data = line.split(",")
ans = 0

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

boxes_head = [Node() for _ in range(256)]
boxes = [x for x in boxes_head]

def print_box(idx):
    current_node = boxes_head[idx].next
    while current_node:
        print(current_node.value, end=" ")
        current_node = current_node.next
    print()

cached = {
}

verbose = False
for x in data:
    current_value = 0
    index = None
    label = None
    slot = ""
    for i, c in enumerate(x):
        if c in "=-":
            label = c
            if label == "=":
                index = int(x[i+1:])
            break
        slot += c
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256

    verbose = slot == "nck" or current_value == 236
    if label == "=":
        if slot in cached:
            cached[slot].value = index
        else:
            if verbose:
                print("adding", current_value, index, x)
                print_box(current_value)
            current_node = Node(index)
            boxes[current_value].next = current_node
            current_node.prev = boxes[current_value]
            boxes[current_value] = boxes[current_value].next
            cached[slot] = current_node

            if verbose:
                print_box(current_value)
    
    elif label == "-":
        if slot in cached:
            if verbose:
                print("deleting", current_value, x)
                print_box(current_value)
            if cached[slot].next:
                cached[slot].next.prev = cached[slot].prev
            else:
                boxes[current_value] = boxes[current_value].prev
                
            cached[slot].prev.next = cached[slot].next
            cached.pop(slot)

            if verbose:
                print_box(current_value)

ans = 0
for i, head in enumerate(boxes_head):
    current_node = head.next
    current_value = 0
    j = 0
    while current_node:
        current_value += (i + 1) * (j + 1) * current_node.value
        print(i+1, j+1, current_node.value)
        j += 1
        current_node = current_node.next
    ans += current_value
    # print(current_value, i, j)
print(ans)
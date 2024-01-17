import os
import sys
import heapq

print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import read_line

input_path = "day1.txt"

current_calories = 0
max_calories = 0
min_heap = []
for line in read_line(input_path):
    print 
    if not line:
        heapq.heappush(min_heap, current_calories)
        if len(min_heap) > 3:
            heapq.heappop(min_heap)
        current_calories = 0
    else:
        current_calories += int(line)

print(sum(min_heap))
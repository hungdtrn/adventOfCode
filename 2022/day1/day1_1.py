import os
import sys

print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import read_line

input_path = "day1.txt"

current_calories = 0
max_calories = 0
for line in read_line(input_path):
    if not line:
        max_calories = max(max_calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

print(max_calories)
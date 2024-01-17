import os
import sys

print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import read_line

mapping1 = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
    "rock": "X",
    "paper": "Y",
    "scissors": "Z",
}

mapping2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "rock": "A",
    "paper": "B",
    "scissors": "C",
}

compare = {
    "rock rock": "draw",
    "rock paper": "lose",
    "rock scissors": "win",
    "paper rock": "win",
    "paper paper": "draw",
    "paper scissors": "lose",
    "scissors rock": "lose",
    "scissors paper": "win",
    "scissors scissors": "draw",
}


score_match = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

score_hand = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}



input_path = "day2.txt"
total_score = 0
for line in read_line(input_path):
    if not line:
        continue

    total_score += score_match[compare[mapping1[line[-1]] + " " + mapping2[line[0]]]] + score_hand[mapping1[line[-1]]]
    
print(total_score)    


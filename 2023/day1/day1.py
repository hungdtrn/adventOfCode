digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
input_path = "day1.txt"
total = 0
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        left = 0
        numbers = []
        for left in range(len(line)):
            if line[left].isdigit():
                numbers.append(line[left])
            
        total += int(numbers[0] + numbers[-1])

print(total)


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
input_path = "day1.txt"

total = 0
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        left = 0
        numbers = []
        for left in range(len(line)):
            if line[left].isdigit():
                numbers.append(line[left])
            else:
                num_str = line[left]
                for right in range(left+1, min(left + 5, len(line))):
                    num_str += line[right]
                    if num_str in digits:
                        numbers.append(digits[num_str])

        total += int(int(numbers[0] + numbers[-1]))

print(total)
"""
Day 2 - advent of code 2024
"""

import os

# set dir to file dir
os.chdir(os.path.dirname(__file__))
TEST_FILE = "test.txt"
DATA_FILE = "data.txt"
filename = DATA_FILE 
with open(filename) as f:
    data = f.read().splitlines()

split_lines = [line.split(' ') for line in data]

LIMIT = 3
count = 0

def check_line(line): 

    asscending = None

    for i, item in enumerate(line[1:]):
        current = int(item)
        previous = int(line[i])

        c_gt = (current >= previous)
        if current == previous:
            return False, i         

        if abs(current - previous) > LIMIT:
            return False, i 
        if asscending is None:
            asscending = c_gt 
            continue

        if asscending != c_gt:
            return False, i

    return True, None

for line in split_lines:
    print(count)
    result, idx = check_line(line)
    print(result, line)
    if result:
        count += 1
        continue

    for i in range(2):
        _line = line.copy()
        del _line[idx + i]
        result, _ = check_line(_line)
        print(result, _line)
        if result:
            count += 1
            break

print([len(l) for l in split_lines])
print(count)

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

split_lines = [line.split(" ") for line in data]

LIMIT = 3
count = 0


def check_line(line):

    direction = None

    for i, item in enumerate(line[1:]):
        current = int(item)
        previous = int(line[i])

        if current == previous:
            return False

        if abs(current - previous) > LIMIT:
            return False

        is_accending = current > previous

        if direction is None:
            direction = is_accending
            continue

        if is_accending != direction:
            return False

    return True


for line in split_lines:
    print("-" * 20)
    result = check_line(line)
    print(result, line)
    if result:
        count += 1
        continue

    for i in range(len(line)):
        _line = line.copy()
        del _line[i]
        result = check_line(_line)
        print(result, _line)
        if result:
            count += 1
            break

print(count)

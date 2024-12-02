"""
Day 2 - advent of code 2024
"""

import os

# set dir to file dir
os.chdir(os.path.dirname(__file__))
TEST_FILE = "test.txt"
DATA_FILE = "data.txt"
filename = TEST_FILE 
with open(filename) as f:
    data = f.read().splitlines()

split_lines = [line.split(' ') for line in data]

for line in split_line:
    max = 0
    for i, item in enumerate(line):
        if i == len(len):
            break
        current_ = int(item)
        next_ = int(line[i])

        diff = abs(current_ - next_)
        if diff > max:
            max = diff


    if max <= 3:
        valid = True



"""
word search for the word XMAS

can be forward and backwards

can be horizonal, vertical, or diagnoal

words ca overlap

pt 1 answer requires the number of instances of the word XMAS.


Solution:
    - load data as an 2d array
    - start loc 0,0
    - if loc == X loop surronding spaces/directions
    - when checking surround rule:
        1. set direction i.e. forward horizontal; inc x value
        2. check loc + len(XMAS) falls inside of array.
        3. for each letter in word take a step in direction
            if letter do not match check next direction
        4. if all letters found inc counter
    - loop over cols and lines.
"""

import os
from itertools import product

import numpy as np

# set dir to file dir
os.chdir(os.path.dirname(__file__))
TEST_FILE = "test.txt"
DATA_FILE = "data.txt"
filename = DATA_FILE
data = []
with open(filename) as f:
    for line in f.readlines():
        line = line.strip()
        data.append(list(line))

print(data)
data = np.array(data)
print(data[0])
print(data.shape)
data_y, data_x = data.shape
XMAS = "XMAS"

# starting loc
x = 0
y = 0

count = 0

dir_index = [-1, 0, 1]


def check_direction_for_word(direction, root_loc):
    print(f"{root_loc=}")
    direction = np.array(direction)
    print(f"{direction=}")
    for i, letter in enumerate(XMAS):
        update_dir = direction * (i)
        update_loc = root_loc + update_dir
        _x, _y = update_loc
        if (_x < 0) or (_y < 0) or (_x >= data_x) or (_y >= data_y):
            return False
        if data[_y][_x] != letter:
            print(f"{data[_y][_x]=} != {letter}")
            return False
        print(letter, _x, _y)
    return True


while y < data_y:
    print(f"main loop {x=}. {y=}")
    # move to next row if x outside of range
    if x >= data_x:
        x = 0
        y += 1
        continue

    root_loc = np.array([y, x])

    # check surround
    dir_comb = product(dir_index, dir_index)
    for direction in dir_comb:
        results = check_direction_for_word(direction, root_loc)

        if results:
            count += 1
    x += 1
print(count)

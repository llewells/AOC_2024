
import os

# regex
import re

# set dir to file dir
os.chdir(os.path.dirname(__file__))
TEST_FILE = "test.txt"
DATA_FILE = "data.txt"
filename = DATA_FILE 
with open(filename) as f:
    data = f.read()

split_lines = [line.split(' ') for line in data]

g = re.compile(r"mul\((\d{1,3},\d+)\)|(do\(\))|(don't\(\))")
res = g.findall(data)

flag = True
ans = 0
for pair in res:
    v, do, dont = pair
    if do:
        flag = True
        continue
    if dont:
        flag = False
        continue
    if flag:
        a, b = v.split(',')
        ans += int(a) * int(b)

print(ans)

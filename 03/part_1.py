import re

with open("puzzle_input.txt", 'r') as f:
    mull = f.read()

muls = re.findall(r"mul\(\d+,\d+\)", mull)

mulsum = sum([int(a)*int(b) for (a,b) in (i.replace("mul", "").replace("(", "").replace(")","").split(",") for i in muls)])
print(mulsum)



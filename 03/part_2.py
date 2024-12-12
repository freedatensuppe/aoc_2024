import re

d = "do()" + open("puzzle_input.txt").read().replace('\n',' ') + "don't()"

mull = re.sub(r"don't\(\).+?do\(\)", "", mull, flags=re.DOTALL)

muls = re.findall(r"mul\(\d*,\d*\)", mull)

mulsum = sum([int(a)*int(b) for (a,b) in (i.replace("mul", "").replace("(", "").replace(")","").split(",") for i in muls)])
print(mulsum)






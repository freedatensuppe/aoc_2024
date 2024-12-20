from functools import cache

@cache
def rec(string, patterns,score):
    if not string:
        return 1
    f = 0
    for p in patterns.split(","):
        if string.startswith(p):
            f += rec(string[len(p):], patterns,score)
    return f


with open("puzzle_input.txt", 'r') as f:
     patterns,designs = f.read().split('\n\n')

patterns = patterns.replace(",", "").split()
designs = designs.split()

possible = []
score = 0

for d in designs:
    score += rec(d,",".join(patterns),0)

print(score)

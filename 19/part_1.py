from functools import cache

@cache
def rec(string, patterns):
    if not string:
        return True
    f = False
    for p in patterns.split(","):
        if string.startswith(p):
            f = f or rec(string[len(p):], patterns)
    return f


with open("puzzle_input.txt", 'r') as f:
     patterns,designs = f.read().split('\n\n')

patterns = patterns.replace(",", "").split()
designs = designs.split()

possible = []

for d in designs:
    if rec(d,",".join(patterns)):
        possible.append(d)

print(len(designs))
print(len(possible))

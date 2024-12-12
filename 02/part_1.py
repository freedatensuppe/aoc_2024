from itertools import pairwise

reports = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        tups = list(pairwise(line.split()))
        reports.append(tups)

print(reports)

def check_if_safe(report):
    rep = [int(a)-int(b) for a,b in report]
    print(rep)
    for r in rep: 
        if abs(r) > 3 or r == 0: return 0 
    if all(i > 0 for i in rep) or all(i < 0 for i in rep): return 1
    else: return 0

r_save = [check_if_safe(r) for r in reports]
print(r_save)
print(sum(r_save))

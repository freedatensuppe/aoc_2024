from itertools import pairwise

reports = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        reports.append(line.split())

print(reports)

def check_if_safe(report):
    rep = [int(a)-int(b) for a,b in report]
    for r in rep: 
        if abs(r) > 3 or r == 0: return 0 
    if all(i > 0 for i in rep) or all(i < 0 for i in rep): return 1
    else: return 0

def check_mod_report(report):
    if check_if_safe(list(pairwise(report))) == 1: return 1
    rm_safe = []
    print(report)
    for i,_ in enumerate(report):
        rmod = report.copy()
        rmod.remove(rmod[i])
        print(i,rmod)
        rmod = list(pairwise(rmod))
        rm_safe.append(check_if_safe(rmod))
    print(rm_safe)
    if any(i > 0 for i in rm_safe): return 1
    else: return 0



r_safe = [check_mod_report(r) for r in reports]
#r_safe = [check_if_safe(r) for r in reports]
print(sum(r_safe))

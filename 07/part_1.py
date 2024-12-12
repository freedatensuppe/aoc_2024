from itertools import product, zip_longest

eqs = []
values = []
numbers = []
vsum = 0

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        v,n = line.split(":")
        values.append(v)
        numbers.append(n.split())
        
def eval_ewise(l,o):
    s = 0
    f = [l[0]]
    for i,j in zip(o,l[1:]):
        f = f + [i + j]
        f = [str(eval("".join(f)))]
    s = int(f[0])
    return s

for v,n in zip(values,numbers):
    obin = list(product(range(2), repeat=len(n)-1))
    for o in obin:
        opm = ["+" if i == 0 else "*" for i in o]
#        nsumlist = [str(x) for y in list(zip_longest(n, opm)) for x in y if x is not None]
        if int(v) == eval_ewise(n,opm):
            vsum += int(v)
            break

print(vsum)

    






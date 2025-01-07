
with open("puzzle_input.txt", 'r') as f:
     xybits,cbits = f.read().strip().split('\n\n')

xybits = {k: v for k,v in [a.split() for a in xybits.replace(":", "").split("\n")]}
cbits = {k: v for v,k in [a.split(" -> ") for a in cbits.replace(" OR ", " | ").replace(" XOR ", " ^ ").replace(" AND ", " & ").split("\n")]}

xybits_full = len(xybits) + len(cbits)

print(xybits)
print(cbits)

while True:
    for k,v in cbits.items(): 
        a,o,b = v.split()
        if a in xybits.keys() and b in xybits.keys():
            xybits[k] = str(eval(xybits[a] + o + xybits[b]))
    if len(xybits) == xybits_full:
        break

zlist = [(k,v) for (k,v) in sorted(xybits.items()) if k.startswith("z")][::-1]
print(zlist)
print(int("".join([z[1] for z in zlist]), 2))



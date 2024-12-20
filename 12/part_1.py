regions_map = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word =  []
        for w in line.rstrip():
            word.append(w)
        regions_map.append(word)

cols = len(regions_map[0])
rows = len(regions_map)

for r in regions_map:
    print(r)

dirs = [(0,1), (-1, 0), (1, 0), (0,-1)]

regions = []

def take_step(regions_map, r, c, reg):
    if (r,c) in reg: return
    reg.add((r,c))
    for d in dirs:
        rn = r + d[0]
        cn = c + d[1]
        if cn >= cols or cn < 0 or rn >= rows or rn < 0:
            continue
        if regions_map[r][c] == regions_map[rn][cn]:
            take_step(regions_map, rn, cn, reg)
    return reg

for j in range(rows):
    for i in range(cols):
        if (j,i) in [r for r in regions]: continue
        reg = set()
        regions.append(take_step(regions_map, j, i, reg))

regions_uniq = []

for r in regions:
    if r in regions_uniq:
        continue
    regions_uniq.append(r)
    print(len(r), r)

peris = []

for ru in regions_uniq:
    p = 0
    for (r,c) in ru:
        for d in dirs:
            rn = r + d[0]
            cn = c + d[1]
            if cn >= cols or cn < 0 or rn >= rows or rn < 0 or regions_map[r][c] != regions_map[rn][cn]:
               p += 1 
    peris.append(p)

price = 0

for p,ru in zip(peris, regions_uniq):
    print(len(ru), p)
    price += p*len(ru)

print(price)

regions_map = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word =  []
        for w in line.rstrip():
            word.append(w)
        regions_map.append(word)

cols = len(regions_map[0])
rows = len(regions_map)

dirs = [(0,1), (0,-1), (-1, 0), (1, 0)]
rdict = {"-1": "down", "1": "up"}
cdict = {"-1": "left", "1": "right"}

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

peris = []

for ru in regions_uniq:
    p = []
    for (r,c) in ru:
        for d in dirs:
            rn = r + d[0]
            cn = c + d[1]
            if cn >= cols or cn < 0 or rn >= rows or rn < 0 or regions_map[r][c] != regions_map[rn][cn]:
                p.append((r,c,d[0],d[1]))
    peris.append(p)

corr = []

for p in peris:
    c = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            m,n = p[i], p[j]
            if (n[2] == m[2] and n[3] == m[3]) and ((n[0]==m[0] and abs(n[1]-m[1]) == 1) or (n[1]==m[1] and abs(n[0]-m[0]) == 1)):
                c += 1 
    corr.append(c)

price = 0

for i,_ in enumerate(peris):
    price += len(regions_uniq[i]) * (len(peris[i]) - corr[i])
    

print(price)

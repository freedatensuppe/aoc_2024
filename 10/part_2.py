
topmap = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = []
        for w in line.rstrip():
            word.append(int(w))
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

for t in topmap:
    print(t)

dirs = [(0,1), (-1,0), (1,0), (0,-1)]

zeros = []
sumlist = []

for i in range(len(topmap)):
    for j in range(len(topmap[0])):
        if topmap[i][j] == 0:
            zeros.append((i,j))

def take_step(topmap,r,c,n):
    if topmap[r][c] == 9:
       sumlist.append(1)
       return 0 
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if (cn >= cols or cn < 0 or rn < 0 or rn >= rows): continue
        if (topmap[rn][cn] == n+1):
            take_step(topmap,rn,cn,topmap[rn][cn])

for z in zeros:
    take_step(topmap, z[0], z[1], topmap[z[0]][z[1]])
    print(z,len(sumlist))

print(sum(sumlist))



topmap = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = []
        for w in line.rstrip():
            word.append(w)
        topmap.append(word)

cols = len(topmap[0])
rows = len(topmap)

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
sumlist = []
start = (0,0)

for i in range(len(topmap)):
    for j in range(len(topmap[0])):
        if topmap[i][j] == 'S':
            start = (i,j)

def take_step(topmap,r,c,cd,score):
    if topmap[r][c] == "E":
        score.add((r,c))
        return score
    for d in dirs:
        cn = c + d[1]
        rn = r + d[0]
        if (topmap[rn][cn] == '.') and (rn,cn) not in score: 
            score.add((r,c))
            print(r,c)
            take_step(topmap,rn,cn,d,score)

score = set()
take_step(topmap, start[0], start[1], dirs[0], score)
print(score)
print(len(score))

for t in topmap:
    print(t)


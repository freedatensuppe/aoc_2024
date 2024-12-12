import copy

guard_map = []
dirs = [[-1,0], [0,1], [1,0], [0,-1]]

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = ["O"]
        for w in line.rstrip():
            word.append(w)
        guard_map.append(word + ["O"])

ncols = ["O" for _ in guard_map[0]]
gmo = []
for _ in range(1): gmo.append(ncols)
for i in guard_map: gmo.append(i)
for _ in range(1): gmo.append(ncols)

def get_initial_pos(gm):
    for i in gm:
        for j in i:
            if j == '^':
                return [gm.index(i), i.index(j)]

def move_guard(g, x, y, dirs, i=0):
    count = 0
    next_block = ""
    g[x][y] = "X"
    while(g[x][y] != 'O'):
        d = dirs[i]
        next_block = ""
        g[x][y] = "X"
        while(next_block != '#'):
            x += d[0]
            y += d[1]
            if g[x][y] == "O": break
            g[x][y] = "X"
            next_block=g[x+d[0]][y+d[1]]
            count +=1
            if count > 30000: break
#        print("count:", count)
        i = (i + 1) % 4
        if count > 30000: break
    return count

obs = 0

x1, y1 = get_initial_pos(gmo)

for i,_ in enumerate(gmo):
    for j,_ in enumerate(gmo[0]):
        gmo_mod = copy.deepcopy(gmo)
        if gmo_mod[i][j] == ".":
            gmo_mod[i][j] = "#"
            c = move_guard(gmo_mod, x1, y1, dirs, i=0)
            if c > 30000:
                obs += 1

print(obs)


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

for i in gmo:
    print(i)

def get_initial_pos(gm):
    for i in gm:
        for j in i:
            if j == '^':
                return gm.index(i), i.index(j)
    
x,y = get_initial_pos(gmo)
print("initial position:", x,y)
count = 0
next_block = ""
i = 0

while(gmo[x][y] != 'O'):
    d = dirs[i]
    next_block = ""
    gmo[x][y] = "X"
    while(next_block != '#'):
        x += d[0]
        y += d[1]
        if gmo[x][y] == "O": break
        gmo[x][y] = "X"
        next_block=gmo[x+d[0]][y+d[1]]
        count +=1
    print("count:", count)
    i = (i + 1) % 4

for i in gmo:
    print(i)

count_distinct = 0

for i in gmo:
    for j in i:
        if j == "X":
            count_distinct += 1

print("count_distinct:", count_distinct)

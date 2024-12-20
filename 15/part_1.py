
with open("puzzle_input.txt", 'r') as f:
     wh,moves = f.read().split('\n\n')

dirdict = {"^": [-1, 0],
           "v": [ 1, 0],
           ">": [ 0, 1],
           "<": [ 0,-1]}

def get_initial_pos(wh):
    for i in wh:
        for j in i:
            if j == '@':
                return wh.index(i), i.index(j)

def move_blocks(wh, r, c, m):
    rn = r 
    cn = c 
    while (wh[rn][cn] != "#"):
        rn += m[0]
        cn += m[1]
        if wh[rn][cn] == ".":
            wh[rn][cn], wh[r][c] = wh[r][c], wh[rn][cn]
            return True
    return False

def move_robot(wh, r, c, m):
    rn =  r + m[0]
    cn =  c + m[1]
    if wh[rn][cn] == "#": return r, c
    if wh[rn][cn] == ".": 
        wh[rn][cn], wh[r][c] = wh[r][c], wh[rn][cn]
        return rn, cn
    if wh[rn][cn] == "O": 
        if move_blocks(wh, rn, cn, m): 
            wh[rn][cn], wh[r][c] = wh[r][c], wh[rn][cn]
            return rn,cn
    return r,c

warehouse = []

for w in wh.strip().split("\n"):
    l =[]
    for i in w:
        l.append(i)
    warehouse.append(l)


rows = len(warehouse)
rows = len(warehouse[0])

r,c = get_initial_pos(warehouse)

for m in "".join(moves.split()):
    m = dirdict[m]
    rn, cn = move_robot(warehouse, r, c, m)
    r, c = rn, cn

for w in warehouse:
    print(w)
print()

osum = 0

for i,w in enumerate(warehouse):
    for j,_ in enumerate(w):
        if warehouse[i][j] == "O":
            osum += 100 * i + j

print(osum)


    

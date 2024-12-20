
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

def get_blocks(wh,r,c,m,b):
    if (r,c) in b:
        return b
    b.add((r,c))
    rn =  r + m[0]
    cn =  c + m[1]
    if wh[r][c] == "[": 
        get_blocks(wh,r,c+1,m,b)
        if wh[rn][cn] == "#" or wh[rn][cn+1] == "#":
            print("here")
            return 
        if wh[rn][cn] == "[" or wh[rn][cn] == "]":
            get_blocks(wh,rn,cn,m,b)
        if wh[rn][cn] == "." and wh[rn][cn+1] == ".":
            b.add((r,c))
            b.add((r,c+1))
    if wh[r][c] == "]":
        get_blocks(wh,r,c-1,m,b)
        if wh[rn][cn] == "#" or wh[rn][cn-1] == "#":
            print("or here")
            return 
        if wh[rn][cn] == "[" or wh[rn][cn] == "]":
            get_blocks(wh,rn,cn,m,b)
        if wh[rn][cn] == "." and wh[rn][cn-1] == ".":
            b.add((r,c))
            b.add((r,c-1))
    return b

def move_blocks(wh, r, c, m):
    b = set()
    blocks = get_blocks(wh,r,c,m,b)
    print(blocks)
    if blocks is None:
        return False
    for b in sorted(blocks):
        if wh[b[0]+m[0]][b[1]+m[1]] == "#":
            return False
    for b in blocks:
        wh[b[0]][b[1]], wh[b[0]+m[0]][b[1]+m[1]] =  wh[b[0]+m[0]][b[1]+m[1]], wh[b[0]][b[1]]
    return True

def move_robot(wh, r, c, m):
    rn =  r + m[0]
    cn =  c + m[1]
    if wh[rn][cn] == "#": return r, c
    if wh[rn][cn] == ".": 
        wh[rn][cn], wh[r][c] = wh[r][c], wh[rn][cn]
        return rn, cn
    if wh[rn][cn] == "[" or wh[rn][cn] == "]": 
        if move_blocks(wh, rn, cn, m): 
            wh[rn][cn], wh[r][c] = wh[r][c], wh[rn][cn]
            return rn,cn
    return r,c

warehouse = []

for w in wh.strip().split("\n"):
    l =[]
    for i in w:
        if i == "#":
            l.append(i)
            l.append(i)
        if i == "O":
            l.append("[")
            l.append("]")
        if i == "@":
            l.append("@")
            l.append(".")
        if i == ".":
            l.append(i)
            l.append(i)
    warehouse.append(l)


rows = len(warehouse)
rows = len(warehouse[0])

r,c = get_initial_pos(warehouse)

for m in "".join(moves.split()):
    print(m)
    m = dirdict[m]
    for w in warehouse:
        print(*w)
    print()
    rn, cn = move_robot(warehouse, r, c, m)
    r, c = rn, cn

for w in warehouse:
    print(*w)

osum = 0

for i,w in enumerate(warehouse):
    for j,_ in enumerate(w):
        if warehouse[i][j] == "[":
            osum += 100 * i + j

print(osum)





    

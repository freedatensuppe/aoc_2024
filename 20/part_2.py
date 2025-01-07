import networkx as nx 
from copy import deepcopy
from collections import Counter

def get_grid(grid, rows, cols):
    G = nx.Graph()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                G.add_node((r,c))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "#":
                if c < cols - 1 and grid[r][c+1] != "#":
                    G.add_edge((r,c), (r,c+1))
                if r < rows - 1 and grid[r+1][c] != "#":
                    G.add_edge((r,c), (r + 1, c))
    return G

def get_pos(topmap, s):
    for i in topmap:
        for j in i:
            if j == s:
                return topmap.index(i), i.index(j)

topmap = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = []
        for w in line.rstrip():
            word.append(w)
        topmap.append(word)

rows = len(topmap)
cols = len(topmap[0])

for i in range(len(topmap)):
    for j in range(len(topmap[0])):
        if topmap[i][j] == 'S':
            start = (i,j)

G = get_grid(topmap, rows, cols) 
start = get_pos(topmap, "S")
end = get_pos(topmap, "E")
time = nx.shortest_path_length(G, start, end)
print(start, end, time)

ctimes = []
count = 0
cn = 0
print("dims", rows*cols)

for r in range(1, rows -1 ):
    for c in range(1, cols - 1):
        print(cn)
        topmapmod = deepcopy(topmap)
        if topmapmod[r][c] == "#":
            topmapmod[r][c] = "."
            G = get_grid(topmapmod, rows, cols) 
            ctime = nx.shortest_path_length(G, start, end)
            if (time - ctime) > 99:
                count += 1
        cn += 1

print(count)







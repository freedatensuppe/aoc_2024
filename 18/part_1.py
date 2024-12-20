import networkx as nx 

corrupted = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        r,c = line.strip().split(",")
        corrupted.append((int(r),int(c)))

for i in corrupted:
    print(i)

cols = 71
rows = 71


topmap = [["."]*cols for _ in range(rows)]

for i,c in enumerate(corrupted):
    if i >= 1024: break
    topmap[c[1]][c[0]] = "#"

for i in topmap:
    print(*i)

def get_grid(grid, rows, cols):
    start = (0,0)
    end = (rows - 1 ,cols -1)
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
    return G, start, end

G, start, end = get_grid(topmap, rows, cols) 
path = nx.shortest_path(G, start, end)
shortest = nx.shortest_path_length(G, start, end)

print(path)
print(shortest)

#for p in path: 
#    topmap[p[0]][p[1]] = "O"
#
#for i in topmap:
#    print(*i)







import networkx as nx 

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

corrupted = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        r,c = line.strip().split(",")
        corrupted.append((int(r),int(c)))

cols = 71
rows = 71

topmap = [["."]*cols for _ in range(rows)]

for i,c in enumerate(corrupted):
    shortest = None
    topmap[c[1]][c[0]] = "#"
    print(c)
    G, start, end = get_grid(topmap, rows, cols) 
    shortest = nx.shortest_path_length(G, start, end)







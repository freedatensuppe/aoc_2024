
with open("puzzle_input.txt", 'r') as f:
     grids = f.read().split('\n\n')

locks, keys = [], []
for grid in grids:
    grid_str = grid.replace("\n", "").replace(".", "0").replace("#", "1")
    if grid_str[0] == "1":
        locks.append(int(grid_str, 2))
    else:
        keys.append(int(grid_str, 2))


uniques = set()
for i in range(len(keys)):
    key = keys[i]

    for j in range(len(locks)):
        lock = locks[j]
        if "1" not in format(key & lock, "b"):
            uniques.add((i, j))


print(len(uniques))

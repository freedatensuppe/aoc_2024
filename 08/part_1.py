import copy

city = []
antennas = set()

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = []
        for w in line.rstrip():
            word.append(w)
        city.append(word)

rows = len(city)
cols = len(city[0])

def get_antinodes(node):
    nodes = set()
    antinodes = set()
    for i,r in enumerate(city):
        for j,c in enumerate(r):
            if c == node:
                nodes.add((i,j))
    for n in nodes:
        for m in nodes:
            dist = (n[0]-m[0], n[1]-m[1])
            if not (n[0]+dist[0] < 0 or n[0]+dist[0] >= rows or n[1]+dist[1] < 0 or  n[1]+dist[1] >= cols):
                antinodes.add((n[0]+dist[0], n[1]+dist[1]))
                continue
            if not (n[0]-dist[0] < 0 or n[0]-dist[0] >= rows or n[1]-dist[1] < 0 or  n[1]-dist[1] >= cols):
               antinodes.add((n[0]-dist[0], n[1]-dist[1]))
               continue
            if not (m[0]+dist[0] < 0 or m[0]+dist[0] >= rows or m[1]+dist[1] < 0 or  m[1]+dist[1] >= cols):
               antinodes.add((m[0]+dist[0], m[1]+dist[1]))
               continue
            if not (m[0]-dist[0] < 0 or m[0]-dist[0] >= rows or m[1]-dist[1] < 0 or  m[1]-dist[1] >= cols):
               antinodes.add((m[0]-dist[0], m[1]-dist[1]))
               continue
    return antinodes - nodes

hashcity = copy.deepcopy(city)
    
for r in city:
    for c in r:
        if c in antennas:
            continue
        if c.isalnum():
            an = get_antinodes(c)
            print(len(an))
            antennas.add(c)
            for a in an:
                hashcity[a[0]][a[1]] = "#"

count = 0

for r in hashcity:
    for c in r:
        if c == "#":
            count += 1 
print(count)

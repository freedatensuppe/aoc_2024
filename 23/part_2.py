from itertools import combinations

connections = set()
computers = set()

with open("puzzle_input.txt", 'r') as f: 
    for line in f:
        a,b = (line.strip().split("-"))
        computers.add(a)
        computers.add(b)
        connections.add((a,b))
        connections.add((b,a))


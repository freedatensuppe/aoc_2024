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

triples = { ( (a,b),(b,c),(c,a) )
           for a, b, c in combinations(computers, 3) 
           if 't' in (a + b + c)[::2] and (a,b) in connections 
                                      and (b,c) in connections
                                      and (c,a) in connections 
           }

print(len(triples))

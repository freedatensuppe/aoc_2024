
machines = []

with open("puzzle_input.txt", 'r') as f: 
    machine_data = [l.replace("+", " ").replace("=", " ").replace(",", " ").split() \
                    for l in f.read().split('\n\n')]

for m in machine_data:
    a = (int(m[3]),  int(m[5]))
    b = (int(m[9]),  int(m[11]))
    p = (int(m[14]), int(m[16]))
    machines.append([a,b,p])

tokens = []

for m in machines: 
    t = [1000]
    for i in range(1, 101):
        for j in range(1, 101):
            if  (i * m[0][0] + j * m[1][0] == m[2][0]) and \
                (i * m[0][1] + j * m[1][1] == m[2][1]):  
                t.append((3*i+j))
    tokens.append(min(t))

print(sum([t if t < 1000 else 0 for t in tokens]))




    




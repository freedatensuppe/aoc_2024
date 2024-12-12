
x = []
y = []

with open("test.txt", 'r') as f:
    for line in f:
        a,b = line.split()
        x.append(int(a))
        y.append(int(b))


sim = sum([j*y.count(j) for j in x])

print(sim)

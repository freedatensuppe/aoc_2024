
x = []
y = []

with open("test.txt", 'r') as f:
    for line in f:
        a,b = line.split()
        x.append(int(a))
        y.append(int(b))

dist = sum([abs(a-b) for a,b in zip(sorted(x), sorted(y))])
print(dist)




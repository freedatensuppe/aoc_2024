
stones = []

with open("puzzle_input.txt", 'r') as f:
    stones = list(f.read().strip().split())


for i in range(75):
    print(i)
    t = []
    for j in stones: 
        if j == "0": 
            j = "1"
            t.append(j)
            continue
        if len(j) % 2 == 0:
            a, b = j[:int(len(j)/2)], j[int(len(j)/2):]
            t.append(str(int(a)))
            t.append(str(int(b)))
            continue
        t.append(str(int(j) * 2024))
    stones = t
    
print(len(stones))

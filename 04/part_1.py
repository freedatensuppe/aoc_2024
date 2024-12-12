
xmas = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        word = ["O", "O", "O"]
        for w in line.rstrip():
            word.append(w)
        xmas.append(word + ["O", "O", "O"])

ncols = ["O" for _ in xmas[0]]
xmas_o = []

for _ in range(3): xmas_o.append(ncols)
for i in xmas: xmas_o.append(i)
for _ in range(3): xmas_o.append(ncols)

dirs = [(-1, 1), ( 0, 1), ( 1, 1),
        (-1, 0),          ( 1, 0), 
        (-1,-1), ( 0,-1), ( 1,-1),
        ]

count = 0

for i in range(len(xmas_o)):
    for j in range(len(xmas_o[0])):
        if xmas_o[i][j] == "X":
            for (k,l) in dirs:
                if xmas_o[i+k][j+l] == "M":
                    if xmas_o[i+2*k][j+2*l] == "A":
                        if xmas_o[i+3*k][j+3*l] == "S":
                            count += 1
print("Part 1:")
print(count)

mas_dirs = [(-1, 1), ( 1, 1),
            (-1,-1), ( 1,-1),
           ]

count = 0
#### part 2 ####

for i in range(len(xmas_o)):
    for j in range(len(xmas_o[0])):
        if xmas_o[i][j] == "A":
            for (k,l) in mas_dirs:
                if xmas_o[i+k][j+l] == "M":
                    if xmas_o[i-k][j-l] == "S":
                        if xmas_o[i+k][j-l] == "M" and xmas_o[i-k][j+l] == "S": count += 1
                        if xmas_o[i+k][j-l] == "S" and xmas_o[i-k][j+l] == "M": count += 1

print("Part 2:")
print(count/2)

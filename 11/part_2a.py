
stones = []

with open("puzzle_input.txt", 'r') as f:
    stones = list(f.read().strip().split())

stones_dict = {s: 1 for s in stones}

for k,v in stones_dict.items(): 
    print(k,v)


for i in range(25):
    stones_dict['1'] = stones_dict['0']
    stones_dict['0'] = 0
    for k,v in stones_dict.items(): 
        print(k,v)
        if len(str(k)) % 2 == 0:
            a, b = str(k[:int(len(k)/2)]), str(k[int(len(k)/2):])
            stones_dict[a] += 1
            stones_dict[b] += 1
            stones_dict[k] =  0
            continue
        stones_dict[k] = 0
        stones_dict[k*2024] += 1
    
print([])

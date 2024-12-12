import re

s = []
smap = []

with open("puzzle_input.txt", 'r') as f:
    diskmap = f.read().strip()

for i,n in enumerate(list(diskmap)):
    s = []
    for j in range(int(n)):
        if int(i) % 2 != 0:
            s += "."
            continue
        s.append(str(int(i/2)))
    smap.append(s)

#print("".join(["".join(i) for i in smap]))

nums = [j for j in smap if len(j) > 0 and re.match(r'[0-9]', j[0])]
nums.reverse()
dots = [j for j  in smap if len(j) > 0 and j[0] == "."]

#print((nums))
#print((dots))
nl = len(nums) 
nd = len(dots)


for ni,n in enumerate(nums):
    for di,d in enumerate(dots): 
        if di >= nl - ni: continue
        ids = [i for i, x in enumerate(d) if x == "."]
#        print(len(n), "<=", len(ids), len(n) <= len(ids))
        if len(n) > 0 and len(ids) > 0 and len(n) <= len(ids):
            for i,_ in enumerate(n): 
                d[ids[i]], n[i] = n[i], d[ids[i]]
    print("".join(["".join(i) for i in smap]))

#print("".join(["".join(i) for i in smap]))

tl = [t for t in smap for t in t]
tlsum = sum([n*int(t) for n,t in enumerate(tl) if t != "." and t != 0])
print(tlsum)


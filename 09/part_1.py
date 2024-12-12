import re

#diskmap = "67325383346463505419167727"
s = []

with open("puzzle_input.txt", 'r') as f:
    diskmap = f.read().strip()

print(diskmap)

for i,n in enumerate(list(diskmap)):
    for j in range(int(n)):
        if int(i) % 2 != 0:
            s += "."
            continue
        s.append(str(int(i/2)))


nums = [j for j, a in enumerate(s) if re.match(r'[0-9]', a)][::-1]
dots = [j for j, a in enumerate(s) if a == "."]

count = 0 

for n,d in zip(nums,dots):
    s[d], s[n] = s[n], s[d]
    k = s.index(".")
    count += 1
    if count % 100 == 0:
        print(count)
    if "".join(s[:k]).isalnum() and all(i == "." for i in s[k:]):
        tl = s[:k] 
        break

tlsum = sum([n*int(t) for n,t in enumerate(tl)])

print("".join(s))        
print(" ".join(s))        
print(tlsum)

#for n,c in enumerate(sl):
#    if sl[n] == ".":
#        i = [j for j, a in enumerate(sl) if re.match(r'[0-9]', a)]
#        sl[n], sl[i[-1]] = sl[i[-1]], "."
#    k = sl.index(".")
#    count += 1 
#    if count % 100 == 0:
#        print(count)
#    if "".join(sl[:k]).isalnum() and all(i == "." for i in sl[k:]):
#        tl = sl[:k] 
#        break
##    print("".join(sl))        
#

#
##print("".join(sl))
##print("".join(tl))        
#

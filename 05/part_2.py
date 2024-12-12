
with open("puzzle_input.txt", 'r') as f:
     rules,updates = f.read().split('\n\n')

rules = [tuple(i.split("|")) for i in rules.split("\n")]
updates = [u.split(",") for u in updates.strip().split("\n")]
mlist = []
clist = []

def check_rules(update):
    for r in rules:
        if r[0] in u and r[1] in update:
            if update.index(r[0]) < update.index(r[1]): continue
            if update.index(r[0]) > update.index(r[1]): return False
    return True

def correct(update):
    for _ in range(len(update)):
        for r in rules:
            if r[0] in u and r[1] in update:
                if update.index(r[0]) < update.index(r[1]): continue
                if update.index(r[0]) > update.index(r[1]): 
                    t = update[update.index(r[0])]
                    update[update.index(r[0])] = update[update.index(r[1])]
                    update[update.index(r[1])] = t
    return update

for u in updates:
    if check_rules(u):
        mlist.append(int(u[int(len(u)/2)]))

print(mlist)
print(sum(mlist))

for u in updates:
    if not check_rules(u):
        uc = correct(u)
        clist.append(int(u[int(len(uc)/2)]))

print(clist)
print(sum(clist))

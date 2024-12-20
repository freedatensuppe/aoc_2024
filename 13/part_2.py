
machines = []

with open("puzzle_input.txt", 'r') as f: 
    machine_data = [l.replace("+", " ").replace("=", " ").replace(",", " ").split() \
                    for l in f.read().split('\n\n')]

for m in machine_data:
    a = (int(m[3]),  int(m[5]))
    b = (int(m[9]),  int(m[11]))
    p = (int(m[14]) + 10000000000000, int(m[16]) + 10000000000000)
    machines.append([a,b,p])

tokens = []

for i in machines: 
    n = i[0][0]
    m = i[1][0] 
    p = i[2][0] 
    r = i[0][1] 
    s = i[1][1] 
    q = i[2][1]
    y = - (q*n-p*r)/(m*r-s*n)
    x = (p - y*m)/n
    print(x,y)
    if (x.is_integer() and y.is_integer() and x >= 0 and y >= 0):
        tokens.append(3*x+y)

print(sum(tokens))





    




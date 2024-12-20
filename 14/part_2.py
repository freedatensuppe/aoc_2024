
particles  = []
velocities = []
dimx = 101
dimy = 103
midx = int(dimx/2)
midy = int(dimy/2)

with open("puzzle_input.txt", 'r') as f: 
    lines = [line.strip() for line in f]

for l in lines:
    p, px, py, v, vx, vy = l.replace(",", " ").replace("=", " ").split()
    particles.append( [int(px),int(py)])
    velocities.append([int(vx),int(vy)])

bathroom = []

for j in range(dimy):
    b = []
    for i in range(dimx):
        b.append(0)
    bathroom.append(b)

min_sf = float("inf")
best = None

for i in range(2*dimx*dimy):
    be = [list(b) for b in bathroom]
    for (p,v) in zip(particles,velocities):
        p[0] = (p[0] + v[0]) % dimx
        p[1] = (p[1] + v[1]) % dimy

    for p in particles:
        be[p[1]][p[0]] += 1
    
    q1 = [q[:midx] for q in be[:midy]]
    q2 = [q[:midx] for q in be[midy+1:]]
    q3 = [q[midx+1:] for q in be[:midy]]
    q4 = [q[midx+1:] for q in be[midy+1:]]

    m = 1
    
    for q in q1,q2,q3,q4:
        s = 0
        s = sum([j for x in q for j in x])
        m *= s

    if m < min_sf:
        min_sf = m
        best = i

print(min_sf, best)
    



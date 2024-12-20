

def adv(a,b,c,o, odict): 
    if o > 3 and o < 7:
        o = int(odict[str(o)])
    a = a // (2**o)
    return a,b,c,""

def bxl(a,b,c,o,odict):
    b = b ^ o  
    return a,b,c,""

def bst(a,b,c,o,odict):
    if o > 3 and o < 7:
        o = int(odict[str(o)])
    b = o % 8
    return a,b,c,""

def jnz(a,b,c,o,odict):
    if a == 0:
        return a,b,c,""
    return a,b,c,o

def bxc(a,b,c,o,odict):
    b = b ^ c
    return a,b,c,""

def out(a,b,c,o,odict):
    if o > 3 and o < 7:
        o = int(odict[str(o)])
    o = o % 8
    return a,b,c,str(o)

def bdv(a,b,c,o,odict):
    if o > 3 and o < 7:
        o = int(odict[str(o)])
    b = a // (2**o)
    return a,b,c,""

def cdv(a,b,c,o,odict):
    if o > 3 and o < 7:
        o = int(odict[str(o)])
    c = a // (2**o)
    return a,b,c,""

def machine(instructions,a,b,c):
    i = 0
    output = []
    while(i+1 < len(instructions)):
        operanddict = {"4": a, "5": b, "6": c}
        instr = instructions[i]
        fun = fundict[str(instr)]
        operand = instructions[i+1]
        a,b,c,op = fun(a,b,c,operand, operanddict)
        if isinstance(op, str):
            if op != "":
                output.append(op)
        if isinstance(op, int):
            i = op
            continue
        i += 2
    return output

with open("puzzle_input.txt", 'r') as f:
     registers,program = f.read().split('\n\n')

a,b,c = [int(r.split()[-1]) for r in registers.strip().split("\n")]
instructions = [int(p) for p in program.split()[1] if p.isalnum()]
backint = [str(i) for i in instructions[::-1]]
fundict = {"0": adv, "1": bxl,  "2": bst,  "3": jnz,  "4": bxc,  "5": out,  "6": bdv,  "7": cdv}

print("A,B,C: ",a,b,c)
print("Instructions: ", [i for i in instructions])

def find_a(a=0, depth=0):
    if depth == len(backint):
        return a
    for i in range(8):
        output = machine(instructions, a*8 + i, 0, 0)
        if output[0] == backint[depth]:
            if result := find_a((a*8 + i), depth+1): 
                return result
    return 0

print("Part 2:", find_a())

from functools import cache
import sys

sys.setrecursionlimit(2005)

numbers = []

with open("puzzle_input.txt", 'r') as f:
    for line in f:
        numbers.append(int(line))

@cache
def get_secret_number(n, depth):
    if depth == 0:
        return n
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ ((n // 32))) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    return get_secret_number(n, depth - 1)

secret_numbers = []
depth = 2000
get_secret_number(123,10)

for n in numbers:
    secret_numbers.append(get_secret_number(n,depth))

print(secret_numbers)
print(sum(secret_numbers))







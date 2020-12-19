import sys

file_name = sys.argv[1]

lines = []
with open(file_name, 'r') as file:
    lines = [int(line.rstrip()) for line in file]

def solve():
    pass

result = solve()

print(f'{result}')

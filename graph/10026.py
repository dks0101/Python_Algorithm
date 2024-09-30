import sys
grid = []
n = int(sys.stdin.readline())
for i in range(n):
    row = sys.stdin.readline().strip()
    grid.append(list(row))
for row in grid:
    print(''.join(row))


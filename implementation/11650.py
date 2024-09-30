import sys

n = int(sys.stdin.readline())
list_x = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list_x.append([a, b])
list_x.sort()

for i in list_x:
    print(i[0], i[1])

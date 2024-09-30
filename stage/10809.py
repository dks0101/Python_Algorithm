s = list(input())
find = 'abcdefghijklmnopqrstuvwxyz'

cnt = []
for i in find:
    if i in s:
        print(s.index(i), end= ' ')
    else:
        print(-1, end=' ')
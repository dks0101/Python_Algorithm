import sys
input = sys.stdin.readline

n = int(input())
sta = []
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        sta.append(a[1])
        print(sta)
    elif a[0] == 2:
        if len(sta) != 0:
            print(sta.pop())
            print(sta)
        else:
            print(-1)
    elif a[0] == 3:
        print(len(sta))
    elif a[0] == 4:
        if len(sta) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 5:
        if len(sta) != 0:
            print(sta[-1])
        else:
            print(-1)
n, k = map(int, input().split())
cnt = 0
list = []
for i in range(n):
    a = int(input())
    list.append(a)
list.sort(reverse=True)
for coin in list:
    cnt += k//coin
    k %= coin
print(cnt)

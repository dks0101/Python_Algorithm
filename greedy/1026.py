n = int(input())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

lista.sort()
ans = 0
cnt = 0
for i in range(n):
    max_b = max(listb)
    ans =  max_b*lista[i]
    listb.remove(max_b)
    cnt += ans
print(cnt)
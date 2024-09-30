num = list(map(int, input().split()))
ans = 0
for i in num:
    num_wprhq = i**2
    ans += num_wprhq
    answer = ans%10
print(answer)
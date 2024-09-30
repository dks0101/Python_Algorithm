import sys
input = sys.stdin.readline

n = int(input())
card_n = list(map(int, input().split()))
m = int(input())
card_m = list(map(int, input().split()))
    
ans = {}
for i in card_n:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
# print(ans)

for j in card_m:
    result = ans.get(j)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
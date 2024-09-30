import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())  
    clothes = {}
    for i in range(n):
        cloth, clo_ty = map(str, input().split())
        if clo_ty in clothes.keys():
            clothes[clo_ty] += 1
        else:
            clothes[clo_ty] = 1
    cnt = 1
    for value in clothes.values():
        cnt *= (value+1)
    print(cnt-1)
# (종류 + 1) * (종류 + 1) -1 = cnt (맨 마지막에 -1을 하는 이유는 알몸 상태를 제외해야하기 때문이다.)
# clothes에서 cloth의 타입별로 몇 개가 있는지 확인해야한다.
# 그래서 clo_ty에 따라 이미 존재한다면 +1을 해주고 없다면 하나의 종류를 생성해준다.
# 그리고 맨 위의 식에 따라 계산을 해야하므로 clothes의 values 값만 뽑은 후
# 계산해준다.
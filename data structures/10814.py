import sys
input = sys.stdin.readline

n = int(input())
agelist = []
for i in range(n):
    age, name = input().split()
    agelist.append([int(age), name])
# print(agelist)
# agelist.sort()

agelist_sorted = sorted(agelist, key=lambda x: x[0])
for i in agelist_sorted:
    print(i[0], i[1])

######################################################
# 정렬을 할 때 labmda란 무엇일까??
# 만약 2개의 값을 가진 list가 있다면 key = lambda x : x[0]를 이용하여
# x[0]에 대해 정렬을 할 수 있다.
# 입력받은 순서대로 나이순으로 정렬만 하면 되므로 나이만 가지고 정렬을 하면 이 문제를 풀 수 있다.
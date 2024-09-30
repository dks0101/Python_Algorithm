import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))
sorted_arr = sorted(arr, key = lambda x: (x[1], x[0]))

for i in sorted_arr:
    print(i[0], i[1])


# x,y를 int로 안해주고 str로 해줘서 틀림 띠바

# 그리고 list 안에 2개의 값이 있을 때 lambda를 사용해서 정렬해주고 싶은 순서대로 
# x[0], x[1] 이런식으로 넣어주면 됨.
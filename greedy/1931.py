n = int(input())
time = []
for i in range(n):
    first, end = map(int,input().split())
    time.append((first, end))
time.sort(key=lambda x : (x[1],x[0]))
cnt = 1
finish = time[0][1]
for i in range(1, n):
    if time[i][0] >= finish:
        finish = time[i][1]
        cnt +=1
print(cnt)

# time[1]를 기준으로 오름차순 -> time[0]을 내림차순 정렬
#
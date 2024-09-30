import sys
input = sys.stdin.readline

# t = int(input())
# for i in range(t):
n = int(input())
employee = []
cnt = 1
for i in range(n):
    paper, interview = map(int, input().split())
    employee.append((paper, interview))
employee.sort() 

minemployee = employee[0][1]
# print(minemployee)
for j in range(1, n):
    if employee[j][1] < minemployee:
        cnt+=1
        # print("cnt:     ", cnt)
        minemployee=employee[j][1] # 어차피 밑에는 서류점수가 낮으므로 이 점수보다 낮은 점수는 붙을 수 없다. 그러므로 갱신
        # print(minemployee)
print(cnt)
# print(employee)

# 1. 서류를 중심으로 sort()
# 2. 그리고 면접을 중심으로 sort()
# 3. 일단 min을 1,4로 두기
# 4. 2~7까지 비교해보면 4보다 작은 수가 있다면 cnt += 1
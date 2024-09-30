# t = int(input())
# sum = 0
# people = 1
# for i in range(t):
#     k = int(input())
#     n = int(input())
#     while people<=n:
#         if k-1==0:
#             sum +=  people
#             people += 1  
# print(sum)


# 1층 3호 - 0층의 1~3호까지 사람들의 수의 합
# 2층 3호 - 1층의 1~3호 의 합
# 1층 1호 - 1명 / 1층 2호 - 3명 / 1층 3호 - 6
# 2층 3호 - 1+3+6 = 10



for _ in range(int(input())):
    k, n = int(input()), int(input())
    residents = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]
    print(residents[-1])
import sys
input = sys.stdin.readline

# 사이트-비밀번호 저장할 딕셔너리
site_dict = {}

# n: 사이트 수, m: 찾을 사이트 수
n, m = map(int, input().split())

# 사이트와 비밀번호를 딕셔너리에 저장
for i in range(n):
    site, password = input().split()
    site_dict[site] = password

# 찾을 사이트 입력받기
site_find_arr = []
for j in range(m):
    site_find = input().strip()  # 줄바꿈 제거
    site_find_arr.append(site_find)

# 찾은 사이트 순서대로 비밀번호 출력
for site in site_find_arr:
    print(site_dict[site])


# 내가 list 이용해서 적은 코드 - 시간초과 발생
# import sys
# input = sys.stdin.readline

# site_arr = []
# n, m = map(int, input().split())
# for i in range(n):
#     site, password = map(str, input().split())
#     site_arr.append((site, password))

# site_find_arr = []
# for j in range(m):
#     site_find = str(input())
#     site_find_arr.append(site_find)
    
# clean_data = [item.strip() for item in site_find_arr]

# for site in clean_data:
#     # site_arr에서 사이트를 찾아서 비밀번호 출력
#     for s, password in site_arr:
#         if s == site:
#             print(password)
#             break  # 비밀번호 찾으면 반복 종료 (다음 사이트로 이동)
n = int(input())  # 과일의 개수 N 입력
fruit_in = list(map(int, input().split()))  # 과일 리스트 S 입력

max_len = 0  # 두 종류 이하의 과일로 만든 최대 부분 배열의 길이
left = 0  # 슬라이딩 윈도우의 왼쪽 끝
fruit_count = {}  # 현재 윈도우에서 과일의 개수를 저장할 딕셔너리

# 윈도우의 오른쪽 끝을 확장하면서 처리
for right in range(n):
    fruit = fruit_in[right]
    
    # 현재 과일을 딕셔너리에 추가 (과일의 개수 증가)
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
    
    # 과일 종류가 3개 이상일 때, 왼쪽 끝을 줄여가며 과일 개수를 감소시킴
    while len(fruit_count) > 2:
        left_fruit = fruit_in[left]
        fruit_count[left_fruit] -= 1
        
        # 만약 과일 개수가 0이 되면 딕셔너리에서 제거
        if fruit_count[left_fruit] == 0:
            del fruit_count[left_fruit]
        
        left += 1  # 왼쪽 끝을 한 칸 이동
    
    # 현재 슬라이딩 윈도우 크기 갱신 (최대 길이)
    max_len = max(max_len, right - left + 1)

# 결과 출력: 두 종류 이하의 과일로 만든 가장 긴 탕후루 길이
print(max_len)

import sys
n = int(sys.stdin.readline())
s = set()
for i in range(n):
    ord = sys.stdin.readline().split()
    if len(ord) > 1:  # 숫자가 입력되었을 경우 처리
        num = int(ord[1])  # 숫자를 정수로 변환
    if ord[0] == "add":
        s.add(num)
    elif ord[0] == "remove":
        try:
            s.remove(num)
        except:
            pass
    elif ord[0] == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif ord[0] == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif ord[0] == "all":
        s = set([i for i in range(1, 21)])
    elif ord[0] == "empty":
        s = set()
t = int(input())
for i in range(t):
    s = list(input().split())
    num = int(s[0])
    res = ''.join([word * num for word in s[1]])
    print(res)
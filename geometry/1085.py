x, y, w, h = map(int, input().split())

a = w-x
b = h-y

list = [x, y, a, b]
ans = min(list)
print(ans)
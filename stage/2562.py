list = []

for i in range(9):
    a = int(input())
    list.append(a)
    max_value = max(list)
print(max_value)
print(list.index(max_value)+1)
list_n= []
for i in range(1, 11):
    n = int(input())
    num = n % 42
    list_n.append(num)
    res = set(list_n)
print(len(res))
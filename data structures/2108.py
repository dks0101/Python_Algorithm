import sys
n = int(sys.stdin.readline())

list_a = []
for i in range(n):
    value = int(sys.stdin.readline())
    list_a.append(value)

sum_a = 0
sum_a = sum(list_a)
average = round(sum_a/n)
print(average)

list_a.sort()
print(list_a[n//2])

dict = {}
for i in list_a:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] += 1
max_cnt = max(dict.values())
max_arr = sorted([k for k,v in dict.items() if v == max_cnt])
if len(max_arr)>1:
  print(max_arr[1])
else:
  print(max_arr[0])

max_a = max(list_a)
min_a = min(list_a)
print(max_a - min_a)
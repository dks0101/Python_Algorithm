from collections import Counter

lista = []
listb=[]
result = []

for i in range(3):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)
cnta = Counter(lista)
resulta = [item for item in lista if cnta[item] == 1]
cntb = Counter(listb)
resultb = [item for item in listb if cntb[item]==1]

print(resulta[0], resultb[0])

# 출력이 list가 되면 안 되므로 각각 원소만 출력해주기
# Counter 모듈 이용하여 list 안의 중복된 값 제거하기
import sys
input = sys.stdin.readline

arr_x = []
arr_y = []
for i in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)
# inclination1 = (arr_x[0] - arr_x[1]) / (arr_y[0] - arr_y[1])
# inclination2 = (arr_x[1] - arr_x[2]) / (arr_y[1] - arr_y[2])

inclination2 = (arr_y[1]-arr_y[0])*(arr_x[2]-arr_x[1])
inclination1 = (arr_y[2]-arr_y[1])*(arr_x[1]-arr_x[0])

# print(inclination1, inclination2)
if inclination1 == inclination2:
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")


# 기울기로 구하면 런타임 에러
# 외적 이용하여 구하기 -> (x2 - x1)*(y3-y1) = (y2-y1)*(x3-x1)

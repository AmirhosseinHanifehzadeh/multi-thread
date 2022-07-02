
n, x, y = list(map(int, input().split()))
num1 = n // x
num2 = n // y
value = True
for i in range(0, num1 + 1):
    for j in range(0, num2 + 1):
        if x * i + y * j == n:
            print(i, j)
            value = False
            break
    if value == False:
        break
if value:
    print('-1')


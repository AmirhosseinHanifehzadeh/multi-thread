import math
for a in range(1,500):
    for  b in range(1,500):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(f'{c},{b},{a}')
                    
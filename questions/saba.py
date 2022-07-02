import math


n = int(input())
k = int(input())
while k != 0:
    n = n / 2
    k -= 1

print(math.floor(n))

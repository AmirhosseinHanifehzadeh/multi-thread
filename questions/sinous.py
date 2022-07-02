def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1,n + 1):
            fact *= i

    return fact


def sinus(n):
    radianNum = n * 3.14 / 180
    sumVal = 0

    def inner(x):
        nonlocal radianNum
        nonlocal sumVal

        for i in range(x):
            sign = (-1) ** i
            sumVal += sign * radianNum ** (2*i + 1) / factorial(2*i + 1)

        return round(sumVal,6)
    return inner

n, x = input().split()
n= int(n)
x = float(x) 

value = sinus(x)
print(value(n))
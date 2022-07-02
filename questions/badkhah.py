n = int(input())
factor = n // 4
if n % 4 == 2:
    print(f'{factor + 1} {factor * -1}')
elif n % 4 == 3:
    print(f'{factor + 1} {factor + 1}')
elif n % 4 == 0:
    print(f'{factor * -1} {factor}')
elif n % 4 == 1:
    print(f'{factor * -1} {factor * -1}')






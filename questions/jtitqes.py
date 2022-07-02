m = int(input("please enter first number: "))
n = int(input("pleae enter second number: "))
value_sum = 0
for num in range(m, n):
    if num % 3 == 0:
        value_sum += num
print(value_sum)

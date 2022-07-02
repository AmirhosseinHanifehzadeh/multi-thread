from math import sqrt

a, b, x = list(map(int, input().split()))
a_list = []
b_list = []
counter = 0
i = 1
j = 1
while i <= sqrt(a):
    if a % i == 0:
        if a / i == i:
            a_list.append(i)
        else:
            a_list.append(a / i)
            a_list.append(i)
    i += 1

while j <= sqrt(b):
    if b % j == 0:
        if b / j == j:
            b_list.append(j)
        else:
            b_list.append(b / j)
            b_list.append(j)
    j += 1

for a_index in a_list:
    for b_index in b_list:
        if a_index + b_index <= x:
            counter += 1

print(counter)

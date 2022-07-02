n = int(input())
sum_list = []
alist = list(map(int, input().split()))

max_value = max(alist)

for i in range(n):
    for j in range(1, n + 1):
        if alist[i:j] != []:
            value = sum(alist[i:j])
            sum_list.append(value)

if max_value > max(sum_list):
    x = max_value
else:
    x = max(sum_list)
if x > 0:
    print(x)
else:
    print(0)

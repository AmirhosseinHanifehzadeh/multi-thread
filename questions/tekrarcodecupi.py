m = int(input())
alist = list(map(int, input().split()))
for value in alist:
    if value <= 3:
        print('*' * value)
    else:
        print('*')

n, p, q = list(map(int, input().split()))
alist = []
for i in range(n):
    var = input()
    alist.append(var[:p] + var[len(var) - q:len(var)])
print(len(set(alist)))
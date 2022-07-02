
length_alist = int(input())
alist = list(map(int, input().split()))
alist1 = alist.copy()
counter = 0

while length_alist != 1:
    if alist[counter] > alist[counter + 1]:
        del alist[counter + 1]
        length_alist -= 1 
    else:
        del alist[counter]
        length_alist -= 1

var = alist[0]

for i in range(len(alist1)):
    if alist1[i] == var:
        print(i + 1)

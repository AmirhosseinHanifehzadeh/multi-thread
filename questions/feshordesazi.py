
m = input()
alist = []
Istrue = True
for digit in m :
    alist.append(digit)

while Istrue:
    if alist[0] == '=':
        del alist[0]
    else:
        Istrue = False
        
var = len(alist)
num = 0

while num != var:
    if alist[num] == '=':
        del alist[num]
        if num - 1 >= 0 :
            del alist[num - 1]
            var -= 2 
            num -= 1 
        else:
            num -= 1 
            var -= 1 
    else:
        num += 1

print(''.join(alist))






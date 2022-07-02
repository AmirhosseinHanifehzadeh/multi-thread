s = input()
p = input()
counter = 0

for i in range(len(p)):
    if p[i:len(s) + i] == s:
        print("Yes")
        counter += 1 
        break
if counter < 1:
    print('No')
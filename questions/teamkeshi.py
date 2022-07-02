a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
counter = 0 
if b1 < a1:
    counter += b1
else:
    counter += a1 
if b2 < a2:
    counter += b2
else:
    counter += a2 
if b3 < a3:
    counter += b3
else:
    counter += a3

print(counter)

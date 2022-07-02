a, b, l = map(int, input().split())
if l % 2 == 0:
    print((a+b)*l/2)
elif l % 2 == 1:
    print((a+b)*(l-1)/2+a)
elif l == 0:
    print("duck can't sing:)")
else:
    print('enter a number.')

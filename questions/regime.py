m = input()
counter_red = 0
counter_yellow = 0
counter_green = 0

for i in m:
    if i == 'R':
        counter_red += 1
    elif i == 'Y':
        counter_yellow += 1
    else:
        counter_green += 1

if counter_red >= 3 or counter_green == 0:
    print('nakhor lite')
elif counter_yellow >= 2 and counter_red == 2:
    print('nakhor lite')
else:
    print('rahat baash')
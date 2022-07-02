n, x, y = list(map(int, input().split()))
charge_numbers = list(map(int, input().split()))
mincharge = min(charge_numbers)
charge_numbers.remove(mincharge)
number1 = mincharge // x 
number2 = 0 
for item in charge_numbers:
    if item // y < item / y < item // y + 1:
       number2 += item // y + 1 
    else:
        number2 += item / y  
if number1 >= number2:
    print('YES')
else:
    print("NO")



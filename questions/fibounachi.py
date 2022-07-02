x1 = 0 
x2 = 1 
number = int(input('enter a number? '))

if number >= 2 :
    print(x1)
    print(x2)
    counter = 2 
    while counter < number:
        x3 = x1 + x2
        print(x3) 
        x1 = x2 
        x2 = x3 
        counter += 1


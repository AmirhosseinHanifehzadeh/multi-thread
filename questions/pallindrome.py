pallindrome_list = []

for i in range(99, 1, -1):
    for j in range(99, 1, -1):
        number = str(i * j)
        if number == number[::-1]:
            print(f'{i} * {j} = {number}')
            break

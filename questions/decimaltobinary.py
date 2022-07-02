from timeit import default_timer

def decimal_to_binary(decimal_number):
    ration_number = decimal_number // 2
    remaining_number = decimal_number % 2
    remaining_list = []
    while ration_number != 0:
        ration_number = decimal_number // 2
        remaining_number = decimal_number % 2
        remaining_list.append(remaining_number)
        decimal_number = ration_number

    for i in remaining_list[::-1]:
        print(i, end='')


def timer(n):
    start = default_timer()
    decimal_to_binary(n)
    print(default_timer() - start)

timer(18)
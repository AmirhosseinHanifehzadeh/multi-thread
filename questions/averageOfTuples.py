finall_tup = tuple()
def average_tuple(tup):
    '''function to find average
    create a nested loop that first loop go over value of inner tuple 
    and second one go over value of outer tuple
    '''
    # n = lenght tuple , m = lenght inner tuples
    global finall_tup
    n = len(tup)
    m = len(tup[0])

    for col in range(m):
        sum_value = 0
        for row in range(n):
            sum_value += tup[row][col]
        average_value = sum_value / n
        finall_tup += (average_value,)

    return finall_tup

if __name__ == '__main__':
    expression_to_evaluate = input()
    print(eval(expression_to_evaluate))
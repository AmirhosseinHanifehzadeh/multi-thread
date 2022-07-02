from time import perf_counter, sleep

def averager(numbers):
    """it gives multiple varialbe and return average of them"""
    def inner():
        nonlocal numbers
        return sum(numbers) / len(numbers)

    return inner

def Timer():
    ''' function to calculate spending time after create a object '''
    start = perf_counter() # starting time
    def x():
        nonlocal start
        end = perf_counter()
        return round(end - start)
    return x

x = Timer()
for i in range(5):
    print(x())
    sleep(2)

'''
    A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution.
    we use it in two situation: 
    1. when we have a simple class, we use closure instead.
    2. when we wan to prevent having global variables.   
'''
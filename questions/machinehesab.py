from functools import wraps
from time import perf_counter , sleep

def log(original_function):
    '''a decorator to show some information about function'''
    @wraps(original_function)
    def inner(*args, **kwargs):
        start = perf_counter() # start time
        sleep(0.6)
        original_function_value = original_function(*args, **kwargs)
        end = perf_counter()   # end time 
        print(f"Function Name: '{original_function.__name__}'")
        if len(args) == 0:
            print('Value Error: At least one number must be entered.')
        elif 'operation' in kwargs.keys() and kwargs['operation'] not in ['SUB', 'ADD', 'MUL','DIV']:
            print('Value Error: Operation must be ADD, SUB, MUL or DIV')
        elif 'output_format' in kwargs.keys() and kwargs['output_format'] not in ['int', 'float']:
            print('Value Error: Format must be float or int')
        else:
            print(f"Number of Positional Arguments: {len(args)}")
            print(f"Keyword Arguments: {kwargs}")
        print(f"return value: {original_function_value}")
        if end - start > 1:
            print("Time Consumption: more than a second")
        else:
            print("Time Consumption: less than a second")

    return inner

@log
def calculator(*args, operation='ADD', output_format='float'):
    '''claculator function 
        with optional arguments
        and add operation by default 
        output format should be int or float (client can choose)    '''
    try:
        if operation not in ['SUB', 'ADD', 'MUL','DIV']:
            raise ValueError
        if output_format not in ['int', 'float']:
            raise ValueError
                
        if len(args) > 1:
            if operation == 'ADD':
                result = 0
                for arg in args:
                    result += float(arg)
                if output_format == 'int':
                    return eval('round(' + output_format + f'({result})' + ')')
                return eval(output_format + f'({result})')
                        
            elif operation == 'DIV':
                result = float(args[0])
                for i in range(1, len(args)):
                    result /= float(args[i])
                if output_format == 'int':
                    return eval('round(' + output_format + f'({result})' + ')')
                return eval(output_format + f'({result})')

            elif operation == 'MUL':
                result = 1
                for arg in args:
                    result *= float(arg)
                if output_format == 'int':
                    return eval('round(' + output_format + f'({result})' + ')')
                return eval(output_format + f'({result})')

            elif operation == 'SUB':
                result = 0
                for i in range(len(args)):
                    result -= float(args[i])
                if output_format == 'int':
                    return eval('round(' + output_format + f'({result})' + ')')
                return eval(output_format + f'({result})')

        elif len(args) == 1:
            return ''
        else:
            raise ValueError
    except ValueError:
        return 'None'


# your submission must include following lines of codes
if __name__ == '__main__':
    code_to_execute = input()
    exec(code_to_execute)

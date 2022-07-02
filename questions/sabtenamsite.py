import re
from functools import wraps

ans_list = []
clients = []
controller_signUp = True
value = True
def has_num(func):
    @wraps(func)
    def inner(string):
        global controller_signUp
        global ans_list
        for i in string:
            if i.isdigit():
                return func(string)

        ans_list.append(f"{func.__name__.split('_')[1]} should have at least one number!") 
        controller_signUp = False
        return func(string)

    return inner

def has_uppercase(func):
    @wraps(func)
    def inner(string):
        global controller_signUp
        global ans_list

        if not bool(re.search('([A-Z])', string)):
            ans_list.append(f"{func.__name__.split('_')[1]} should have at least one capital letter!") 
            controller_signUp = False
            return func(string)
        return func(string)
        
    return inner

def has_lowercase(func):
    @wraps(func)
    def inner(string):
        global controller_signUp
        global ans_list

        if not bool(re.search('([a-z])', string)):
            ans_list.append(f"{func.__name__.split('_')[1]} should have at least one lowercase letter!") 
            controller_signUp = False
            return func(string)
        return func(string)
        
    return inner

def length_bigger_than_8(func):
    @wraps(func)
    def inner(string): 
        global controller_signUp
        global ans_list

        if len(string) < 8:
            ans_list.append(f"{func.__name__.split('_')[1]} have to be at least 8 characters!") 
            controller_signUp = False
            return func(string)
        return func(string)
                
    return inner

@length_bigger_than_8
@has_uppercase
@has_lowercase
@has_num
def validation_username(username):
    return username 

@length_bigger_than_8
@has_uppercase
@has_lowercase
@has_num
def validation_password(password):
    return password

def signUp(sen):
    global clients
    global controller_signUp
    global ans_list

    username = sen.split()[2]
    password = sen.split()[3]
    validation_username(username)
    validation_password(password)

    if controller_signUp:
        clients.append([username, password])
        ans_list.append(f'{username} signed up successfully!')




def logIn(sen):
    global clients 
    global ans_list

    username_list = []
    password_list = []

    username = sen.split()[2]
    password = sen.split()[3]
    for client in clients:
        username_list.append(client[0])
        password_list.append(client[1])

    if clients != []:
        if username in username_list:
            if password in password_list:
                if username_list.index(username) == password_list.index(password):
                    ans_list.append(f'{username} logged in successfully!')
            else:
                ans_list.append('username or password is not correct!')
        else:
            ans_list.append('username or password is not correct!')
    else:
        ans_list.append('you should sign up first!')
           
while value:
    com = input()
    if com.split()[0] == 'Sign':
        signUp(com)
    elif com.split()[0] == 'Log':
        logIn(com)
    elif com == 'exit':
        for answer in ans_list:
            print(answer)
        value = False

    
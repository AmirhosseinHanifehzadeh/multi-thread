import re

q = int(input())
clients = []
ans_list = []

def connect(com):
    ip = com.split(':')[0]
    username = com.split(':')[1]
    regex = re.compile('[_*$#]')

    if regex.search(username) == None:
        clients.append([ip, username, 0])

    else:
        ans_list.append('invalid username')


def deposit(com):
    money = int(com.split(':')[2])
    depositer_ip = com.split(':')[0]
    receiver_username = com.split(":")[1]
    loop_stopper = 0

    for client in clients:
        if client[0] == depositer_ip:
            client[2] -= money
            loop_stopper += 1
        elif receiver_username == client[1]:
            client[2] += money
            loop_stopper += 1
        if loop_stopper == 2:
            break


def showMoney(com):
    for client in clients:
        if client[0] == com:
            ans_list.append(client[2])
            return 

for i in range(q):
    var = input()
    type_command = var.split()[0]
    command = var.split()[1]
    if type_command == '1':
        connect(command)
    elif type_command == '2':
        deposit(command)
    else:
        showMoney(command)

for answer in ans_list:
    print(answer)

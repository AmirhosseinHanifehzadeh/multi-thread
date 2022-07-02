n = int(input())
names_list = []
friends_list = []
counter = 1
for i in range(n):
    names_list.append(input())
    names_list.append(0)


while counter != n + 1:
    sender_name = input()
    sender_money, sender_friend = input().split()
    for i in range(int(sender_friend)):
        friends_list.append(input())

    if int(sender_friend) != 0:
        given_money = int(sender_money) // int(sender_friend)
        lossing_money = given_money * int(sender_friend)
        for i in friends_list:
            names_list[names_list.index(i) + 1] += given_money

        names_list[names_list.index(sender_name) + 1] -= lossing_money

    friends_list = []
    counter += 1

for i in range(0,len(names_list),2):
    print(f'{names_list[i]} {names_list[i + 1]}')


     
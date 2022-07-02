game_table = []
finall_cheker2 = True
finall_checker3 = True

for i in range(6):
    game_table.append(list('0' for i in range(7)))

n = int(input())
move_table = list((map(int, input().split(' ', n))))


def addPlayerName(start, col):
    global game_table
 
    if start == 0:
        player_name = 'r'
    else:
        player_name = 'y'

    j = 0
    value = True

    while value:
        if game_table[j][col] == '0':
            game_table[j][col] = player_name
            value = False
        else:
            j += 1


for i in range(n):
    addPlayerName(i % 2, move_table[i] - 1)


def rowWinner():
    global finall_cheker2
    global finall_checker3
    row = -1
    counter = 1

    while row != 5:
        row += 1
        for j in range(6):
            if game_table[row][j] == game_table[row][j + 1] != '0':
                counter += 1
                if counter == 4:
                    finall_cheker2 = False
                    finall_checker3 = False
                    print('Winner = ' +  game_table[row][j])
                    row = 5
                    break
            else:
                counter = 1


def colWinner():
    global finall_checker3
    col = -1
    counter = 1

    while col != 6:
        col += 1
        for row in range(5):
            if game_table[row][col] == game_table[row + 1][col] != '0':
                counter += 1
                if counter == 4:
                    finall_checker3 = False
                    print('Winner = ' + game_table[row][col])
                    col = 6
                    break
            else:
                counter = 1


def skewedWinner():
    global game_table
    counter = 1

    # ltr row 1
    for i in range(5):
        if game_table[i][i] == game_table[i + 1][i + 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][i])
                return
        else:
            counter = 1
            if i >= 2:
                break

    for i in range(5):
        j = i + 1
        if game_table[i][j] == game_table[i + 1][j + 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            if i >= 2:
                break

    for i in range(4):
        j = i + 2
        if game_table[i][j] == game_table[i + 1][j + 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            if i >= 1:
                break

    for i in range(3):
        j = i + 3
        if game_table[i][j] == game_table[i + 1][j + 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            break
    
    # rtl row 1
    for i in range(5):
        j = 6 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return
        else:
            counter = 1
            if i >= 2:
                break
    
    for i in range(5):
        j = 5 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return
        else:
            counter = 1
            if i >= 2:
                break

    for i in range(4):
        j = 4 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return
        else:
            counter = 1
            if i >= 1:
                break

    for i in range(3):
        j = 3 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return
        else:
            counter = 1
            break
    # ltr row 2
    for i in range(1, 5):
        j = i - 1
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            if i >= 2:
                break
    # ltr row 3
    for i in range(2,5):
        j = i - 2
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            if i >= 2:
                break
    
    # rtl row 2
    for i in range(1, 5):
        j = 7 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            if i >= 2:
                break
    # trl row 3
    for i in range(2,5):
        j = 8 - i
        if game_table[i][j] == game_table[i + 1][j - 1] != '0':
            counter += 1
            if counter == 4:
                print('Winner = ' + game_table[i][j])
                return

        else:
            counter = 1
            break


rowWinner()
if finall_cheker2:
    colWinner()
if finall_checker3:
    skewedWinner()


for i in range(5, -1, -1):
    for j in range(7):
        print(game_table[i][j], end=' ')
    print()

player_list = []
team_list = []
team_status = []
teamsName = []
id_player = 1
id_team = 1
value = True
ans_list = []


def addPlayer(sentence: str):
    global player_list
    global id_player
    test_list = []

    test_list.append(id_player)
    for word in range(2, 7):
        test_list.append(sentence.split()[word])
    test_list.append(0)
    id_player += 1
    player_list.append(test_list)


def addTeam(sentence: str):
    global team_list
    global id_team
    global team_status
    global teamsName
    test_list = []
    if sentence.split()[2] not in teamsName:
        teamsName.append(sentence.split()[2])
        test_list.append(id_team)
        test_list.append(sentence.split()[2])
        test_list.append(int(sentence.split()[3]))
        test_list.append([])
        team_status.append([0,0])
        team_status[id_team - 1].append(id_team)
        id_team += 1
        team_list.append(test_list)
    else:
        teamIndex = teamsName.index(sentence.split()[2])
        team_list[teamIndex][2] = int(sentence.split()[3])


def buyPlayer(sentece: str):
    global team_list
    global player_list
    global ans_list

    if int(sentece.split()[1]) > len(player_list):
        ans_list.append(f'player with the id {sentece.split()[1]} doesnt exist')
    elif int(sentece.split()[2]) > len(team_list):
        ans_list.append(f'team with the id {sentece.split()[2]} doesnt exist')
    elif int(player_list[int(sentece.split()[1]) - 1][2]) > team_list[int(sentece.split()[2]) - 1][2]:
        ans_list.append('the team cant afford to buy this player')
    elif player_list[int(sentece.split()[1]) - 1][6] != 0:
        ans_list.append('player already has a team')
    else:
        team_list[int(sentece.split()[2]) - 1][3].append(int(sentece.split()[1]))
        player_list[int(sentece.split()[1]) - 1][6] = int(sentece.split()[2])
        team_list[int(sentece.split()[2]) - 1][2] -= int(player_list[int(sentece.split()[1]) - 1][2])
        ans_list.append('player added to the team succesfully')


def sellPlayer(sentence: str):
    global team_list
    global player_list
    global ans_list

    if int(sentence.split()[2]) > len(team_list):
        ans_list.append('team doesnt exist')
    elif int(sentence.split()[1]) not in team_list[int(sentence.split()[2]) - 1][3]:
        ans_list.append('team doesnt have this player')
    else:
        team_list[int(sentence.split()[2]) - 1][3].remove(int(sentence.split()[1]))
        player_list[int(sentence.split()[1]) - 1][6] = 0
        team_list[int(sentence.split()[2]) - 1][2] += int(player_list[int(sentence.split()[1]) - 1][2])
        ans_list.append('player sold succesfully')


def Match(sentence: str):
    global team_list
    global player_list
    global team_status
    global ans_list

    firstTeamStrong = 0
    secondTeamStrong = 0

    if int(sentence.split()[1]) > len(team_list) or int(sentence.split()[2]) > len(team_list):
        ans_list.append('team doesnt exist')
    else:
        counterFisrtTeam = len(team_list[int(sentence.split()[1]) - 1][3])
        counterSecondTeam = len(team_list[int(sentence.split()[2]) - 1][3])
        if counterFisrtTeam < 11 or counterSecondTeam < 11:
            ans_list.append('the game can not be held due to loss of the players')
        else:
            for team in range(1, 3):
                for i in range(11):
                    indexPlayerTeam = team_list[int(sentence.split()[team]) - 1][3][i] - 1
                    if team == 1:
                        firstTeamStrong += int(player_list[indexPlayerTeam][3]) + int(player_list[indexPlayerTeam][4])
                    else:
                        secondTeamStrong += int(player_list[indexPlayerTeam][3]) + int(player_list[indexPlayerTeam][5])

            if firstTeamStrong > secondTeamStrong:
                team_status[int(sentence.split()[1]) - 1][0] += 1
                team_status[int(sentence.split()[2]) - 1][1] += 1
                team_list[int(sentence.split()[1]) - 1][2] += 1000
            elif firstTeamStrong < secondTeamStrong:
                team_status[int(sentence.split()[2]) - 1][0] += 1
                team_status[int(sentence.split()[1]) - 1][1] += 1
                team_list[int(sentence.split()[2]) - 1][2] += 1000


def Rank():
    global team_status
    global team_list
    global ans_list

    team_status.sort(key= lambda row:(-row[0], row[1], row[2]))
    for i in range(len(team_status)):
        ans_list.append(f'{i + 1}. {team_list[team_status[i][2] - 1][1]}')


while value:
    inputVal = input()
    if inputVal != '':
        if inputVal.split()[0] == 'new':
            if inputVal.split()[1] == 'player':
                addPlayer(inputVal)
            else:
                addTeam(inputVal)
        else:
            if inputVal.split()[0] == 'buy':
                buyPlayer(inputVal)
            elif inputVal.split()[0] == 'sell':
                sellPlayer(inputVal)
            elif inputVal.split()[0] == 'match':
                Match(inputVal)
            elif inputVal == 'rank':
                Rank()
            else:
                value = False


for ans in ans_list:
    print(ans)

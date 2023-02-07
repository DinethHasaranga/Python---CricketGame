import random
import pandas as pd
from itertools import combinations

data = pd.read_excel("D:\\DINETH HASARANGA\\Python_Projects\\CricketCW-Python\\cricT.xlsx", header=0, usecols='A:D')
data2 = pd.read_excel("D:\\DINETH HASARANGA\\Python_Projects\\CricketCW-Python\\cricT.xlsx", header=0, usecols='E:H')
# print(data.head())

data.columns = [x.upper() for x in data.columns]
data2.columns = [x.upper() for x in data2.columns]

x = data.iloc[0:11, :]
print(x)
y = data2.iloc[0:11, :]
print(y)

print('You can change the Teams as required in the next phase.','\n')

change_T_name = input('Do you need to change Team Name:Enter Y or N: ',)

if change_T_name=='Y':
    change_T_name_group = input("Enter the group name of the team as A or B: ", )
    if change_T_name_group == 'A':
        flag_1=True

        while flag_1:
            previous_team_name=input('Enter the exsisting Team Name: ',)
            new_team_name=input('Enter the new Team Name: ',)
            x.rename({previous_team_name:new_team_name},axis=1,inplace=True)
            print(x)

            change_T_name_group_A=input('Do you need to change Team Name again:Enter Y YB or N: ',)

            if change_T_name_group_A=='Y':
                continue
            elif change_T_name_group_A=='YB':

                flag_2= True
                while flag_2:
                    previous_team_name = input('Enter the exsisting Team Name: ', )
                    new_team_name = input('Enter the new Team Name: ', )
                    y.rename({previous_team_name: new_team_name}, axis=1, inplace=True)
                    print(y)
                    change_T_name_group_A_B = input('Do you need to change Team Name again:Enter Y or N: ', )
                    if change_T_name_group_A_B=='Y':
                        continue
                    elif change_T_name_group_A_B=='N':
                        flag_2=False
                        flag_1=False
                        change_T_name = input('Do you need to change Team Name:Enter Y or N: ', )


            elif change_T_name_group_A=='N':
                flag_1=False
                change_T_name = input('Do you need to change Team Name:Enter Y or N: ', )
    elif change_T_name == 'N':
        flag_1 = False

    if change_T_name_group == 'B':
        flag_1 = True

        while flag_1:
            previous_team_name = input('Enter the exsisting Team Name: ', )
            new_team_name = input('Enter the new Team Name: ', )
            y.rename({previous_team_name: new_team_name}, axis=1, inplace=True)
            print(y)

            change_T_name_group_B = input('Do you need to change Team Name again:Enter Y YA or N: ', )

            if change_T_name_group_B == 'Y':
                continue
            elif change_T_name_group_B == 'YA':

                flag_2 = True
                while flag_2:
                    previous_team_name = input('Enter the exsisting Team Name: ', )
                    new_team_name = input('Enter the new Team Name: ', )
                    x.rename({previous_team_name: new_team_name}, axis=1, inplace=True)
                    print(x)
                    change_T_name_group_B_A = input('Do you need to change Team Name again:Enter Y or N: ', )
                    if change_T_name_group_B_A == 'Y':
                        continue
                    elif change_T_name_group_B_A == 'N':
                        flag_2 = False
                        flag_1 = False
                        change_T_name = input('Do you need to change Team Name:Enter Y or N: ', )


            elif change_T_name_group_B == 'N':
                flag_1 = False
                change_T_name = input('Do you need to change Team Name:Enter Y or N: ', )
    elif change_T_name == 'N':
        flag_1 = False

print('\n')
print('You can change the players in the next stage if required.You may type the row number of the player and the name of the country in BLOCK CAPITALS.','\n')
change = input('Do you need to change Team Players:Enter Y or N: ', )
if change == 'Y':
    print('You can change Team Players')
    change_T = input('Enter the Team Name, A/B: ')

    if change_T == 'A':
        flag = True

        while flag:
            if change == 'Y':
                try:
                    row = int(input('Enter the row number of the player: '))
                except ValueError:
                    print('Enter an integer value between 1 and 11 !!!')
                    continue
                column = str(input('Type the name of the country: '))
                replace_p = str(input('Enter the name of the new player: '))

                x.loc[row, column] = replace_p
                print(x)

                print('If group B player needed to be change,Enter YB or If same group, Enter Y else to Start the Match, Enter N')
                change_N = input('Do u need to make another change,Enter YB/Y/N: ')
                if change_N == 'Y':
                    continue
                elif change_N == 'YB':
                    flag = True
                    while flag:
                        if change == 'Y':
                            try:
                                row = int(input('Enter the row number of the player: '))
                            except ValueError:
                                print('Enter an integer value between 1 and 11 !!!')
                                continue
                            column = str(input('Type the name of the country: '))
                            replace_p = str(input('Enter the name of the new player: '))

                            y.loc[row, column] = replace_p
                            print(y)

                            change_N = input('Do u need to make another change,Enter Y/N: ')
                            if change_N == 'Y':
                                continue
                            elif change_N == 'N':
                                print(y)
                                flag = False
                elif change_N == 'N':
                    print(x)
                    break

    elif change_T == 'B':
        flag = True
        while flag:
            if change == 'Y':
                try:
                    row = int(input('Enter the row number of the player: '))
                except ValueError:
                    print('Enter an integer value between 1 and 11 !!!')
                    continue
                column = str(input('Type the name of the country: '))
                replace_p = str(input('Enter the name of the new player: '))

                y.loc[row, column] = replace_p
                print(y)

                print('If group A player needed to be change,Enter YA or If same group, Enter Y else to Start the Match, Enter N')
                change_N = input('Do u need to make another change,Enter Y/YA/N: ')
                if change_N == 'Y':
                    continue
                elif change_N == 'YA':
                    flag = True

                    while flag:
                        if change == 'Y':
                            try:
                                row = int(input('Enter the row number of the player: '))
                            except ValueError:
                                print('Enter an integer value between 1 and 11 !!!')
                                continue
                            column = str(input('Type the name of the country: '))
                            replace_p = str(input('Enter the name of the new player: '))

                            x.loc[row, column] = replace_p
                            print(x)

                            change_N = input('Do u need to make another change,Enter YB/Y/N: ')
                            if change_N == 'Y':
                                continue
                            elif change_N == 'N':
                                print(x)
                                flag = False

                elif change_N == 'N':
                    print(y)
                    break
try:
    if change == 'N' or change_N == 'N' or change_T_name == 'N':
        teams = list(data.columns)
        teams1 = list(data2.columns)
        TEAM = list(teams + teams1)
        print(TEAM,'\n')

        flag = True

        while flag:
            global select_group_name
            Match_shedule_Team_A = list(combinations(teams, 2))
            Match_shedule_Team_B = list(combinations(teams1, 2))

            print('Below shows the match shedule of the Tournament for Group A first and Group B sceond.')
            print(Match_shedule_Team_A)
            print(Match_shedule_Team_B,'\n')
            data_teams = {'Team_A': teams, 'Team_B': teams1}

            select_group_name = input('Group name:', )
            select_team_1 = input('Team name:', )
            select_team_2 = input('Team name:', )
            selected_teams = (select_team_1, select_team_2)
            selected_teams_list_1 = list(selected_teams)
            print(list(selected_teams))

            break

        if flag == True:

            possibletoss = ['Head', 'Tail']
            toss = random.choice(possibletoss)
            print('The Toss is:', toss)

            Decision_F = 'Bat'
            Decision_F_other = 'Bowl'
            toss_won_team = random.choice(selected_teams)
            T = list(toss_won_team)
            selected_teams_list_1.insert(0, T)
            print('The Team which won the Toss:', toss_won_team)

            TOSS_W = True
            TOSS_L = True

            for i in selected_teams_list_1:
                if i == toss_won_team:
                    selected_teams_list_1.remove(toss_won_team)
                    selected_teams_list_1.pop(0)
                    selected_teams_list_1.insert(0, toss_won_team)
                    #print(selected_teams_list_1)   #list for making order
                    TW = selected_teams_list_1[0]
                    TL = selected_teams_list_1[1]
                    # print(TW)
                    # print(TL)
                    break

            print('' 
                  '')

            country = [i for i in data.columns]
            #print(country)

            country_2 = [i for i in data2.columns]
            #print(country_2)

            country_array_1 = [data[i].tolist() for i in data.columns]
            #print(country_array_1)

            country_array_2 = [data2[i].tolist() for i in data2.columns]
            #print(country_array_2)

            country_keys_1 = ['SRI LANKA', 'AUSTRALIA', 'BANGLADESH', 'WEST INDIES']
            country_keys_2 = ['INDIA', 'PAKISTAN', 'AFGHANISTAN', 'ENGLAND']

            country_dict_1 = dict(zip(country_keys_1, country_array_1))
            #print(country_dict_1)

            country_dict_2 = dict(zip(country_keys_2, country_array_2))
            #print(country_dict_2)

            # sri_lanka = data['SRI LANKA'].tolist()
            # print(sri_lanka)

            if select_team_1 == 'SRI LANKA' or select_team_2 == 'SRI LANKA':
                player_batsman_p = country_dict_1['SRI LANKA']
                print('Players of the team: ', player_batsman_p)
                #player_batsman=player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'AUSTRALIA' or select_team_2 == 'AUSTRALIA':
                player_batsman_p = country_dict_1['AUSTRALIA']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'BANGLADESH' or select_team_2 == 'BANGLADESH':
                player_batsman_p = country_dict_1['BANGLADESH']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'WEST INDIES' or select_team_2 == 'WEST INDIES':
                player_batsman_p = country_dict_1['WEST INDIES']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'INDIA' or select_team_2 == 'INDIA':
                player_batsman_p = country_dict_2['INDIA']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'PAKISTAN' or select_team_2 == 'PAKISTAN':
                player_batsman_p = country_dict_2['PAKISTAN']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'AFGHANISTAN' or select_team_2 == 'AFGHANISTAN':
                player_batsman_p = country_dict_2['AFGHANISTAN']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()

            if select_team_1 == 'ENGLAND' or select_team_2 == 'ENGLAND':
                player_batsman_p = country_dict_2['ENGLAND']
                print('Players of the team: ', player_batsman_p)
                #player_batsman = player_batsman_p

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                f.write('\n')
                f.write('Players of the team\n')
                f.write(str(player_batsman_p))

                f.close()


            def randomball(curruns, currwickets):
                possibilities = [0, 1, 2, 3, 4, 5, 6, 'W', 'WD', 'NB']
                otherpossibilities = [0, 1, 2, 3, 4, 5, 6]
                play = random.choice(possibilities)

                if play == 'WD':
                    play = random.choice(otherpossibilities)
                    return ('wide', play), curruns + 1 + play, currwickets

                elif play == 'NB':
                    play = random.choice(otherpossibilities)
                    return ('no ball', play), curruns + 1 + play, currwickets

                elif play == 'W':
                    return 'wicket', curruns, currwickets + 1

                else:
                    return play, curruns + play, currwickets


            def generateMatch(overs):
                global scorelist_global
                global bcr
                balls = overs * 6
                score = 0
                wickets = 0
                bcr = 1  # ball counter

                scorelist = []
                scorelist_global = scorelist

                while bcr <= balls:
                    if wickets < 10:
                        outcome = randomball(score, wickets)
                        play = outcome[0]

                        # print(outcome[0])
                        # print(outcome[1])

                        if isinstance(play, tuple):
                            outcomestr = str(play[0]) + ',' + str(play[1]) + ';' + f'{score + 1 + play[1]}-{wickets}'
                            score += 1 + play[1]

                        elif isinstance(play, int):
                            outcomestr = str(play) + ';' + f'{score + play}-{wickets}'
                            score += play

                        elif isinstance(play, str):
                            outcomestr = 'Wicket' + ';' + f'{score}-{wickets + 1}'
                            wickets += 1

                        scorelist.append(outcomestr)
                        bcr += 1
                    else:
                        print('scorelist', scorelist)
                        break
                print('scorelist', scorelist)


            def Batsman():
                global SCORE_LIST_BATSMAN
                scorelist_2 = scorelist_global

                l = []
                k = []
                for idx, val in enumerate(scorelist_2):
                    l.append(idx)
                    k.append(val)
                    # print(idx,val)
                # print(l)
                # print(k)

                keys = l
                values = k
                final = dict(zip(keys, values))
                print('Final', final)  # Dictionary used for creating the score list

                score_list_batsman = []
                c = -1
                c_wide = 0
                #c_wide_list = []
                c_noball = 0
                #c_noball_list = []
                for i in scorelist_2:
                    while c < bcr - 3:
                        c += 1

                        if final[c][0:6] == 'Wicket':
                            g = scorelist_2[c][0:6]
                            score_list_batsman.append(g)
                            # print('1',g)

                        elif final[c][0:4] == 'wide':
                            g = int(scorelist_2[c][5:6])
                            score_list_batsman.append(g)
                            c_wide += 1
                            # print('2',g)

                        elif final[c][0:7] == 'no ball':

                            g = int(scorelist_2[c][8:9])
                            score_list_batsman.append(g)
                            c_noball += 1
                            # print('3',g)

                        else:
                            g = int(final[c][0])
                            score_list_batsman.append(g)
                            # print('4',g)
                SCORE_LIST_BATSMAN = score_list_batsman

                # print('hi', score_list_batsman)  # score list used for batsman statistics
                print('EXTRAS')
                print('No. of wide balls', c_wide)  # To get no. of wides
                print('No. of no balls', c_noball)  # To get no. of noball

                def player_score():
                    global total
                    scorelist = SCORE_LIST_BATSMAN
                    # scorelist = (1, 2, 3, 45, 'W', 3, 4, 5, 6, 'W', 32, 13, 45, 6, 'W')
                    player_batsman = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')

                    player_c = 0
                    count = 1
                    w = 0
                    o = []
                    batsman_scorelist = []
                    batsman_scorelist2 = []

                    while count < bcr - 2:
                        for j in scorelist:
                            if j != 'Wicket':
                                # print(j)
                                o.append(j)
                                # print(o)

                            if j == 'Wicket':
                                total = sum(o)
                                batsman_scorelist.append(total)

                                # print(q)
                                # print('out')
                                player_c += 1
                                # print('batsman', player_c)

                            if count == bcr - 2:
                                # print('batsman_scorelist',batsman_scorelist)
                                # print(o)
                                total = sum(o) + int(c_wide) + int(c_noball)

                                batsman_scorelist.append(total)
                                print('sum of team', total)
                                print(''
                                      '')

                                for n in range(len(batsman_scorelist)):
                                    k = batsman_scorelist[n] - batsman_scorelist[n - 1]
                                    batsman_scorelist2.append(k)

                                p = batsman_scorelist2
                                p.pop(0)
                                p.insert(0, batsman_scorelist[0])
                                # print(p) #scorelist without wickets

                                keys = player_batsman
                                values = p
                                final_scorelist = dict(zip(keys, values))
                                print('Final scorelist of Batsman', final_scorelist,'\n')

                                method_of_miss = ('Hit Wicket', 'Catch', 'Run Out', 'LBW', 'Stumps', 'WK-Stumped')

                                print('Method of missing', '\n')
                                H = list(final_scorelist.keys())
                                for i in range(len(H)):
                                    l = random.choice(method_of_miss)
                                    print(l)
                                print('\n')

                            count += 1

                    sort_batsman_dict = {k: v for k, v in sorted(final_scorelist.items(), key=lambda v: v[1], reverse=True)}
                    # print(sort_batsman_dict)  #batsman are sorted in descending order of runs

                    best_5_batsman = list(sort_batsman_dict.items())
                    print('Highest run scorers', best_5_batsman[0:5])
                    print(''
                          ''
                          '')

                    f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")

                    f.write('\n')
                    f.write('NEW MATCH-FIRST BAT TEAM\n')
                    f.write('Batsman Performnce\n')
                    f.write(str(sort_batsman_dict))
                    f.write('\n')
                    f.write('Best 5 batsman..........\n')
                    f.write(str(best_5_batsman[0:5]))

                    f.close()

                player_score()


        def second_innings():
            def Batsman():
                global SCORE_LIST_BATSMAN_2
                scorelist_2 = scorelist_global

                l = []
                k = []
                for idx, val in enumerate(scorelist_2):
                    l.append(idx)
                    k.append(val)
                    # print(idx,val)
                # print(l)
                # print(k)

                keys = l
                values = k
                final = dict(zip(keys, values))
                print('final', final)  # Dictionary used for creating the score list

                score_list_batsman = []
                c = -1
                c_wide = 0
                c_wide_list = []
                c_noball = 0
                c_noball_list = []
                for i in scorelist_2:
                    while c < bcr - 3:
                        c += 1

                        if final[c][0:6] == 'Wicket':
                            g = scorelist_2[c][0:6]
                            score_list_batsman.append(g)
                            # print('1',g)


                        elif final[c][0:4] == 'wide':
                            g = int(scorelist_2[c][5:6])
                            score_list_batsman.append(g)
                            c_wide += 1
                            # print('2',g)


                        elif final[c][0:7] == 'no ball':

                            g = int(scorelist_2[c][8:9])
                            score_list_batsman.append(g)
                            c_noball += 1
                            # print('3',g)

                        else:
                            g = int(final[c][0])
                            score_list_batsman.append(g)
                            # print('4',g)
                SCORE_LIST_BATSMAN_2 = score_list_batsman

                # print('hi', score_list_batsman)  # score list used for batsman statistics
                print('EXTRAS')
                print('No. of wide balls', c_wide)  # To get no. of wides
                print('No. of no balls', c_noball)  # To get no. of noball

                def player_score():
                    global p_sum_i
                    scorelist = SCORE_LIST_BATSMAN_2
                    # scorelist = (1, 2, 3, 45, 'W', 3, 4, 5, 6, 'W', 32, 13, 45, 6, 'W')
                    player_batsman = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')

                    player_c = 0
                    count = 1
                    w = 0
                    o = []
                    batsman_scorelist = []
                    batsman_scorelist2 = []

                    while count < bcr - 2:
                        for j in scorelist:
                            if j != 'Wicket':
                                # print(j)
                                o.append(j)
                                # print(o)

                            if j == 'Wicket':
                                p_sum_i = sum(o)
                                batsman_scorelist.append(p_sum_i)

                                # print(q)
                                # print('out')
                                player_c += 1
                                # print('batsman', player_c)

                            if count == bcr - 2:
                                # print('batsman_scorelist',batsman_scorelist)
                                # print(o)
                                p_sum_i = sum(o) + int(c_wide) + int(c_noball)


                                batsman_scorelist.append(p_sum_i)
                                print('sum of team', p_sum_i)
                                print(''
                                      '')

                                for n in range(len(batsman_scorelist)):
                                    k = batsman_scorelist[n] - batsman_scorelist[n - 1]
                                    batsman_scorelist2.append(k)

                                p = batsman_scorelist2
                                p.pop(0)
                                p.insert(0, batsman_scorelist[0])
                                # print(p) #scorelist without wickets

                                keys = player_batsman
                                values = p
                                final_scorelist = dict(zip(keys, values))
                                print('Final scorelist of Batsman', final_scorelist,'\n')

                                method_of_miss = ('Hit Wicket', 'Catch', 'Run Out', 'LBW', 'Stumps', 'WK-Stumped')

                                print('Method of missing', '\n')
                                H = list(final_scorelist.keys())
                                for i in range(len(H)):
                                    l = random.choice(method_of_miss)
                                    print(l)
                                print('\n')

                            count += 1

                    sort_batsman_dict = {k: v for k, v in sorted(final_scorelist.items(), key=lambda v: v[1], reverse=True)}
                    # print(sort_batsman_dict)  #batsman are sorted in descending order of runs

                    best_5_batsman = list(sort_batsman_dict.items())
                    print('Highest run scorers', best_5_batsman[0:5])
                    print(''
                          ''
                          '')

                    f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Batstat.txt", "a")


                    f.write('\n')
                    f.write('NEW MATCH-SECOND INNINGS\n')
                    f.write('Batsman Performnce\n')
                    f.write(str(sort_batsman_dict))
                    f.write('\n')
                    f.write('Best 5 batsman..........\n')
                    f.write(str(best_5_batsman[0:5]))
                    f.write(''
                            '')

                    f.close()

                player_score()

            generateMatch(20)
            Batsman()

        #second_innings()

        if Decision_F == 'Bat':
            generateMatch(20)
            Batsman()

            def Scorelist_baller(list, list_size):
                global g_2
                for i in range(0, len(list), list_size):
                    yield list[i:i + list_size]

            g_2 = (Scorelist_baller(SCORE_LIST_BATSMAN, 30))


            def Baller():
                global m
                baller_stat = []
                baller_stat_wickets = []
                player_baller_1 = ('H', 'I', 'J', 'K')
                player_baller_2 = ('H', 'I', 'J')
                player_baller_3 = ('H', 'I')
                player_baller_4 = ('H')
                m = list(g_2)

                Count_c = [m.count(item) for item in m]
                s = (sum(Count_c))

                # g=list(Scorelist_baller(scorelist,6))
                # keys=random.choice(player_baller)
                if s == 4:
                    # keys=random.choice(player_baller)
                    keys = player_baller_1
                    values = m
                    baller_summary = dict(zip(keys, values))
                    print(''
                          '')
                    print('Baller Summary', baller_summary)
                elif s == 3:
                    keys = player_baller_2
                    values = m
                    baller_summary = dict(zip(keys, values))
                    print(''
                          '')
                    print('Baller Summary', baller_summary)
                elif s == 2:
                    keys = player_baller_3
                    values = m
                    baller_summary = dict(zip(keys, values))
                    print(''
                          '')
                    print('Baller Summary', baller_summary)
                elif s == 1:
                    keys = player_baller_4
                    values = m
                    baller_summary = dict(zip(keys, values))
                    print(''
                          '')
                    print('Baller Summary', baller_summary)

                runs_played_bowler = []
                for i in keys:
                    A = (baller_summary[i])

                    z = []
                    for i in A:
                        if isinstance(i, str):
                            continue

                        if isinstance(i, int):
                            z.append(i)
                            f = sum(z)
                    runs_played_bowler.append(f)

                    # print(f)
                    # print(z)
                print('runs_played_bowler', runs_played_bowler)

                if s == 4:
                    # keys=random.choice(player_baller)
                    keys = player_baller_1
                    values = runs_played_bowler
                    bowl_summary_final = dict(zip(keys, values))
                    print('bowl_summary_final', bowl_summary_final)
                    print(''
                          '')
                elif s == 3:
                    keys = player_baller_2
                    values = runs_played_bowler
                    bowl_summary_final = dict(zip(keys, values))
                    print('bowl_summary_final', bowl_summary_final)
                    print(''
                          '')
                elif s == 2:
                    keys = player_baller_3
                    values = runs_played_bowler
                    bowl_summary_final = dict(zip(keys, values))
                    print('bowl_summary_final', bowl_summary_final)
                    print(''
                          '')
                elif s == 1:
                    keys = player_baller_4
                    values = runs_played_bowler
                    bowl_summary_final = dict(zip(keys, values))
                    print('bowl_summary_final', bowl_summary_final)
                    print(''
                          '')

                if s == 4:
                    www = []
                    index = ['H', 'I', 'J', 'K']
                    for i in index:
                        ww = []
                        for j in baller_summary[i]:
                            if j == 'Wicket':
                                ww.append(j)
                        www.append(ww)
                        # print(i, ww)
                    # print(www)

                elif s == 3:
                    www = []
                    index = ['H', 'I', 'J']
                    for i in index:
                        ww = []
                        for j in baller_summary[i]:
                            if j == 'Wicket':
                                ww.append(j)
                        www.append(ww)
                        # print(i, ww)
                    # print(www)

                elif s == 2:
                    www = []
                    index = ['H', 'I']
                    for i in index:
                        ww = []
                        for j in baller_summary[i]:
                            if j == 'Wicket':
                                ww.append(j)
                        www.append(ww)
                        # print(i, ww)
                    # print(www)

                elif s == 1:
                    www = []
                    index = ['H']
                    for i in index:
                        ww = []
                        for j in baller_summary[i]:
                            if j == 'Wicket':
                                ww.append(j)
                        www.append(ww)
                    # print(i, ww)
                # print(www)

                print(''
                      '')

                if s == 4:
                    # keys=random.choice(player_baller)
                    keys = player_baller_1
                    values = www
                    wicket_summary = dict(zip(keys, values))
                    print('wicket_summary', wicket_summary)
                elif s == 3:
                    keys = player_baller_2
                    values = www
                    wicket_summary = dict(zip(keys, values))
                    print('wicket_summary', wicket_summary)
                elif s == 2:
                    keys = player_baller_3
                    values = www
                    wicket_summary = dict(zip(keys, values))
                    print('wicket_summary', wicket_summary)
                elif s == 1:
                    keys = player_baller_4
                    values = www
                    wicket_summary = dict(zip(keys, values))
                    print('wicket_summary', wicket_summary)

                sortedval = {k: v for k, v in sorted(wicket_summary.items(), key=lambda v: v[1], reverse=True)}
                print('Highset wicket takers: ', sortedval)

                f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Bowlstat.txt", "a")


                f.write('\n')
                f.write('BOWL FIRST INNINGS')
                f.write('Bowler performance\n')
                f.write(str(bowl_summary_final))
                f.write('\n')
                f.write('Highest Wicket Takers\n')
                f.write(str(sortedval))
                f.write(''
                        '')


                f.close()

            Baller()

            if Decision_F_other == 'Bowl':
                print(''
                      '')

                second_innings()


                def Scorelist_baller(list, list_size):
                    global g_2
                    for i in range(0, len(list), list_size):
                        yield list[i:i + list_size]

                g_2_2 = (Scorelist_baller(SCORE_LIST_BATSMAN_2, 30))

                def Baller():
                    global m
                    baller_stat = []
                    baller_stat_wickets = []
                    player_baller_1 = ('H', 'I', 'J', 'K')
                    player_baller_2 = ('H', 'I', 'J')
                    player_baller_3 = ('H', 'I')
                    player_baller_4 = ('H')
                    m = list(g_2_2)

                    Count_c = [m.count(item) for item in m]
                    s = (sum(Count_c))

                    # g=list(Scorelist_baller(scorelist,6))
                    # keys=random.choice(player_baller)

                    if s == 4:
                        # keys=random.choice(player_baller)
                        keys = player_baller_1
                        values = m
                        baller_summary = dict(zip(keys, values))
                        print(''
                              '')
                        print('Baller Summary', baller_summary)
                    elif s == 3:
                        keys = player_baller_2
                        values = m
                        baller_summary = dict(zip(keys, values))
                        print(''
                              '')
                        print('Baller Summary', baller_summary)
                    elif s == 2:
                        keys = player_baller_3
                        values = m
                        baller_summary = dict(zip(keys, values))
                        print(''
                              '')
                        print('Baller Summary', baller_summary)
                    elif s == 1:
                        keys = player_baller_4
                        values = m
                        baller_summary = dict(zip(keys, values))
                        print(''
                              '')
                        print('Baller Summary', baller_summary)


                    runs_played_bowler = []
                    for i in keys:
                        A = (baller_summary[i])

                        z = []
                        for i in A:
                            if isinstance(i, str):
                                continue

                            if isinstance(i, int):
                                z.append(i)
                                f = sum(z)
                        runs_played_bowler.append(f)

                        # print(f)
                        # print(z)
                    print('runs_played_bowler', runs_played_bowler)

                    if s == 4:
                        # keys=random.choice(player_baller)
                        keys = player_baller_1
                        values = runs_played_bowler
                        bowl_summary_final = dict(zip(keys, values))
                        print('bowl_summary_final', bowl_summary_final)
                        print(''
                              '')
                    elif s == 3:
                        keys = player_baller_2
                        values = runs_played_bowler
                        bowl_summary_final = dict(zip(keys, values))
                        print('bowl_summary_final', bowl_summary_final)
                        print(''
                              '')
                    elif s == 2:
                        keys = player_baller_3
                        values = runs_played_bowler
                        bowl_summary_final = dict(zip(keys, values))
                        print('bowl_summary_final', bowl_summary_final)
                        print(''
                              '')
                    elif s == 1:
                        keys = player_baller_4
                        values = runs_played_bowler
                        bowl_summary_final = dict(zip(keys, values))
                        print('bowl_summary_final', bowl_summary_final)
                        print(''
                              '')

                    if s == 4:
                        www = []
                        index = ['H', 'I', 'J', 'K']
                        for i in index:
                            ww = []
                            for j in baller_summary[i]:
                                if j == 'Wicket':
                                    ww.append(j)
                            www.append(ww)
                            # print(i, ww)
                        # print(www)

                    elif s == 3:
                        www = []
                        index = ['H', 'I', 'J']
                        for i in index:
                            ww = []
                            for j in baller_summary[i]:
                                if j == 'Wicket':
                                    ww.append(j)
                            www.append(ww)
                            # print(i, ww)
                        # print(www)

                    elif s == 2:
                        www = []
                        index = ['H', 'I']
                        for i in index:
                            ww = []
                            for j in baller_summary[i]:
                                if j == 'Wicket':
                                    ww.append(j)
                            www.append(ww)
                            # print(i, ww)
                        # print(www)

                    elif s == 1:
                        www = []
                        index = ['H']
                        for i in index:
                            ww = []
                            for j in baller_summary[i]:
                                if j == 'Wicket':
                                    ww.append(j)
                            www.append(ww)
                        # print(i, ww)
                    # print(www)

                    print(''
                          '')

                    if s == 4:
                        # keys=random.choice(player_baller)
                        keys = player_baller_1
                        values = www
                        wicket_summary = dict(zip(keys, values))
                        print('wicket_summary', wicket_summary)
                    elif s == 3:
                        keys = player_baller_2
                        values = www
                        wicket_summary = dict(zip(keys, values))
                        print('wicket_summary', wicket_summary)
                    elif s == 2:
                        keys = player_baller_3
                        values = www
                        wicket_summary = dict(zip(keys, values))
                        print('wicket_summary', wicket_summary)
                    elif s == 1:
                        keys = player_baller_4
                        values = www
                        wicket_summary = dict(zip(keys, values))
                        print('wicket_summary', wicket_summary)

                    sortedval = {k: v for k, v in sorted(wicket_summary.items(), key=lambda v: v[1], reverse=True)}
                    print('Highset wicket takers: ', sortedval)

                    f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\Bowlstat.txt", "a")


                    f.write('\n')
                    f.write('BOWL SECOND INNINGS')
                    f.write('Bowler Summary\n')
                    f.write(str(bowl_summary_final))
                    f.write('\n')
                    f.write('Highest Wicket Takers\n')
                    f.write(str(sortedval))
                    f.write(''
                            '')

                    f.close()

                Baller()

                Tournament_W = []
                Tournament_L = []
                Tournament_D = []

                R=f'{TL}'
                R_1=f'{TW}'

                if p_sum_i > total:
                    v_1=f'{TL}' + ' ' + 'WON THE MATCH'
                    Tournament_L.append(R_1)
                    Tournament_W.append(R)
                    print('\n')
                    print(v_1,'\n')
                    print('Tournament Summary','\n')

                elif p_sum_i < total:
                    v_2=f'{TW}' + ' ' + 'WON THE MATCH'
                    Tournament_L.append(R)
                    Tournament_W.append(R_1)
                    print('\n')
                    print(v_2,'\n')
                    print('Tournament Summary','\n')

                elif p_sum_i == total:
                    Tournament_D.append(R)
                    Tournament_D.append(R_1)
                    print('\n')
                    print('MATCH DRAW','\n')
                    print('Tournament Summary','\n')


        #print(Tournament_L)
        #print(Tournament_W)
        #print(Tournament_D)
except NameError:
    print("Your input is wrong.Enter 'Y' for YES or enter 'N' for NO as required or else if Group Name to be entered, Enter as A or B")

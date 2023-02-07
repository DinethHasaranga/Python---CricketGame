import LAST

try:
    for i in LAST.Tournament_W:
        if i == 'SRI LANKA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Sri lanka.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'AUSTRALIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Australia.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'BANGLADESH':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Bangladesh.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'WEST INDIES':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Westindies.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'INDIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\India.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'PAKISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Pakistan.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'AFGHANISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Afghanistan.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()
        if i == 'ENGLAND':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\England.txt", "a")
            f.write('\n')
            f.write('won')
            f.close()

    for i in LAST.Tournament_L:
        if i == 'SRI LANKA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Sri lanka.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'AUSTRALIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Australia.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'BANGLADESH':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Bangladesh.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'WEST INDIES':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Westindies.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'INDIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\India.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'PAKISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Pakistan.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'AFGHANISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Afghanistan.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
        if i == 'ENGLAND':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\England.txt", "a")
            f.write('\n')
            f.write('loss')
            f.close()
    for i in LAST.Tournament_D:
        if i == 'SRI LANKA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Sri lanka.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'AUSTRALIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Australia.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'BANGLADESH':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Bangladesh.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'WEST INDIES':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Westindies.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'INDIA':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\India.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'PAKISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Pakistan.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'AFGHANISTAN':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Afghanistan.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()
        if i == 'ENGLAND':
            f = open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\England.txt", "a")
            f.write('\n')
            f.write('draw')
            f.close()



    a=[]
    b=[]

    try:
        WSL = []
        LSL = []
        DSL = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Sri lanka.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                #print(stripped_line)
                if stripped_line == 'loss':
                    LSL.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WSL.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    WSL.append(stripped_line)
                    continue

            #print(LSL)
            #print(WSL)
            C_SL_L = len(LSL)
            C_SL_W = len(WSL)
            C_SL_D = len(DSL)
            T_M_P_SL = int(C_SL_L) + int(C_SL_W) + int(C_SL_D)
            Win_percentage_SL = (int(C_SL_W)/T_M_P_SL)*100

            print('SRI LANKA')
            print('No of matches Loss: ',   C_SL_L)
            print('No of matches Won: ',    C_SL_W)
            print('No of matches Draw: ',   C_SL_D)
            print('Total matches played: ', T_M_P_SL )
            print('Win Percentage: ',       Win_percentage_SL,'\n')
            a.append(C_SL_W)

    except ZeroDivisionError:
        print("Sri Lanka didn't play a match yet\n")

    try:
        WA = []
        LA = []
        DA = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Australia.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                #print(stripped_line)
                if stripped_line == 'loss':
                    LA.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WA.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DA.append(stripped_line)
                    continue

            #print(LA)
            #print(WA)
            C_A_L = len(LA)
            C_A_W = len(WA)
            C_A_D = len(DA)
            T_M_P_A = int(C_A_L) + int(C_A_W) + int(C_A_D)
            Win_percentage_A = (int(C_A_W)/T_M_P_A)*100

            print('AUSTRALIA')
            print('No of matches Loss: ',   C_A_L)
            print('No of matches Won: ',    C_A_W)
            print('No of matches Draw: ',   C_A_D)
            print('Total matches played: ', T_M_P_A )
            print('Win Percentage: ',       Win_percentage_A,'\n')
            a.append(C_A_W)

    except ZeroDivisionError:
        print("Australia didn't play a match yet\n")


    try:
        WB = []
        LB = []
        DB = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Bangladesh.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                #print(stripped_line)
                if stripped_line == 'loss':
                    LB.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WB.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DB.append(stripped_line)
                    continue

            #print(LA)
            #print(WA)
            C_B_L = len(LB)
            C_B_W = len(WB)
            C_B_D = len(DB)
            T_M_P_B = int(C_B_L) + int(C_B_W) + int(C_B_D)
            Win_percentage_B = (int(C_B_W)/T_M_P_B)*100

            print('BANGLADESH')
            print('No of matches Loss: ',   C_B_L)
            print('No of matches Won: ',    C_B_W)
            print('No of matches Draw: ',   C_B_D)
            print('Total matches played: ', T_M_P_B )
            print('Win Percentage: ',       Win_percentage_B,'\n')
            a.append(C_B_W)

    except ZeroDivisionError:
        print("Bangladesh didn't play a match yet\n")

    try:
        WWI = []
        LWI = []
        DWI = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Westindies.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line == 'loss':
                    LWI.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WWI.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DWI.append(stripped_line)
                    continue

            # print(LA)
            # print(WA)
            C_WI_L = len(LWI)
            C_WI_W = len(WWI)
            C_WI_D = len(DWI)

            T_M_P_WI = int(C_WI_L) + int(C_WI_W) + int(C_WI_D)
            Win_percentage_WI = (int(C_WI_W) / T_M_P_WI) * 100
            print('WEST INDIES')
            print('No of matches Loss: ',   C_WI_L)
            print('No of matches Won: ',    C_WI_W)
            print('No of matches Won: ',    C_WI_D)
            print('Total matches played: ', T_M_P_WI)
            print('Win Percentage: ',       Win_percentage_WI, '\n')
            a.append(C_WI_W)

    except ZeroDivisionError:
        print("West Indies didn't play a match yet\n")


    try:
        WI = []
        LI = []
        DI = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\India.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line == 'loss':
                    LI.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WI.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DI.append(stripped_line)
                    continue

            # print(LA)
            # print(WA)
            C_I_L = len(LI)
            C_I_W = len(WI)
            C_I_D = len(DI)
            T_M_P_I = int(C_I_L) + int(C_I_W) + int(C_I_D)
            Win_percentage_I = (int(C_I_W) / T_M_P_I) * 100

            print('INDIA')
            print('No of matches Loss: ',   C_I_L)
            print('No of matches Won: ',    C_I_W)
            print('No of matches Draw: ',   C_I_D)
            print('Total matches played: ', T_M_P_I)
            print('Win Percentage: ',       Win_percentage_I, '\n')
            b.append(C_I_W)

    except ZeroDivisionError:
        print("India didn't play a match yet\n")


    try:
        WP = []
        LP = []
        DP=[]

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Pakistan.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line == 'loss':
                    LP.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WP.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DP.append(stripped_line)
                    continue

            # print(LA)
            # print(WA)
            C_P_L = len(LP)
            C_P_W = len(WP)
            C_P_D = len(DP)
            T_M_P_P = int(C_P_L) + int(C_P_W) + int(C_P_D)
            Win_percentage_P = (int(C_P_W) / T_M_P_P) * 100

            print('PAKISTAN')
            print('No of matches Loss: ',   C_P_L)
            print('No of matches Won: ',    C_P_W)
            print('No of matches Draw: ',   C_P_D)
            print('Total matches played: ', T_M_P_P)
            print('Win Percentage: ',       Win_percentage_P, '\n')
            b.append(C_P_W)

    except ZeroDivisionError:
        print("Pakistan didn't play a match yet\n")


    try:
        WAF = []
        LAF = []
        DAF = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\Afghanistan.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line == 'loss':
                    LAF.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WAF.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DAF.append(stripped_line)
                    continue

            # print(LA)
            # print(WA)
            C_AF_L = len(LAF)
            C_AF_W = len(WAF)
            C_AF_D = len(DAF)
            T_M_P_AF = int(C_AF_L) + int(C_AF_W) + int(C_AF_D)
            Win_percentage_AF = (int(C_AF_W) / T_M_P_AF) * 100

            print('AFGHANISTAN')
            print('No of matches Loss: ',   C_AF_L)
            print('No of matches Won: ',    C_AF_W)
            print('No of matches Draw: ',   C_AF_D)
            print('Total matches played: ', T_M_P_AF)
            print('Win Percentage: ',       Win_percentage_AF, '\n')
            b.append(C_AF_W)

    except ZeroDivisionError:
        print("Afghanistan didn't play a match yet\n")


    try:
        WE = []
        LE = []
        DE = []

        with open("C:\\Users\\Dineth\\DINETH\\Desktop\\PROG CW\\prog cw final cricket\\Files\\win loss\\England.txt",'r') as f:
            for line in f:
                stripped_line = line.strip()
                # print(stripped_line)
                if stripped_line == 'loss':
                    LE.append(stripped_line)
                    continue

                elif stripped_line == 'won':
                    WE.append(stripped_line)
                    continue

                elif stripped_line == 'draw':
                    DE.append(stripped_line)
                    continue

            # print(LA)
            # print(WA)
            C_E_L = len(LE)
            C_E_W = len(WE)
            C_E_D = len(DE)
            T_M_P_E = int(C_E_L) + int(C_E_W) + int(C_E_D)
            Win_percentage_E = (int(C_E_W) / T_M_P_E) * 100

            print('ENGLAND')
            print('No of matches Loss: ',   C_E_L)
            print('No of matches Won: ',    C_E_W)
            print('No of matches Draw: ',   C_E_D)
            print('Total matches played: ', T_M_P_E)
            print('Win Percentage: ',       Win_percentage_E, '\n')
            b.append(C_E_W)

    except ZeroDivisionError:
        print("England didn't play a match yet\n")


    country_A = ['SRI LANKA', 'AUSTRALIA', 'BANGLADESH', 'WEST INDIES']
    country_B = ['INDIA', 'PAKISTAN', 'AFGHANISTAN', 'ENGLAND']

    c_a=dict(zip(country_A,a))
    c_b=dict(zip(country_B,b))

    #print(c)

    sort_c_a = sorted(c_a.items(),key=lambda x:x[1],reverse=True)
    sort_c_b = sorted(c_b.items(), key=lambda x: x[1], reverse=True)

    print('Tournament Standings of Group A', '\n')
    for i in sort_c_a:
        print(i[0])

    print(' '
          ' ')

    print('Tournament Standings of Group B', '\n')
    for i in sort_c_b:
        print(i[0])

except AttributeError:
    print('Enter A or B')
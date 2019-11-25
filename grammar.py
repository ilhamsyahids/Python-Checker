Dict = {}
listTerminal = ['a','b','c']

def ReadFromFile(namaFile):
    with open(namaFile) as cfg:
        lines = cfg.readlines()
    res = [i.strip().replace('->', '').split() for i in lines]
    resBaru = []
    temp = []
    for i in range(len(res)):
        if (res[i]=='|'):
            resBaru.append(temp)
            temp = []
        else:
            temp.append(res)
    for i in range(len(res)):
        key = res[i][0]
        Dict[key] = res[i][1:]


def eliminateTerminalwithNonTerminalRHS():
    listKey = [k for k in Dict]
    for posK in range(len(listKey)):
        k = listKey[posK]
        i = 0
        while(i<len(Dict[k])):
            isExistTerminal = False
            isExistNonTerminal = False
            for j in range(i,len(Dict[k])):
                if ((Dict[k][j] == "|") or (j==len(Dict[k])-1)):
                    if(isExistNonTerminal and isExistTerminal):
                        for pos in range(i,j):
                            if (Dict[k][pos] in listTerminal):
                                Dict[k][pos] = "-"+Dict[k][pos]+"-"
                                Dict["-"+Dict[k][pos]+"-"] = [Dict[k][pos]]
                    i = j+1
                    break
                elif (Dict[k][j] in listTerminal):
                    isExistTerminal = True
                else:
                    isExistNonTerminal = True

            if(isExistNonTerminal and isExistTerminal):
                for pos in range(i,len(Dict[k])):
                    if (Dict[k][pos] in listTerminal):
                        Dict[k][pos] = "-"+Dict[k][pos]+"-"
                        Dict["-"+Dict[k][pos]+"-"] = [Dict[k][pos]]


def eliminateMoreTwoNonTerminalRHS():
    listKey = [k for k in Dict]
    # print(listKey)
    for posK in range(len(listKey)):
        k = listKey[posK]
        temp = []
        newProduction = []
        for i in range(len(Dict[k])):
            if (Dict[k][i]=='|'):
                if (len(temp) > 2):
                    isProses = True
                    j = len(temp)-1
                    while(isProses):
                        if (j == 1):
                            isProses = False
                        else:
                            str1 = temp[j]
                            str2 = temp[j-1]
                            temp.pop()
                            temp.pop()
                            temp.append(str2+"_"+str1)
                            Dict[str2+"_"+str1] = [str2, str1]
                            j = j-1
                
                
                newProduction = newProduction + temp
                newProduction.append("|")
                temp = []

            else:
                temp.append(Dict[k][i])

        # last part
        if (len(temp) > 2):
            isProses = True
            j = len(temp)-1
            while(isProses):
                if (j == 1):
                    isProses = False
                else:
                    str1 = temp[j]
                    str2 = temp[j-1]
                    temp.pop()
                    temp.pop()
                    temp.append(str2+"_"+str1)
                    Dict[str2+"_"+str1] = [str2, str1]
                    j = j-1

            newProduction = newProduction + temp
            temp = []
        else:
            newProduction = newProduction + temp
            temp = []
        
        Dict[k] = newProduction
                        
def changeFormat():
    listKey = [k for k in Dict]
    for posK in range(len(listKey)):
        k = listKey[posK]
        newRes = []
        temp = []
        for e in Dict[k]:
            if (e=='|'):
                newRes.append(temp)
                temp = []
            else:
                temp.append(e)
        newRes.append(temp)
        Dict[k] = newRes


# ReadFromFile("test.txt")
# print(Dict)
# eliminateTerminalwithNonTerminalRHS()
# print(Dict)
# eliminateMoreTwoNonTerminalRHS()
# print(Dict)
# changeFormat()
# print(Dict)

def makeRule(file):
    ReadFromFile(file)
    eliminateTerminalwithNonTerminalRHS()
    eliminateMoreTwoNonTerminalRHS()
    changeFormat()
    return Dict

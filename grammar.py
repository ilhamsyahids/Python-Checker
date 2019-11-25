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
        if (len(Dict[k])>1):
            isExistTerminal = False
            isExistNonTerminal = False
            for i in range(len(Dict[k])):
                if (Dict[k][i] in listTerminal):
                    isExistTerminal = True
                else:
                    isExistNonTerminal = True
            if (isExistTerminal and isExistNonTerminal):
                for i in range(len(Dict[k])):
                    if (Dict[k][i] in listTerminal):
                        x = Dict[k][i]
                        Dict[k][i] = "-"+x+"-"
                        Dict["-"+x+"-"] = [x]


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


ReadFromFile("test.txt")
print(Dict)
eliminateTerminalwithNonTerminalRHS()
print(Dict)
eliminateMoreTwoNonTerminalRHS()
print(Dict)
changeFormat()
print(Dict)

def makeRule(file):
    ReadFromFile(file)
    eliminateTerminalwithNonTerminalRHS()
    eliminateMoreTwoNonTerminalRHS()
    changeFormat()
    return Dict

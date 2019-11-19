Dict = {}


def ReadFromFile(namaFile):
    with open(namaFile) as cfg:
        lines = cfg.readlines()
    res = [i.strip().replace('->', '').split() for i in lines]
    for i in range(len(res)-1):
        key = res[i][0]
        Dict[key] = res[i][1:]
    return res


def eliminateTerminalRHS():
    print('tes')
    for k in Dict:
        temp = Dict[k]

    for k in Dict:
        for production in Dict[k]:
            temp = [x.split() for x in production]
            if (len(temp) > 2):
                isProses = True
                i = len(temp)-1
                while(isProses):
                    if (i == 1):
                        isProses = False
                    else:
                        str1 = temp[i]
                        str2 = temp[i-1]
                        Dict[k].pop()
                        Dict[k].pop()
                        Dict[k].append(str1+str2)
                        Dict[str1+str2] = [str1, str2]


ReadFromFile("grammar.txt")
# eliminateTerminalRHS()
print(Dict)

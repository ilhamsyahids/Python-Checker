import grammar

terminalInput = ['a', 'a', 'b', 'b']  # dari input .txt
banyakTerminal = len(terminalInput)
rule = grammar.makeRule('test.txt')
tabel = [[[] for j in range(banyakTerminal)] for i in range(banyakTerminal)]
dp = {}


def nonTerminalOf(X):
    resNonTerminal = []
    for key, val in rule.items():
        if (X in val):
            resNonTerminal.append(key)
    return resNonTerminal


def searchTerminal(X):
    res = []
    # print("cok",X)
    for key, lol in rule.items():
        # print(key,lol)
        if X in lol:
            # print('mantap',X,key)
            res.append(key)
    return res


def makeIsi(pos1,pos2):
    # print('(',pos1[0],pos1[1],') (',pos2[0],pos2[1],')')
    res = []
    for val1 in tabel[pos1[0]][pos1[1]]:
        for val2 in tabel[pos2[0]][pos2[1]]:
            if (val1==[] or val2==[]): 
                continue
            temp = (val1,val2)
            if (temp in dp):
                temp = dp[temp]
            else:
                temp = searchTerminal([val1,val2])
                dp[(val1,val2)] = temp
            if (temp!=[]):
                res += temp
    return res


def cyk():
    print('Ini soal')
    for j in range(banyakTerminal):
        tabel[0][j] = nonTerminalOf([terminalInput[j]])
        print(tabel[0][j],end=' ')
    print()

    for row in range(1, banyakTerminal):
        for col in range(banyakTerminal-row):
            # print(row,' ',col,':',end=' ')
            for r in range(row-1,-1,-1):
                pos1 = (r,col)
                pos2 = (row-r-1,r+col+1)
                temp = makeIsi(pos1,pos2)
                if not(temp in tabel[row][col]):
                    tabel[row][col]+=temp
            tabel[row][col] = list(dict.fromkeys(tabel[row][col]))

def printTabel():
    for row in range(banyakTerminal-1,-1,-1):
        for col in range(0,banyakTerminal-row):
            print(tabel[row][col],end=' ')
        print()

if __name__ == "__main__":    
    print('Ini rule')
    print(rule)
    cyk()
    print('\nIni hasil')
    printTabel()
    if ('S' in tabel[banyakTerminal-1][0]):
        print('Accepted')
    else:
        print('Error')
import grammar

terminalInput = ['a', 'a', 'b', 'b']  # dari input .txt
banyakTerminal = len(terminalInput)
rule = grammar.makeRule('coba.txt')
tabel = [[[] for j in range(banyakTerminal)] for i in range(banyakTerminal)]


def nonTerminalOf(X):
    for key, val in rule.items():
        if (val == [X]):
            return key
    return X


def searchTerminal(X):
    for key, val in rule.items():
        if (val == X):
            return key
    return None


def makeIsi(pos1, pos2):
    res = []
    for val1 in tabel[pos1[0]][pos1[1]]:
        for val2 in tabel[pos2[0]][pos2[1]]:
            temp = [val1, val2]
            temp = searchTerminal([val1, val2])
            if (temp != None):
                res.append(temp)
    return res


def cyk():
    print('Ini soal')
    for j in range(banyakTerminal):
        tabel[0][j].append(nonTerminalOf(terminalInput[j]))
        print(tabel[0][j], end=' ')
    print()

    for row in range(1, banyakTerminal):
        for col in range(banyakTerminal-row):
            print(row, ' ', col, ':', end=' ')
            for r in range(row-1, -1, -1):
                pos1 = (r, col)
                pos2 = (row-r-1, r+col+1)
                tabel[row][col] += makeIsi(pos1, pos2)
            print(tabel[row][col])


print('Ini rule')
print(rule)
cyk()

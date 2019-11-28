import grammar
import readFile

dp = {}


def nonTerminalOf(X):
    # mencari nonterminal dari suatu terminal input
    if (X[0][0] >= '0' and X[0][0] <= '9'):
        return nonTerminalOf(['number'])
    resNonTerminal = []
    for key, val in rule.items():
        if (X in val):
            resNonTerminal.append(key)
    if (resNonTerminal == []):
        return nonTerminalOf(['object'])
    else:
        return resNonTerminal


def searchNonTerminal(X):
    # mencari nonterminal dari suatu nonterminal
    res = []
    for key, lol in rule.items():
        if X in lol:
            res.append(key)
    return res


def makeIsi(pos1, pos2):
    # mengembalikan list nonterminal hasil penggabungan 2 sel
    res = []
    for val1 in tabel[pos1[0]][pos1[1]]:
        for val2 in tabel[pos2[0]][pos2[1]]:
            if (val1 == [] or val2 == []):
                continue
            temp = (val1, val2)
            if (temp in dp):
                temp = dp[temp]
            else:
                temp = searchNonTerminal([val1, val2])
                dp[(val1, val2)] = temp
            if (temp != []):
                res += temp
    return res


def cyk():
    # Mencari nonterminal yang menghasilkan terminal input
    for j in range(banyakTerminal):
        tabel[0][j] = nonTerminalOf([terminalInput[j]])

    for row in range(1, banyakTerminal):
        for col in range(banyakTerminal-row):
            for r in range(row-1, -1, -1):
                pos1 = (r, col)
                pos2 = (row-r-1, r+col+1)
                # Mencari hasil tabel[row][col]
                temp = makeIsi(pos1, pos2)
                if not(temp in tabel[row][col]):
                    tabel[row][col] += temp
            tabel[row][col] = list(dict.fromkeys(tabel[row][col]))


# def printTabel():
#     for row in range(banyakTerminal-1, -1, -1):
#         for col in range(0, banyakTerminal-row):
#             print(tabel[row][col], end=' ')
#         print()


def python_checker():
    global terminalInput, banyakTerminal, tabel, rule

    namaFile = input('Masukkan nama file: ')
    terminalInput = readFile.inputFromText(namaFile)
    banyakTerminal = len(terminalInput)

    rule = grammar.makeRule('grammarcoba.txt')  # file grammar
    tabel = [[[] for j in range(banyakTerminal)]
             for i in range(banyakTerminal)]

    cyk()

    # printTabel()
    if ('S' in tabel[banyakTerminal-1][0]):
        print('Accepted')
    else:
        print('Syntax Error')


if __name__ == "__main__":
    python_checker()

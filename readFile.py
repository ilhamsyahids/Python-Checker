def inputFromText(namaFile):
    fin = open(namaFile)
    terminal = getTerminal('terminal.txt')
    hasil = []
    for line in fin.readlines():
        temp = ""
        line = line.strip()
        print(line)
        isNumber = False
        for cc in line:
            if (cc == " " or (isNumber and (cc < '0' or cc > '9'))):
                if (isNumber):
                    isNumber = False
                if (temp != ""):
                    hasil.append(temp)
                if (cc == " "):
                    temp = ""
                else:
                    temp = cc
            elif (cc in terminal):
                if (temp != ""):
                    hasil.append(temp)
                hasil.append(cc)
                temp = ""
            else:
                if (not isNumber and (cc >= '0' and cc <= '9') and temp == ""):
                    isNumber = True
                temp = temp + cc
        if (temp != ""):
            hasil.append(temp)
        hasil.append('\\n')
    hasil.pop()
    return hasil


def getTerminal(namaFile):
    fin = open(namaFile)
    allTerminals = []
    for line in fin.readlines():
        line = line.strip()
        allTerminals.append(line)
    # print(allTerminals)
    return allTerminals


if __name__ == "__main__":
    print(inputFromText('coba.txt'))

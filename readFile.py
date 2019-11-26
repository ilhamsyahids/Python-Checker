def inputFromText(namaFile):
    fin = open(namaFile)
    terminal = ["def","(",")",":","'"] # getTerm?inal()
    hasil = []
    temp = ""
    for line in fin.readlines():
        line = line.strip()
        for cc in line:
            if (cc==" "):
                hasil.append(temp)
                temp = ""
            elif (cc in terminal):
                if (temp!=""):
                    hasil.append(temp)
                hasil.append(cc)
                temp = ""
            else:
                temp = temp + cc
        if (temp!=""):
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
    print(allTerminals)
    return allTerminals


if __name__ == "__main__":
    # inputFromText('haha')
    getTerminal("terminal.txt")
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
        hasil.append('\n')
    return hasil
        

if __name__ == "__main__":
    inputFromText('haha')
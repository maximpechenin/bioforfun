def mut(fname):
    fr = open(fname,'r')
    fw = open('txt.txt','w')
    data = fr.read().split('\n')
    i = 0
    print(data)
    print(len(data[0]))
    print(len(data[1]))
    for t in range(0,len(data[0])):
        if data[0][t]!=data[1][t]:
            i=i+1
    fw.write(str(i))
    fw.close()
    fr.close()

def dnarna(fname):
    fr=open(fname,'r')
    fw=open('t.txt','w')
    x=list(fr.read())
    for i in range(0,len(x)):
        if (x[i]=='T'):
            x[i]='U'
        fw.write(x[i])
    fr.close()
    fw.close()

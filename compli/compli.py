def compli(fname):
    fr = open(fname,'r')
    fw = open('t.txt','w')
    x = fr.read().rstrip()
    l = [None]*len(x)
    for i in range(0,len(x)):
        if x[i]=='A': l[len(x)-1-i]='T'
        elif x[i]=='C': l[len(x)-1-i]='G'
        elif x[i]=='G': l[len(x)-1-i]='C'
        elif x[i]=='T': l[len(x)-1-i]='A'
    l=''.join(l)
    fw.write(l)
    fr.close()
    fw.close()

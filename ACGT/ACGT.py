def acgt(fname):
    f = open(fname,'r')
    x=f.read().rstrip()
    xx=set(x)
    d={}
    for let in xx:
        d[let]=x.count(let)
    f.close()
    f=open('file.txt','w')
    l=list(d.keys())
    l.sort()
    for key in l:
        f.write(str(d[key])+' '+str(key)+'\n')
    f.close()
    

import math

def gc(fname):
    fr = open(fname,'r')
    fw = open('txt.txt','w')
    x={}
    for line in fr:
        line.splitlines()
        if line[0]=='>':
            x[line[1:-1]]=''
            tmp=line[1:-1]
        elif line[0]=='A' or line[0]=='C' or line[0]=='G' or line[0]=='T':
            x[tmp]=x[tmp]+line[:-1]       
    for key,value in x.items():
        x[key] = gcstr(value)    
    maxval=max(x.values())
    z = dict([max(x.items(), key=lambda k_v: k_v[1])])
    d = []
    [d.extend([k,v]) for k,v in z.items()]
    fw.write(str(d[0]))
    fw.write(' ')
    fw.write(str(d[1]))
    fw.write('%')
    fr.close()
    fw.close()
    
def gcstr(x):
    t = 0
    for i in range(0,len(x)):
        if x[i]=='C' or x[i]=='G':
            t=t+1
    res = 100*t/len(x)
    return res

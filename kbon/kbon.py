def kbonwith(fname):
    fr = open(fname,'r')
    fw = open('txt.txt','w')
    x = fr.read().split(' ')
    n = int(x[0])
    k = int(x[1]) #данные в формате 'n k'
    print n,k,'n+k=',n+k
    fw.write(str( kbon(n,k) ))
    fr.close()
    fw.close()
def kbon(n,k):
    if (n==1 or n==2): return 1
    elif n==0: return 0
    else: return kbon(n-1,k)+k*kbon(n-2,k)

def fwith(fname):
    fr = open(fname,'r')
    fw = open('txt.txt','w')
    x = fr.read().split(' ')
    n = int(x[0])
    m = int(x[1])
    print (n,m)
    fw.write(str( f(n,m) ))
    fr.close()
    fw.close()
def f(n, k):
    s = [0] * (k + 1)
    s[0] = 1           # [1, 0, 0, 0]
    for x in range(1, n):
        s[1:k + 1] = s[0:k]
        print (s)
        s[0] = sum(s[2:])
    return sum(s[:-1])


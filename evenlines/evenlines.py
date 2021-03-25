def evenlines(fname):
    fr= open(fname,'r')
    fw= open('txt.txt','w')
    i=1
    for line in fr:
        if i%2==0 :
            fw.write(line)
        i+=1

def hmw(fname):
    f = open(fname,'r')
    fw = open('txt.txt','w')
    st=(f.read()).split(' ')
    f.close()
    st1=set(st)
    d={}
    for word in st1:
        d[word]=st.count(word)
    for key, value in d.items():
         fw.write(key+' '+str(value)+'\n')
    

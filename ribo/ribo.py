def ribo(fname):
    fr = open(fname,'r')
    fa = open('aminos','r')
    fw = open('txt.txt','w')
    rna = fr.read()
    fr.close()   
    protein = ''
    
    aminos = {}
    for line in fa:
        line = line.split(' ')
        aminos[line[0]]=line[1].rstrip()
    fa.close()

    i = 0
    while(i+3<=len(rna)):
        for key in aminos:
            if rna[i]==key[0]:
                if rna[i+1]==key[1]:
                    if rna[i+2]==key[2]:
                        protein+=aminos[key]
        i+=3
    fw.write(protein)
    fw.close()
    




 

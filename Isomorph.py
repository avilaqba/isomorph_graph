import numpy as np

lines = open(r'acetic_acid.mol').readlines()
Nlist = [[],[],[]]
c = 1
Hlist, Blist = [], []
for line in lines:
    if len(line.split()) == 16:
        if line.split()[3] == 'H':
            Hlist.append(c)
        c += 1  
       
for line in lines:
    if len(line.split()) == 7:
        if int(line.split()[1]) not in Hlist:
            Nlist[0].append(int(line.split()[0]))
            Nlist[1].append(int(line.split()[1]))
            Nlist[2].append(int(line.split()[2]))
            Blist.append([int(line.split()[0]),int(line.split()[1])])

Slist = list(set(Nlist[0]+Nlist[1]))

matrix = np.zeros(shape = (len(Slist),len(Slist)))     

for e in range(1,len(Slist)+1):
    for f in range(1,len(Slist)+1):
        if [e,f] in Blist:
            matrix[e-1,f-1] = Nlist[2][Blist.index([e,f])]
            matrix[f-1,e-1] = Nlist[2][Blist.index([e,f])]
        elif [f,e] in Blist:
            matrix[e-1,f-1] = Nlist[2][Blist.index([f,e])]
            matrix[f-1,e-1] = Nlist[2][Blist.index([f,e])]
print '\n        The following are a couple of izomorph matrices\n'			
for m in Slist:
    for n in Slist:
        Nmatrix = matrix
        Nmatrix[[m-1,n-1]] = Nmatrix[[n-1,m-1]]
        Nmatrix[:,[m-1,n-1]] = Nmatrix[:,[n-1,m-1]]
        print Nmatrix,'\n'

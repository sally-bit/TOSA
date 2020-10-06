


import sys
import math

def dhms_to_sec(dhms_str):
    t = dhms_str.split(':')
    return 60*int(t[0])+int(t[1])*1

lines = ['5', '3 12:40-15:01', '5 12:15-14:01', '2 14:09-16:56', '3 13:37-15:35', '3 14:54-17:42']


ContainerJour = []
m= 5
n = 600
ContainerJour = [['.' for x in range(n)] for x in range(m)]
del lines[0]
i=0
while i < len(lines): 
    lines[i] = lines[i].split(" ")
    i+=1 
lundi = ContainerJour[0]
for g in lines:
    if int(g[0])-1 == 1:
        heur = g[1].split('-')
        debut = dhms_to_sec(heur[0])-(8*60)                                                                                
        fin = dhms_to_sec(heur[1])-(8*60)  
        r = debut
        while r  <= fin-1:
            lundi[r]= 1
            r+=1

compt = 0
tabp =[]
date = 0
i=0
while i < 600:
    
    if lundi[i] == '.':
        compt +=1
        if compt >= 60:
            break
    else:
        compt=0
    i+=1
nmBreHeu = 0
nbrMin = 0
if compt == 60:
    nmBreHeu = math.floor(date/60)
    nbrMin = date%60
sep = ':'
Temp = sep.join([str(nmBreHeu), str(nbrMin)])
print(Temp)




    
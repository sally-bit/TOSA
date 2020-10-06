#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import math

def dhms_to_sec(dhms_str):
    t = dhms_str.split(':')
    return 60*int(t[0])+int(t[1])*1

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))




ContainerJour = []
m= 5
n = 600
ContainerJour = [['.' for x in range(n)] for x in range(m)]
del lines[0]
i=0
while i < len(lines): 
    lines[i] = lines[i].split(" ")
    i+=1
print(lines)

for g in lines:
    if int(g[0])-1 == 1:
        lundi = ContainerJour[0]
        heur = g[1].split('-')
        debut = dhms_to_sec(heur[0])-(8*60)                                                                                
        fin = dhms_to_sec(heur[1])-(8*60)  
        r = debut
        while r  <= fin-1:
            lundi[r]= 1
            r+=1
        print(debut)
        print(fin)

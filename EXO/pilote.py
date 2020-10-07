#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))



favori = int(lines[0])
poste=[i for i in range(1,21)]
events = lines[2:]

for ev in events:
    if ev.split(" ")[1] == "I":
        poste.remove(int(ev.split(" ")[0]))
    else:
        ind1 = poste.index(int(ev.split(" ")[0]))
        ind2 = ind1-1
        poste[ind1],poste[ind2] = poste[ind2],poste[ind1]

        
if favori in poste:       
    print((poste.index(favori)+1))
else:
    print("KO")
        
        
"""
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


#print(lines)
c=""
favoris = int(lines[0])
events = lines[2:]
dep=[]
inc=[]
for e in events:
    el1=str((e.split(" "))[1])
    el0=int((e.split(" "))[0])
    if el1== "D":
        dep.append(el0)
    elif el1== "I":
        c=" ".join(e.split(" "))
        inc.append(el0)
        events.remove(c)
#print(dep)
#print(inc)

#liste1=set(post)
#print(liste1)

if (favoris in dep) and (favoris !=0):
    b=favoris
    k=dep.count(favoris)
    favoris = favoris - k
    for i in dep:
        if (b+1)==i:
            favoris+=1
    print(favoris)
elif (favoris in inc) and (favoris !=0):
    print("KO")
elif not(favoris in dep) and not(favoris in inc) :
    for i in inc:
        if favoris > i:
            favoris -= 1
    print(favoris)    

"""
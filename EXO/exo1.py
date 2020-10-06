#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
myliste=list(set(lines[1:]))

tab=[]

for  i in myliste:
    nb=0
    for el in lines[1:]:
        if i == el:
            nb +=1
            
    tab.append(nb)        

tab1= tab.copy()
max1= max(tab1)
index1 =tab.index(max1)

tab1.remove(max1)
max2=max(tab1) 
index2 =tab.index(max2)

print(" ".join([myliste[index1],myliste[index2]]))

    
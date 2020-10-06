#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


unique=list(set(lines[1:]))


tab=[0]

for  i in unique:
    nb=0
    for el in lines[1:]:
        if int(i) == int(el):
            nb +=1
        else:
            tab.append(nb)  
            nb=0
        
    
if max(tab) != 0:
    print(max(tab))
else:
    print(5)
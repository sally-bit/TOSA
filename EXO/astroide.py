import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))


myliste=lines[1:]

lig,col= lines[0].split(" ")
lig,col=int(lig),int(col)


print(lines)
#print("ligne ==>",type(lig),lig)
#print("col==>",type(col),col)
cont=0
t=[]
b=[]

for i in myliste:
    nb=0
    for y in i:
        t.append(y)
        if y == "X":
            nb +=1
    
    b.append(nb)

print(int(sum(b)))
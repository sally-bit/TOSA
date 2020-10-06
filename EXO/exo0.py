lines=['20', '2534 6039', '719 1493', '2853 6764', '5686 7757', '5269 6423', '445 6603', '4301 10347', '2265 7418', '4525 9998', '3661 5449', '2655 8025', '1865 2005', '3488 7169', '8553 9595', '988 9181', '3208 10470', '1273 8947', '7899 8261', '18 10661', '3996 4944']
myliste=[]
count= int(lines[0])
print(type(count),count)

for i in range(1,count):

    nb=1
    var=int(lines[i].split()[-1])
    print("var",var,"+++++++++++")
 
    if i < count:
        for a in lines[i+1:]:
           
            print(a)

            d=int(a.split()[0])
            print("d",d)
            print(" ")
            if d < var :
                nb=nb +1
        myliste.append(nb)        
print(myliste)
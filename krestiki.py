t=False
print('x or o')
while (t==False):
    a= input ('напиши')
    if (a=="x" or a=="0"):
        t==True
        break
    print ('x или 0 введи затупок')
end=2
if (end!=0):
    if (end==1):
        print ('харош')
    if (end==2):
        print ('2 дауна')
    if (end==3):
        print ('лошня')
ogre=0
while (ogre<9):
    for a in range (3):
        print ("-------------")
        string=""
        for i in range (13):
            if (i%4==0):
                string=string+ ("|")
                continue
            if (i%2==1):
                string=string+ (" ")
                continue
            if (i%4==2):
                ogre=ogre+1
                string=string+str(ogre)
        print (string)



        

cot=[]
d1=[]
d2=[]
lst=[]
def inkq():
    for i in range(1,9):
        print(i, lst[i])
    print()
def Try(i):
    for j in range(1,9):
        if cot[j]==1 and d1[i-j+8]==1 and d2[i+j-1]==1:
            cot[j]=d1[i-j+8]=d2[i+j-1]=0
            lst[i]=j
            if(i==8):
                inkq()
            else:
                Try(i+1)
            #back-track
            cot[j]=d1[i-j+8]=d2[i+j-1]=1
for i in range(0,100):
    cot.append(1)
    d1.append(1)
    d2.append(1)
    lst.append(1)
Try(1)

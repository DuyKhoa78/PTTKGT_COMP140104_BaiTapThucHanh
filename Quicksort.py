lst=[int(i) for i in input().split()]
def quickSort(lst, left, right):
    if (left>=right): return
    x=lst[(left+right)//2]
    i=left;j=right
    while(i<j):
        while(lst[i]<x): i+=1
        while(lst[j]>x): j-=1
        if(i<=j):
            lst[i],lst[j]=lst[j],lst[i]
            i+=1;j-=1
    quickSort(lst,left,j)
    quickSort(lst,i,right)
quickSort(lst,0,len(lst)-1)
for i in lst:
    print(i,end=" ")
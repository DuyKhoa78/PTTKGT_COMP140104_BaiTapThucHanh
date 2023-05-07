k,h=[int(i) for i in input("Vị trí con mã: ").split()]
lst=[[]]
X=[-2,-2,-1,-1,1,1,2,2]
Y=[-1,1,-2,2,-2,2,-1,1]
for i in range(0,8):
    x=[]
    for j in range(0,8):
        x.append(0)
    lst+=x
def check(i,j):
    return (i>=0 and i<8 and j>=0 and j<8)

def inkq(lst):
    for i in range(0,8):
        for j in range(0,8):
            print(lst[i][j], end =" ")
def move(dem,x,y,lst,X,Y):
    lst[x][y]=dem
    for i in range(0,8):
        if(dem==8*8):
            print("Các bước đã đi:")
            inkq(lst)
            return
        u=x+X[i]
        v=y+Y[i]
        if(check(u,v) and lst[u][v]==0):
            move(dem+1,u,v,lst,X,Y)
    dem-=1
    lst[x][y]=0

# Khởi tạo bàn cờ
lst = []
for i in range(0,8):
    x=[]
    for j in range(0,8):
        x.append(0)
    lst.append(x)
move(1,k,h,lst,X,Y)

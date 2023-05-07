x=input("X = ")
y=input("Y = ")
n=len(x); m=len(y)
f=[[0 for _ in range(n+2)] for _ in range(m+2)]
for i in range(0,n+1):
    for j in range(0,m+1):
        if(i==0 or j==0):
            f[i][j]=0
        else:
            if(x[i-1]==y[j-1]):
                f[i][j]=f[i-1][j-1]+1
            else:
                f[i][j]=max(f[i-1][j],f[i][j-1])
print(f[n][m])           
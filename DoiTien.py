n,s=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
c.insert(0,0)
f=[[0]*(s+1) for _ in range(n+1)]
print(c)
for i in range(1,s+1):
    f[0][i] = float('inf')
for i in range(1,n+1):
    for j in range(1,s+1):
        f[i][j]=f[i-1][j]
        if j>=c[i]:
            f[i][j]=min(f[i-1][j],f[i][j-c[i]]+1)
print(f[n][s])




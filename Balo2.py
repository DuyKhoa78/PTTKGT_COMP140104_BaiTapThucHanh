n,s=[int(i) for i in input().split()]
lw=[int(i) for i in input().split()]
lv=[int(i) for i in input().split()]
lw.insert(0,0)
lv.insert(0,0)
dp=[[0 for j in range(s+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,s+1):
        #khong lua chon do vat thu i vao trong tui
        dp[i][j]=dp[i-1][j]
        #co the dua do vat thu i vao trong tui
        if j>=lw[i]:
            dp[i][j]=max(dp[i][j],dp[i][j-lw[i]]+lv[i])
print(dp[n][s])
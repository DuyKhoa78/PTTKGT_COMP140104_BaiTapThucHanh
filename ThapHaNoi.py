n=int(input("Nhập n: "))
def Tower(n,a,b,c):
    if n==1:
        print("\t %s ------- %s"%(a,c))
        return
    Tower(n-1,a,c,b)
    Tower(1,a,b,c)
    Tower(n-1,b,a,c)
a="A";b="B";c="C"
Tower(n,a,b,c)
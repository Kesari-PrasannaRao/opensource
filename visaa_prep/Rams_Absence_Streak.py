n=int(input())
a=list(map(int,input().split(" ")))
c,m=0,0
for i in range(n):
    if a[i]==0:
        c=c+1
        if c>m:
            m=c
    else:
        c=0   
print(m)

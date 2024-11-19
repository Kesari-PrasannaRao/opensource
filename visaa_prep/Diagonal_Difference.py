n=int(input())
s1,s2=0,0
a=[]
for i in range(n):
    x=list(map(int,input().split(' ')))
    a.append(x)
for i in range(n):
    for j in range(n):
        if i==j:
            s1=s1+a[i][j]
        if i+j==(n-1):
            s2=s2+a[i][j]
print(abs(s1-s2))
            

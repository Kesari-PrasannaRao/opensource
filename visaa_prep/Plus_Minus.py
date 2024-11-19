k=int(input())
a=list(map(int,input().split(' ')))
n,p,z=0,0,0
for i in a:
    if i<0:
        n=n+1
    elif i>0:
        p=p+1
    else:
        z=z+1
print(p/k)
print(n/k)
print(z/k)

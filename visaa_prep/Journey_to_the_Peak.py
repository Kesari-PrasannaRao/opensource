n=int(input())
a=list(map(int,input().split(' ')))
p=0
m=0
for i in a:
    p=p+i
    if m<p:
        m=p    
print(m)

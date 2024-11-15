import copy
r,c=map(int,input().split(' '))
a=[]
for i in range(r):
    m=list(map(int,input().split(' ')))
    a.append(m)
k=copy.deepcopy(a)
for i in range(r):
    for j in range(c):
        if a[i][j]==1:
            continue
        else:
            for x in range(c):
                k[i][x]=0
            for y in range(r):
                k[y][j]=0
for i in range(r):
    for j in range(c):
        print(k[i][j],end=' ')
    print()
            

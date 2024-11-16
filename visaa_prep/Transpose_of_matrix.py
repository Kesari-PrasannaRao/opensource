n=int(input())
m=[]
for i in range(n):
    a=list(map(int,input().split()))
    m.append(a)
for i in range(n):
    for j in range(n):
        print(m[j][i],end=' ')
    print()

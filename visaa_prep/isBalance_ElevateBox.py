n=int(input())
l=list(map(int,input().split(" ")))
for i in range(n):
    s,s1,s2=0,0,0
    if i==0:
        for j in range(1,n):
            s=s+l[j]
        print(s,end=" ")
    elif i==n-1:
        for j in range(0,n-1):
            s=s+l[j]
        print(s,end=" ")
    else:
        for j in range(0,n):
            if j<i:
                s1=s1+l[j]
            elif j>i:
                s2=s2+l[j]
            else:
                continue
        print(abs(s1-s2),end=" ")
    
                

n=int(input())
a=list(map(int,input().split(" ")))
for i in range(0,n):
    if i<n-1:
        print(a[i+1],end=" ")
    else:
        i=0
        print(a[i])
        break

n=int(input())
l=list(map(int,input().split(" ")))
for i in range(n-1,-1,-1):
    print(l[i],end=' ')
#print(l[-1::-1])
    

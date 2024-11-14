n,x,y=map(int,input().split(" "))
l=[]
for i in range(1,n+1):
    l.append(x*i)
if y in l:
    print("YES")
else:
    print("NO")

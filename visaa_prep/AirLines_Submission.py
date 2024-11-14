x,n=map(int,input().split(" "))
h=(n-x*100)/100
if h-int(h)>0:
    print(int(h)+1)
else:
    print(int(h))

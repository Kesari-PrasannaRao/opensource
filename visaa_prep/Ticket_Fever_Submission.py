t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    d=n-m
    if d>=0:
        print(d)
    else:
        print(0)

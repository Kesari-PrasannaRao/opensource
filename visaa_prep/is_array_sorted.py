n=int(input())
l=list(map(int,input().split(" ")))
k=sorted(l)
if k==l:
    print("true")
else:
    print("false")

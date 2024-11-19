n=int(input())
a=list(map(int,input().split(' ')))
k=int(input())
f=0
for i in range(n):
    if a[i]==k:
        f=i
        break
    else:
        continue
if f:
    print(f)
else:
    print(-1)

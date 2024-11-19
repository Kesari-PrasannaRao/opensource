import math
n=int(input())
s=list(map(int,input().split(" ")))
m=0
p=0
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i]<(s[j]+s[j+1]) and s[j]<(s[i]+s[j+1]) and s[j+1]<(s[i]+s[j]):
            p=s[i]+s[j]+s[j+1]
        if m<p:
            m=p
if m:
    print(m)
else:
    print(-1)

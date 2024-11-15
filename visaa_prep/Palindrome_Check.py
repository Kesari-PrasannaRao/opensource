s=input()
s1=len(s)
r=0
l=0
h=s1-1
while(l<=h):
    if s[l]==s[h]:
        r=1
    else:
        r=0
        break
    l=l+1
    h=h-1
if r:
    print("TRUE")
else:
    print("FALSE")

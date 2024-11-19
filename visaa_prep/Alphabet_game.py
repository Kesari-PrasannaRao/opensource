s=input()
c=0
v=0
v1=['a','e','i','o','u','A','E','I','O','U  ']
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        if i in v1:
            v=v+1
        else:
            c=c+1
print("{},{}".format(v,c))

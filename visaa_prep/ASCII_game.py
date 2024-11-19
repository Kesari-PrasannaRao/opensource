s=input()
r=''
for i in s:
    if i>='a' and i<='z':
        r=r+i.upper()
    elif i>='A' and i<='Z':
        r=r+i.lower()
    else:
        continue
print(r)

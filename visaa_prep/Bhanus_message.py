n=input()
l=len(n)

if l<14 or l>14:
    print("Incorrect")
else:
    s=0
    if (n[0]=='+') and (n[1]>='0' or n[1]<='9') and (n[2]>='0' or n[2]<='9') and (n[3]==" "):
        for i in range(4,l):
            c=0
            if n[i]>='0' or n[i]<='9':
                c=1
                s=s+int(n[i])
        if c and s>0:
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("Incorrect")

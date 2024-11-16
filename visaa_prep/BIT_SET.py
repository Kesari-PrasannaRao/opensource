n=int(input())
k=int(input())

'''b=bin(n)[2:]
r=b[-k:]
r=int(r,2)
if k==r:
    print("true")
else:
    print("false")'''

b=1<<(k-1)
if n&b:
    print("true")
else:
    print("false")

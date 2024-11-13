x,y,z=input().split(' ')
x,y,z=int(x),int(y),int(z)
if x>z:
    print(0)
elif x+y>z:
    print(1)
elif x+y <= z:
    print(2)

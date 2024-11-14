x,y,z=map(int,input().split(" "))
t=x*y
t0=24*60*z
if t0>=t:
    print("YES")
else:
    print("NO")

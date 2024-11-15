n=int(input())
s=0
while n>0:
    s=s+n%10
    n=n//10
if s%2==0:
    print("Vignesh")
else:
    print("Charan")
    

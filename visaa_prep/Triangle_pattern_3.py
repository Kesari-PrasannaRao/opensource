n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j<=i:
            print(j,end='')
        elif j>2*n-i:
            print(2*n+1-j,end='')
        else:
            print(" ",end='')              
    print()

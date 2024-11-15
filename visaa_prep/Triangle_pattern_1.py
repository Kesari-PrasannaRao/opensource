n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if j<=i:
            print(k,end=' ')
            k=k+1
    print()

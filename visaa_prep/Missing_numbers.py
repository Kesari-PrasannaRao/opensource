m=int(input())
l1=list(map(int,input().split(' ')))
n=int(input())
l2=list(map(int,input().split()))
l=[]
for i in l2:
    if l1.count(i)<l2.count(i):
        if i not in l:
            l.append(i)
l.sort()
for i in l:
    print(i,end=' ')

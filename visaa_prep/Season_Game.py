n=int(input())
if n<1 or n>12:
    print("Invalid")
elif n>=3 and n<=5:
    print("Spring")
elif n>=6 and n<=8:
    print("Summer")
elif n>=9 and n<=11:
    print("Autumn")
else:
    print("Winter")

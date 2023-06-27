a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"));
if (a>b and a<c)or(b<a and b>c):
    print("Middle number=",a)
elif (b>a and b<c)or(b<a and b>c):
    print("Middle number=",b)
else:
    print("Middle number=",c)

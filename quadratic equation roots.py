import math
print("For quadratic equation ,a**x2+bx+c=0,enter coefficient ")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("enter c:"))
if a==0:
    print("Value of",a,"should not be zero")
    print("Abort!!")
else:
    delta=b*b-4*a*c
    if (delta>0):
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("roots are real and unequal")
        print("Roots1=",root1,"roots2=",root2)
    elif (delta==0):
        root1=-b/(2*a)
        print("roots are real and equal")
        print("roots1=",root1,"Roots2=",root1)
    else:
        print("Roots are complex and imaginary")
        

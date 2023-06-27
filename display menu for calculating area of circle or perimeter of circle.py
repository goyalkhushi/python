radius=float(input("Enter a radius of circle:"))
print("1.Calculate area")
print("2.Calculate perimeter")
choice=int(input("Enter choice 1 or 2:"))
if choice==1:
    area=3.14*radius*radius
    print("Area of circle with radius:",area)
if choice==2:
    perimeter=2*3.14*radius
    print("Perimeter of circle is:",perimeter)

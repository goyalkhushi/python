num1=float(input("Enter 1 number:"))
num2=float(input("Enter 2 number:"))
num3=float(input("Enter 3 number:"))
if (num1>num2)and (num1>num3):
    largest=num1
elif (num2>num3) and (num2>num1):
    largest=num2
else:
    largest=num3
print("The largest number is:",largest)

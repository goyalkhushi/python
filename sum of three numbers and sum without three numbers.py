num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
sum1=0
sum2=0
sum1=num1+num2+num3
if (num1!=num2 and num1!=num3):
    sum2+=num1
elif (num2!=num1 and num2!=num3):
    sum2+=num2
elif (num3!=num1 and num3!=num2):
    sum2+=num3
print("Numbers are:",num1,num2,num3)
print("sum of three given numbers is:",sum1)
print("sum of non-duplicate number is:",sum2)

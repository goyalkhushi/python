#product of digits of given number
n=int(input("Enter a number:"))
product=1
while (n>0):
    product=product*(n%10)
    n=n//10
print("product of digits=",product)

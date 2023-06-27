n=int(input("enter a number:"))
rev=0
x=n
while (n>0):
    rev=(rev*10)+n%10
    n=n//10
if (x==rev):
    print("number is Palindrome")
else:
    print("number is not palindrome")

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
d=int(input("Enter 4th number:"))
e=int(input("Enter 5 number:"))
total=(a+b+c+d+e)
percent=(total/500)*100
print("Total marks=",total,";""percentage=",percent);
if percent>=80:
    print("You have got grade A");
elif percent>=60:
    print("You have got grade B");
elif percent>=40:
    print("You have got grade C");
else:
    print("You have got grade D");

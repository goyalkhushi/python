ch=input("Enter a single character:")
if (ch>='A' and ch<='Z'):
    print("You entered a upper case character")
elif (ch>='a' and ch<='z'):
    print("you entered a lower case character")
elif (ch>='0' and ch<='9'):
    print("You entered a digit")
else:
    print("you entered a special character")

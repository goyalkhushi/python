i=int(input("Enter a number:"))
sum=0
while (i>0):
    sum=sum+i%10
    i//10
print(sum)

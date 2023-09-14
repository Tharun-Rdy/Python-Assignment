sum=0
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    if i%2==0:
        sum=sum+i
print(sum)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
n=num2
sum=0
i=num1
while i<=n:
    if i%2==0:
        sum=sum+i
        i=i+1
print(sum)


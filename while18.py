num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num1
mul=1
n=num2
while i<=n:
    if i%2==0:
        mul=mul*i
    i=i+1
print(mul)

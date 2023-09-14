num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
x=num2
while x>=num1 and x<=num2:
    if x%2==0:
        print(x)
    x-=1  
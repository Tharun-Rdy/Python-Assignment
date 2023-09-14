num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
pro=1
i=1
n=num2
while i<=n:
    if i%2==0:
        pro=pro*i
        i=i+1
print(pro)
'''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
mul=1
for i in range(num1,num2):
    if i%2!=0:
        mul=mul*i
print(mul)
'''

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
mul=1
i=num1
while i>=num1 and i<=num2:
    if i%2!=0:
        mul=mul*i
    i=i+1
print(mul)

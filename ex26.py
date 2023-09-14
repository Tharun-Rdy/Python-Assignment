'''
sum=0
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2!=0:
        sum=sum+i
print(sum)
'''

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=0
i=num2
while i>=num1 and i<=num2:
    if i%2!=0:
        sum=sum+i
    i=i-1
print(sum)

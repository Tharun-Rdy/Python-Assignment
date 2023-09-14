'''
sum=0
num=int(input("Enter a positive integer: "))
for i in range(1,num+1):
    sum=sum+i
print(sum)
'''


num=int(input("Enter a positive integer: "))
i=1
sum=0
while i>=1 and i<=num:
    sum=sum+i
    i=i+1
print(sum)

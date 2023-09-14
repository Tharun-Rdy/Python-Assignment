'''
num=int(input("Enter a number: "))
for i in range(100,201):
    if i%10==0:
        print("none")
    else:
        print(i)
'''

num=int(input("Enter a number: "))
i=100
while i>=100 and i<=200:
    if i%10==0:
        print("none")
    else:
        print(i)
    i=i+1

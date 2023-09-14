 """
FileName          : Looping Constructs(Assignment-3)
Developer         : Tharun
Date              : 13-09-2023 03:00 pm
Purpose           : Performing the actions as per the logic provided and print the output in a proper format.
Location          : Anantapur India
Version           : v0.1
"""

------------------------------------------------------------------------------------------------------------------------------------------------------
1.
for x in range(1,11):
    print("I can do it today itself")

x=1
while x<=10:
    print("I can do it today itself")
    x=x+1
------------------------------------------------------------------------------------------------------------------------------------------------------
2.
for i in range(1,21):
    print(i)

x=1
while x<=20:
    print(x)
    x+=1
------------------------------------------------------------------------------------------------------------------------------------------------------
3.1
for i in range(20,0,-1):
    print(i)
	

x=20
while x>=1 and x<=20:
    print(x)
    x-=1
------------------------------------------------------------------------------------------------------------------------------------------------------
4.
for i in range(100,201):
    print(i)
	
x=100
while x<=200:
    print(x)
    x+=1
------------------------------------------------------------------------------------------------------------------------------------------------------
4.1
num=int(input("Enter a number: "))
for i in range(100,201):
    if i%10==0:
        print("none")
    else:
        print(i)

num=int(input("Enter a number: "))
i=100
while i>=100 and i<=200:
    if i%10==0:
        print("none")
    else:
        print(i)
    i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
5.
for i in range(200,99,-1):
    print(i)

i=200
while i>=100 and i<=200:
    print(i)
    i-=1
------------------------------------------------------------------------------------------------------------------------------------------------------    
 5.1
 ''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
for i in range(100,201):
    if i in range(101,201,10):
        print("")
    else:
        print(i)
''

i=100
while i>=100 and i<=200:
    if i in range(101,201,10):
        print("")
    else:
        print(i)
    i=i+1

------------------------------------------------------------------------------------------------------------------------------------------------------
6.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    print(i)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
x=num1
while x>=num1 and x<=num2:
    print(x)
    x+=1
------------------------------------------------------------------------------------------------------------------------------------------------------
7.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    print(i)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
x=num2
while x>=num1 and x<=num2:
    print(x)
    x-=1
------------------------------------------------------------------------------------------------------------------------------------------------------
8.
for i in range(1,41):
    if i%2==0:
        print(i)

x=2
while x<=40:
    if x%2==0:
        print(x)
    x+=1
------------------------------------------------------------------------------------------------------------------------------------------------------
8.1
for i in range(1,21,):
    if i in range(0,21,2**2):
        print("")
    else:
        print(i)

i=1
while i>=1 and i<=20:
    if i in range(0,20,2*2):
        print("")
    else:
        print(i)
    i=i+1

------------------------------------------------------------------------------------------------------------------------------------------------------
9.
for i in range(41,1,-1):
    if i%2==0:
        print(i)

i=40
while i>=1 and i<=40:
    print(i)
    i-=2
------------------------------------------------------------------------------------------------------------------------------------------------------
10.
for i in range(100,201):
    if i%2==0:
        print(i)

x=100
while x>=100 and x<=200:
    print(x)
    x+=2
------------------------------------------------------------------------------------------------------------------------------------------------------
11.
for i in range(200,99,-2):
    print(i)
	
i=200
while i>=100 and i<=200:
    if i%2==0:
        print(i)
    i-=1
------------------------------------------------------------------------------------------------------------------------------------------------------
12.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2==0:
        print(i)

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
x=num2
while x>=num1 and x<=num2:
    if x%2==0:
        print(x)
    x-=1  
------------------------------------------------------------------------------------------------------------------------------------------------------
13.
x=0
for i in range(1,41):
    if i%2==0:
        x=x+i
print(x)


n=40
sum=0
i=1
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
14.
sum=0
for i in range(100,201):
    if i%2==0:
        sum=sum+i
print(sum)

n=200
sum=0
i=1
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
15.
sum=0
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    if i%2==0:
        sum=sum+i
print(sum)


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
------------------------------------------------------------------------------------------------------------------------------------------------------
16.
i=1
pro=1
for i in range(1,41):
    if i%2==0:
        pro=pro*i
print(pro)

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
------------------------------------------------------------------------------------------------------------------------------------------------------
17.
sum=0
for i in range(10,21):
    if i%2==0:
        sum=sum+i
print(sum)

n=20
sum=0
i=10
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
18.
mul=1
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2==0:
        mul=mul*i
print(mul)

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
------------------------------------------------------------------------------------------------------------------------------------------------------
19.
''
for i in range(1,40):
    if i%2!=0:
        print(i)


i=1
while i<=40:
    if i%2!=0:
        print(i)
    i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
20.
''
for i in range(40,0,-1):
    if i%2!=0:
        print(i)
''


i=40
while i>=1 and i<=40:
    if i%2!=0:
        print(i)
    i=i-1
------------------------------------------------------------------------------------------------------------------------------------------------------
21.

for i in range(100,200):
    if i%2!=0:
        print(i)


i=100
while i<=200:
    if i%2!=0:
        print(i)
    i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
22.

for i in range(200,100,-1):
    if i%2!=0:
        print(i)


i=200
while i>=100 and i<=200:
    if i%2!=0:
        print(i)
    i=i-1
------------------------------------------------------------------------------------------------------------------------------------------------------
23.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2!=0:
        print(i)



        
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num2
while i>=num1 and i<=num2:
    if i%2!=0:
        print(i)
    i=i-1
------------------------------------------------------------------------------------------------------------------------------------------------------
24.
''
sum=0
for i in range(1,40):
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
''

sum=0
i=1
while i>=1 and i<=40:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
25.
''
sum=0
for i in range(100,200):
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
''

sum=0
i=100
while i>=100 and i<=200:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
26.
''
sum=0
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2!=0:
        sum=sum+i
print(sum)
''

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
sum=0
i=num2
while i>=num1 and i<=num2:
    if i%2!=0:
        sum=sum+i
    i=i-1
print(sum)
------------------------------------------------------------------------------------------------------------------------------------------------------
27.
''
mul=1
for i in range(1,41):
    if i%2!=0:
        mul=mul*i
print(mul)
''

mul=1
i=1
while i>=1 and i<=40:
    if i%2!=0:
        mul=mul*i
    i=i+1
print(mul)
------------------------------------------------------------------------------------------------------------------------------------------------------
28.
''
mul=1
for i in range(10,20):
    if i%2!=0:
        mul=mul*i
print(mul)
''

mul=1
i=10
while i>=10 and i<=20:
    if i%2!=0:
        mul=mul*i
    i=i+1
print(mul)
------------------------------------------------------------------------------------------------------------------------------------------------------
29.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
mul=1
for i in range(num1,num2):
    if i%2!=0:
        mul=mul*i
print(mul)
''

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
mul=1
i=num1
while i>=num1 and i<=num2:
    if i%2!=0:
        mul=mul*i
    i=i+1
print(mul)
------------------------------------------------------------------------------------------------------------------------------------------------------
30.
''
for i in range(1,21):
    print("\nnumbers:",i,"\nsquares:",i*i,"\ncubes:",i*i*i)
''

i=1
while i>=1 and i<=20:
     print("\nnumbers:",i,"\nsquares:",i*i,"\ncubes:",i*i*i)
     i=i+1     
------------------------------------------------------------------------------------------------------------------------------------------------------
31.
''
for i in range(20,0,-1):
     print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    
''

i=20
while i>=1 and i<=20:
     print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
     i=i-1
------------------------------------------------------------------------------------------------------------------------------------------------------
32.
''
for i in range(1,41):
    if i%2==0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
''

i=1
while i>=1 and i<=40:
    if i%2==0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
33.
''
for i in range(41,1,-1):
    if i%2==0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
''

i=40
while i>=1 and i<=40:
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1   
------------------------------------------------------------------------------------------------------------------------------------------------------
34.
''
for i in range(1,40):
    if i%2!=0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
''

i=1
while i>=1 and i<=40:
    if i%2!=0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
35.
''
for i in range(40,0,-1):
    if i%2!=0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
''

i=40
while i>=1 and i<=40:
    if i%2!=0:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1
------------------------------------------------------------------------------------------------------------------------------------------------------
36.
''
for i in range(40,81):
    print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=40
while i>=40 and i<=80:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
         i=i+1
------------------------------------------------------------------------------------------------------------------------------------------------------
37.
''
for i in range(80,39,-1):
    print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=80
while i>=40 and i<=80:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
         i=i-1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
38.
''
for i in range(40,81):
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=40
while i>=40 and i<=80:
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
39.
''
for i in range(80,39,-1):
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=80
while i>=40 and i<=80:
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
40.
''
for i in range(40,80):
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=40
while i>=40 and i<=80:
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
41.
''
for i in range(80,40,-1):
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
i=80
while i>=40 and i<=80:
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
42.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num1
while i>=num1 and i<=num2:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
         i=i+1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
43.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num2
while i>=num1 and i<=num2:
         print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
         i=i-1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
44.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num1
while i>=num1 and i<=num2:
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
45.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num2
while i>=num1 and i<=num2:
    if i%2==0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
46.
''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num1,num2):
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)

''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num1
while i>=num1 and i<=num2:
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i+1
''
------------------------------------------------------------------------------------------------------------------------------------------------------
47.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
for i in range(num2,num1,-1):
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
i=num2
while i>=num1 and i<=num2:
    if i%2!=0:
        print("\nnumber:",i,"\nsquare:",i*i,"\ncube:",i*i*i)
    i=i-1
    
------------------------------------------------------------------------------------------------------------------------------------------------------
48.
sum=0
num=int(input("Enter a positive integer: "))
for i in range(1,num+1):
    sum=sum+i
print(sum)


num=int(input("Enter a positive integer: "))
i=1
sum=0
while i>=1 and i<=num:
    sum=sum+i
    i=i+1
print(sum)


------------------------------------------------------------------------------------------------------------------------------------------------------
49.

for i in range(1):
    print("A B C E F G H I J K L M N O P Q R S T U V W X Y Z") 


i=1
while i<=1:
    print("A B C E F G H I J K L M N O P Q R S T U V W X Y Z")
    break
------------------------------------------------------------------------------------------------------------------------------------------------------
50.
''
for i in range(1):
    print("Z Y X W V U T S R Q P O N M L K J I H G F E D C B A")
''

i=1
while i<=1:
    print("Z Y X W V U T S R Q P O N M L K J I H G F E D C B A")
    break
------------------------------------------------------------------------------------------------------------------------------------------------------
51.
''
for i in range(1):
    print("AZ BY CX DW EV FU GT HS IR JQ KP LO MN NM OL PK QJ RI SH TG UF VE WD XC YB ZA")
''

i=1
while i<=1:
    print("AZ BY CX DW EV FU GT HS IR JQ KP LO MN NM OL PK QJ RI SH TG UF VE WD XC YB ZA")
    break
-------------------------------------------------------------------------------------------------------------------------------------------------------
52.
''
for i in range(1):
    print("a b c d e f g h i j k l m n o p q r s t u v w x y z")
''
i=1
while i<=1:
    print("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    break
--------------------------------------------------------------------------------------------------------------------------------------------------------
53.
''
for i in range(1):
    print("z y x w v u t s r q p o n m l k j h g f e d c b a")
''

i=1
while i<=1:
    print("z y x w v u t s r q p o n m l k j h g f e d c b a")
    break
------------------------------------------------------------------------------------------------------------------------------------------------------
54.

for i in range(1):
    print("az by cx dw ev fu gt hs ir jq kp lo mn nm ol pk qj ri sh tg uf ve wd xc yb za")


i=1
while i<=1:
    print("az by cx dw ev fu gt hs ir jq kp lo mn nm ol pk qj ri sh tg uf ve wd xc yb za")
    break

output:
az by cx dw ev fu gt hs ir jq kp lo mn nm ol pk qj ri sh tg uf ve wd xc yb za
------------------------------------------------------------------------------------------------------------------------------------------------------
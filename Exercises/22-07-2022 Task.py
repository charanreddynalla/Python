
#1> Write a program to find sum of number.
'''
n1=int(input("Enter First number: "))
n2=int(input("Enter second number: "))
print(n1+n2)

Output:
Enter First number: 10
Enter second number: 20
30
'''

#2>WAP to find the number is strong number or not
'''
num=int(input('Enter Any number: '))
sum=0
temp=num
while(num):
    i=1
    fact=1
    remainder=num%10
    while(i<=remainder):
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if(sum==temp):
    print('The number is strong number')
else:
    print('The number is not strong number')

Output:
Enter Any number: 145
The number is strong number
'''
#3> Python Program to Find the Square Root
'''
num=eval(input('Enter any number: '))
sqrt=num**0.5
sqrt=int(sqrt)
print('The square root of the',num,'is',sqrt)

Output:
The square root of the 10 is 3.1622776601683795
'''

#4>Python Program to Calculate the Area of a Triangle 
'''
a=eval(input('Enter first number: '))
b=eval(input('Enter second number: '))
c=eval(input('Enter third number: '))
d=(a+b+c)/2
area=(d*(d-a)*(d-b)*(d-c))**0.5

print('The are of triangle is {} '.format(area))

Output:
Enter first number: 5
Enter second number: 6
Enter third number: 7
The are of triangle is 14.696938456699069 
'''
#5>Python Program to Solve Quadratic Equation
'''
a=eval(input('Enter the value of a: '))
b=eval(input('Enter the value of b: '))
c=eval(input('Enter the value of c: '))
d=b**2-4*a*c
if(d<0):
    d=-d
    numerator=-b-d**0.5
    denominator=2*a
    Total=numerator/denominator
    print(Total)
else:
    numerator=-b-d**0.5
    denominator=2*a
    Total=numerator/denominator
    print(Total)

Output:
Enter the value of a: 10
Enter the value of b: 20
Enter the value of c: 30
-2.414213562373095
'''

#6>Python Program to Swap Two Variables 
'''
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=a
a=b
b=c
print('The value of a is {}'.format(a))
print('The value of b is {}'.format(b))

Output:
Enter first number: 10
Enter second number: 20
The value of a is 20
The value of b is 10
'''
#7>Python Program to Convert Kilometres to Miles
'''
n=eval(input('Enter number of kilometer: '))
num=n/1.609
print(num)
Output:
Enter number of kilometer: 12
7.458048477315103
'''
#8>Python Program to Check Leap Year
'''
Year=int(input('Enter any year: '))
if(Year%400==0) or (Year%100!=0) and (Year%4==0):
    print('Leap year')
else:
    print('Non leap year')
    
Output:
Enter any year: 2000
Leap year
Enter any year: 2013
Non leap year
'''
#9>Python Program to Check Prime Number
'''
num=int(input('Enter any number: '))
if num>1:
    for i in range(2, num):
        if (num%i)==0:
            print(num,"Not Prime number")
            break
    else:
        print(num,"prime number ")
else:
    print(num, 'Not prime number')

Output:
Enter any number: 15
15 Not Prime number
'''

#10>Python Program to Find the Factorial of a Number
'''
n=eval(input('Enter any number'))
factorial=1
if n<0:
    print('Please enter positive number')
elif n==0:
    print('Factoril of o is 1')
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print('The factorial of',n,'is:',factorial)
Output:
Enter any number6
The factorial of 6 is: 720
'''

#11>Python Program to Print the Fibonacci sequence
'''
def Fibonacci(n):
    if n<0:
        print('Incorrect input')
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))
print(Fibonacci(11))

Output:
34
89
'''

#12>Python Program to Check Armstrong Number
'''
def armstrong(n,o):
    sum=0
    temp=n
    while temp > 0:
        digit=temp % 10
        sum+=digit**o
        temp=temp//10
    if n==sum:
        print(n, "is armstrong number")
    else:
        print(n, "is not armstrong number")
num=eval(input('Enter any number: '))
order=len(str(num))
armstrong(num,order)
'''
#13>Python Program to Find Armstrong Number in an Interval
'''
lower=eval(input('Enter lower number: '))
upper=eval(input('Enter upper number: '))
for num in range(lower, upper+1):
    total=0
    num=str(num)
    for i in num:
        length=len(num)
        product=(int(i)**length)
        total=total+product
    if(total==int(num)):
        print(total)
Output:
Enter lower number: 5
Enter upper number: 500
5
6
7
8
9
153
370
371
407
'''

#14>Python Program to Find the Sum of Natural Numbers
'''
num=eval(input('Enter any number:'))
sum=0
if num<0:
    print('Enter positive number')
else:
    while(num>0):
        sum=sum+num
        num=num-1
    print('The sum is', sum)

Output:
Enter any number:15
The sum is 120
'''
#15>Python Program to Find the Factors of a Number
'''
n=int(input('Enter any number: '))
lst=[]
for i in range(1,n+1):
    if n%i==0:
        lst.append(i)
print('Factors of {} is {}: '.format(n,lst))

Output:
Enter any number: 15
Factors of 15 is [1, 3, 5, 15]: 
'''

#16>Python Program to Convert Decimal to Binary, Octal and Hexadecimal
'''
num=eval(input('Enter any number: '))
print(bin(num))
print(oct(num))
print(hex(num))

Output:
Enter any number: 400
0b110010000
0o620
0x190
'''

#17>Python Program to Find LCM
'''
n1=eval(input('Enter First number: '))
n2=eval(input('Enter second number: '))
def LCMof2num(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater=greater+1
    return lcm
print('The L.C.M of', n1 ,'and', n2, 'is:', LCMof2num(n1,n2))

Output:
Enter First number: 3
Enter second number: 4
The L.C.M of 3 and 4 is: 12
'''

#18>Python Program to Find HCF

'''
n1=eval(input('Enter First number: '))
n2=eval(input('Enter second number: '))
def HCFof2num(x,y):
    if x<y:
        smaller=x
    else:
        smaller=y
    for i in range(1, smaller+1):
        if((x%i==0) and (y%i==0)):
           hcf=i
    return hcf
print('The HCF of',n1,'and',n2,'is:',HCFof2num(n1,n2))

Output:
Enter First number: 8
Enter second number: 12
The HCF of 8 and 12 is: 4
'''






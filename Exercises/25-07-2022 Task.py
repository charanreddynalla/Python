#1> Print First 10 natural numbers using while loop 
'''
n=int(input('Enter any number: '))
i=0
while(i<n):
    print(i)
    i=i+1

Output:
Enter any number: 10
0
1
2
3
4
5
6
7
8
9
'''

#2>Calculate the sum of all numbers from 1 to a given number
'''
n=int(input('Enter any number: '))
sum=0
for i in range(1,n):
    print(sum)
    sum=sum+i

Output:
Enter any number: 10
0
1
3
6
10
15
21
28
36
'''
#3>Write a program to print multiplication table of a given number
'''
n=eval(input('Enter any number: '))
for i in range(1,11):
    print(n, '*', i ,'=',n*i)
Output:
Enter any number: 8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
'''
#4>Display numbers from a list using loop

'''
lst=[4,5,6,7,8,9,10]
for i in lst:
    print(i)

Output:
4
5
6
7
8
9
10
'''

#5>Count the total number of digits in a number

'''
n=input('Enter any number: ')
print(len(n))

Output:
Enter any number: 123456
6
'''

#6>Print list in reverse order using a loop     

'''
lst=[10,20,30,40,50]
length=len(lst)-1
for i in range(length,-1,-1):
    print(lst[i])
Output:
50
40
30
20
10
'''

#7>numbers from -10 to -1 using for loopDisplay

'''
for i in range(-10,0,1):
    print(i)

Output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
'''
#8>Use else block to display a message “Done” after successful execution of for loop

'''
num=eval(input('Enter any number: '))
for i in range(num):
    print(i)
else:
    print('Done')

Output:
Enter any number: 5
0
1
2
3
4
Done
'''
#9>Write a program to display all prime numbers within a range

'''
num1=eval(input('Enter first number: '))
num2=eval(input('Enter second number: '))
for numb in range(num1,num2+1):
    if numb>1:
        for i in range(2,numb):
            if numb%i==0:
                break
                print('Not prime number')
        else:
            print(numb, end=' ')

Output:
Enter first number: 1
Enter second number: 50
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 
'''
#10> Dispaly the Fibonacci series upto 10 terms

'''
n=eval(input('Enter any number: '))
n1=0
n2=1
count=0
if(n<0):
    print('Enter valid number')
elif n==1:
    print('Number sequence',n)
else:
    print('Fiboncci series is:')
while count<n:
    print(n1, end=' ')
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1

Output:
Enter any number: 13
Fiboncci series is:
0 1 1 2 3 5 8 13 21 34 55 89 144 
'''

#11> Find the factorial of a given number

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

#12> Reverse a given integer number

'''
num=123456
n=str(num)
print(n[::-1])

Output:
654321
'''

#13>Find the sum of series upto n

'''
n=int(input('Number: '))
sum=0
lst=[]
for i in range(1,n+1):
    sum=sum+i
    lst.append(sum)
print(lst)

#Output:
Number: 10
[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
'''

#14>calculate the cube of the numbers from 1 to n

'''
n=int(input('Enter any muber: '))
for i in range(1,n):
    print(i**3)

Output:
Enter any muber: 7
1
8
27
64
125
216
'''

#15>Use a loop to dispaly elements from a given list present at odd index position   

'''
lst=[10,20,30,40,50,60,70]
for i in range(1,len(lst),2):
    print(lst[i])

Output:
20
40
60
'''

#16>Name the keyword which helps in writing code involves condition

'''
if keyword
'''

#17>Write the syntax of simple if statement

'''
if(condition):
    expression

'''
#18>Is there any limit of statement that can appear under an if block.

'''
There is no limit of staement
'''
#19>Write a program to check whether a person is eligible for voting or not. (accept age from user)

'''
n=int(input('Enter the age: '))
if n>=18:
    print('You are eligible for voting')
else:
    print('You are in the process for voting')

Output:
Enter the age: 20
You are eligible for voting
'''

#20>Write a program to check whether a number entered by user is even or odd.

'''
num=int(input('Enter any number: '))
if num%2==0:
    print('Even number')
else:
    print('Odd number')
'''
#21>Write a program to check whether a number is divisible by 7 or not. 

'''
n=int(input('Enter any number: '))
if n%7==0:
    print('It is divisible of 7')
else:
    print('It is not divisible of 7')

Output:
Enter any number: 21
It is divisible of 7
'''
#22>Write a program to display "Hello" if a number entered by user is a multiple of five ,otherwise print "Bye". 

'''
num=int(input('Enter any number: '))
if num%5==0:
    print('Hello')
else:
    print('Bye')
Output:
Enter any number: 17
Bye
'''
#23>Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 

#Unit                                                     Price   

#First 100 units                                               no charge 

#Next 100 units                                              Rs 5 per unit 

#After 200 units                                             Rs 10 per unit 

#(For example if input unit is 350 than total bill amount is Rs2000) 

'''
units=int(input('Enter the units: '))
if units<100:
    print('No charge')
elif units>=100 and units<=200:
    print((100*0)+(units-100)*5)
elif units>200:
    print((100*5)+(units-200)*10)

Output:
Enter the units: 350
2000
'''
#24>Write a program to display the last digit of a number. 
#(hint : any number % 10 will return the last digit)

'''
n=int(input('Enter any number: '))
last_digit=n%10
print('The last digit of a given number is: ', last_digit)

Output:
Enter any number: 256
The last digit of a given number is:  6
'''
#25>Write a program to check whether the last digit of a number( entered by user ) is  divisible by 3 or not.

'''
n=int(input('Enter any number: '))
lastdigit=n%10
if lastdigit%3==0:
    print('Divisible')
else:
    print('Not divisible')
'''
#26>Write a program to accept percentage from the user and display the grade according to the following criteria:

#        Marks                                    Grade 
#    > 90                                         A 
#     > 80 and <= 90                     B 
#       >= 60 and <= 80                 C 
#      below 60                                 D 
'''
marks=int(input('Enter marks of the student: '))
if marks>90:
    print('A Grade')
elif marks>80 and marks<=90:
    print('B Grade')
elif marks>=60 and marks<=80:
    print('C Grade')
elif marks<60:
    print('D Grade')

Output:
Enter marks of the student: 70
C Grade
'''
#27>Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 
#        Cost price (in Rs)                                 Tax 
#     > 100000                                                  15 % 
 #      > 50000 and <= 100000                   10% 
#     <= 50000                                                  5% 

'''
price=int(input('Enter the price of bike: '))
if price>100000:
    print((15/100)*(price))
elif price>50000 and price<=100000:
    print((10/100)*(price))
elif price<=50000:
    print((5/100)*(price))

Output:
Enter the price of bike: 60000
6000.0
'''
#28>Write a program to check whether an years is leap year or not.

'''
year=int(input('Enter the year: '))
if((year%400==0 or year%100!=0) and year%4==0):
    print('Leap Year')
else:
    print('Non Leap year')
'''
#29>Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

'''
num=eval(input('Enter any week: '))
if num==1:
    print('Sunday')
elif num==2:
    print('Monday')
elif num==3:
    print('Tuesday')
elif num==4:
    print('Wednesday')
elif num==5:
    print('Thursday')
elif num==6:
    print('Friday')
elif num==7:
    print('Saturday')
else:
    print('Please enter valid number for a week')
'''

#30>Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on

'''
month=int(input('Enter the month: '))
days=int(input('Enter the days: '))
if month==1 and days==31:
    print('January')
elif month==2 and days==28 or 29:
    print('February')
elif month==3 and days==31:
    print('March')
elif month==4 and days==30:
    print('April')
elif month==5 and days==31:
    print('May')
elif month==6 and days==30:
    print('June')
elif month==7 and days==31:
    print('July')
elif month==8 and days==31:
    print('August')
elif month==9 and days==30:
    print('Septmber')
elif month==10 and days==31:
    print('Octomber')
elif month==11 and days==30:
    print('November')
elif month==12 and days==31:
    print('December')
else:
    print('Please enter valid moth and days')

Output:
Enter the month: 5
Enter the days: 31
May
'''
#31>What do you mean by statement? 

'''
A statement is an instruction that the python interpreter can execute
'''
#32>Write the logical expression for the following: 
#A is greater than B and C is greater than D 
'''
logic=A>B and C>D:
 '''   
#33>Accept any city from the user and display monument of that city. 
#            City                                 Monument 
#               Delhi                               Red Fort 
#             Agra                                Taj Mahal 
 #          Jaipur                              Jal Mahal 

'''
city=input('Enter any city: ')
if city=='Delhi':
    print('Red Fort')
elif city=='Agra':
    print('TajMahal')
elif city=='Jaipur':
    print('JalMahal')
else:
    print('Please enter the valid city')
Output:
Enter any city: Jaipur
JalMahal
Enter any city: jaipur
Please enter the valid city
'''
#34>Write the output of the following if a = 9    
#    if (a > 5 and a <=10):     
#         print("Hello")     
#    else:     
#        print("Bye") 

'''
Output:
    'Hello'
'''    
#35>Write a program to check whether a number entered is three digit number or not.

'''
number=int(input('Enter any number: '))
number=str(number)
len=len(number)
if len==3:
    print('Given number is three digit number')
else:
    print('Given number is not three digit number')
'''
#36>Write a program to check whether a person is eligible for voting or not.(voting age >=18) 

'''
n=int(input('Enter the age: '))
if n>=18:
    print('You are eligible for voting')
else:
    print('You are in the process for voting')

Output:
Enter the age: 20
You are eligible for voting
'''
#37>Write a program to check whether a person is senior citizen or not. 

'''
age=int(input('Enter the age of the person: '))
if age>=60:
    print('You are Senior citizen')
else:
    print('Your age is in between 1-59')

Output:
Enter the age of the person: 64
You are Senior citizen
Enter the age of the person: 15
Your age is in between 1-59
'''

#38>Write a program to find the lowest number out of two numbers excepted from user.

'''
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
if n1<n2:
    print(n1, 'is lowest among',n1,n2)
elif n1>n2:
    print(n2, 'is lowest among',n1,n2)
else:
    print('Both are equal')

Output:
Enter first number: 10
Enter second number: 20
10 is lowest among 10 20
'''
#39>Write a program to find the largest number out of two numbers excepted from user. 

'''   
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
if n1>n2:
    print(n1, 'is largest among',n1,n2)
elif n1<n2:
    print(n2, 'is largest among',n1,n2)
else:
    print('Both are equal')

Output:
Enter first number: 10
Enter second number: 20
20 is largest among 10 20
'''
#40>Write a program to check whether a number (accepted from user) is positive or negative.

'''
num=int(input('Enter any number: '))
if num>0:
     print('Positve number')
else:
    print('Negative number')
 
Output:
Enter any number: 12
Positve number
'''

#41>Write a program to check whether a number is even or odd. 

'''
num=int(input('Enter any number: '))
if num%2==0:
    print('Even number')
else:
    print('Odd number')

Output:
Enter any number: 31
Odd number
'''
#42>Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

'''
num=int(input('Enter any number: '))
if num%2==0 and num%3==0:
    print('Given number is divisible by both 2 and 3')
else:
    print('Number is not divisible by both')

Output:
Enter any number: 30
Given number is divisible by both 2 and 3
'''
#43>Write a program to find the largest number out of three numbers excepted from user.

'''
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3=int(input('Enter third number: '))

if n1>n2 and n1>n3:
    print(n1, 'is largest number')
elif n2>n1 and n2>n3:
    print(n2, 'is largest number')
elif n3>n1 and n3>n2:
    print(n3, 'is largest number')
else:
    print('All are equal numbers')

Output:
Enter first number: 103
Enter second number: 90
Enter third number: 10
103 is largest number
'''

#44>Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC.

'''
temp=int(input('Enter temparature: '))
if temp<100:
    print('Water boilid')
else:
    print('Water boiling')

Output:
Enter temparature: 10
Water boilid
'''

#45>the age of 4 people and display the youngest one and oldest one? Accept 

'''
p1=int(input('Enter the age: '))
p2=int(input('Enter the age: '))
p3=int(input('Enter the age: '))
p4=int(input('Enter the age: '))

if p1>p2 and p1>p3 and p1>p4:
    print('P1 is oldest')
elif p2>p1 and p2>p3 and p2>p4:
    print('P2 is oldest')
elif p3>p1 and p3>p2 and p3>p4:
    print('P3 is oldest')
elif p4>p1 and p4>p2 and p4>p3:
    print('P4 is oldest')
else:
    print('All persons are same age group persons')

Output:
Enter the age: 10
Enter the age: 20
Enter the age: 30
Enter the age: 40
P4 is oldest
'''

#46>Accept the following from the user and calculate the percentage of class attended: 
#a.     Total number of working days 
#b.     Total number of days for absent 

#After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam. 

'''
working_days=30
present=25
absent=5
avg=(25/30)*100
if (avg<75):
    print('The student is not able to write exam')
else:
    print('Student is eligible to write the exam')

Output:
Student is eligible to write the exam
'''

#47>Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle. 


#Note : 
#An equilateral triangle is a triangle in which all three sides are equal. 
#A scalene triangle is a triangle that has three unequal sides. 
#An isosceles triangle is a triangle with (at least) two equal sides. 

'''
a=int(input('Enter any value: '))
b=int(input('Enter any value: '))
c=int(input('Enter any value: '))
if(a==b==c):
    print('An equilateral triangle')
elif(a!=b!=c):
    print('three unequal sides')
elif(a==b or b==c or c==a):
    print('An isosceles triangle')

Output:
Enter any value: 10
Enter any value: 20
Enter any value: 50
three unequal sides
'''

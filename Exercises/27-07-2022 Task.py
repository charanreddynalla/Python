#1>Accept 10 numbers from the user and display their average. 
'''
sum=0
for i in range(1,11):
    n=int(input('Enter any number: '))
    sum=sum+n
avg=sum/10
print(avg)
'''
#2>Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

'''
n1=0
n2=0
for i in range(12,38):
    if i%2==0:
        n1=n1+i
    else:
        n2=n2+i
print('The sum of even numbers from 12 to 37 is', n1)
print('The sum of odd numbers from 12 to 37 is', n2)   

Output:
The sum of even numbers from 12 to 37 is 312
The sum of odd numbers from 12 to 37 is 325
'''
#3>Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

'''
n1=100
n2=500
sum=0
lst=[]
for i in range(n1,n2+1):
    if (i%11==0) and (i%2!=0):
        lst.append(i)
print(lst)

Output:
[121, 143, 165, 187, 209, 231, 253, 275, 297, 319, 341, 363, 385, 407, 429, 451, 473, 495]
'''
#4>Write a program to print numbers from 1 to 20 except multiple of 2 & 3

'''
n1=1
n2=20
for i in range(n1,n2+1):
    if (i%2!=0) and (i%3!=0):
        print(i)

Output:
1
5
7
11
13
17
19
'''
#5>Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers.

'''
num=int(input('Enter any numnber: '))
sum=0
avg=0
for i in range(num,0,-1):
    sum=sum+i
    avg=sum/num
print(avg)

Output:
Enter any numnber: 20
10.5
'''
#6>Write a program to accept decimal number and display its binary number.

'''
n=eval(input('Enter any number: '))
print(bin(n))

Output:
Enter any number: 12
0b1100
'''

#7>Convert the following loop into for loop : #nOT DONE

#x = 4 
#while(x<=8):
#   print(x*10) 
#    x+=2 

'''
x=4
for  i in range(1,x):
        print(x*10)
        x=x+2
output:
40
60
80
'''

#8>What is nested loop? 

'''
if inside the if

if(con):
    if(con):
        if(con):
            expre
        elif(con):
            expre
        else:
    else:
        exp
else:
    exp
'''
#9>Write a program to convert temperature in Fahrenheit to Celsius. 

'''
fahrenheit=int(input('Enter temparature: '))
celsius=(fahrenheit-32)*5/9
print(celsius)

Output:
Enter temparature: 95
35.0
'''
#10>Write a Python program to get the Fibonacci series between 0 to 50.

#Note : The Fibonacci Sequence is the series of numbers : 
#0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
#Every next number is found by adding up the two numbers before it. 
#Expected Output : 1 1 2 3 5 8 13 21 34 

'''
n=int(input('Enter any number: '))
n1=0
n2=1
count=0
if count<0:
    print('Enter invalid number')
elif n==1:
    print('Number sequence',n)
else:
    print('Fibonacci series of a number is: ')
while count<n:
    print(n1, end=' ')
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
Output:
Enter any number: 10
Fibonacci series of a number is: 
0 1 1 2 3 5 8 13 21 34 
'''

#11>Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz". 

#Sample Output : 
#fizzbuzz 
#1 
#2
#fizz 
#4 
#Buzz 

'''
for i in range(1,51):
    if (i%3==0 and i%5==0):
        print('fizzbuzz')
        continue
    elif i%3==0:
        print('Fizz')
        continue
    elif i%5==0:
        print('Buzz')
    print(i)

Output:
    1
2
Fizz
4
Buzz
5
Fizz
7
8
Fizz
Buzz
10
11
Fizz
13
14
fizzbuzz
16
17
Fizz
19
Buzz
20
......................
'''

#12>Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
#Note : Use 'continue' statement. 
#Expected Output : 0 1 2 4 5 

'''
for i in range(0,7):
    if i==0:
        print(i)
        continue
    elif i%3!=0:
        print(i)
        continue
Output:
0
1
2
4
5
'''









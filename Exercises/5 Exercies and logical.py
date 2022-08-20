#26-07-2022
#1>WAP to reverse a number 
'''
n=12345
n=str(n)
print(n[::-1])

Output:
54321
'''
#2>WAP to count  the number  occurrence/frequency  of a  each character in a string .

'''
string='good morning'
reverse={}
for keys in string:
    reverse[keys]=reverse.get(keys,0)+1
print(reverse)

Output:
{'g': 2, 'o': 3, 'd': 1, ' ': 1, 'm': 1, 'r': 1, 'n': 2, 'i': 1}
'''
#3>WAP  to check length of two string is equal or not.

'''
str1='Hello'
str2='Good'

if len(str1)==len(str2):
    print('Equal')
else:
    print('Not equal')

Output:
Not equal
'''
#4>Python program to print even numbers up to 100

'''
lst=[]
for i in range(1,101):
    if i%2==0:
        lst.append(i)
print(lst)

Output:
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
'''

#5> Write a program in python to find greatest among three integers

'''
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3=int(input('Enter third number: '))
if n1>n2 and n1>n3:
    print('n1 is greatest')
elif n2>n1 and n2>n3:
    print('n2 is greatest')
elif n3>n1 and n3>n2:
    print('n3 is greatest')
else:
    print('Three integers are equal ')

Output:
Enter first number: 60
Enter second number: 70
Enter third number: 40
n2 is greatest
'''
#Logical statement

#Q. Given an integer,n, perform the following conditional actions:

#=>If  is odd, print Weird
#=>If  is even and in the inclusive range of  2 to 5 , print "Not Weird"
#=>If  is even and in the inclusive range of 6 to 20, print "Weird"
#=>If  is even and greater than 20, print "Not Weird"

#Input Format:
#------------
#A single line containing a positive integer, n.
#Constraints:
#-----------
#=> 1<=n<=100
#Output Format:
#-------------
#Print "Weird" if the number is weird. Otherwise, print "Not Weird".
#sample input 1:
#------
#    3
#output 1:
#------
#    Weird
#explanation 1:
#------------
#    n=3
#  n is odd and odd numbers are weird, so print "Weird".
#sample input 2:
#------
#    24
#------------------------------or------------------------------------------
#output 2:
#------
#    Not Weird
#explanation 2:
#------------
#    n=24
#   n>20  and nis even,so it is  print " Not Weird"

'''
n=int(input('Enter any number: '))
if n%2!=0:
    print('Weird')
elif n%2==0 and 2<=n<=5:
    print('Not weird')
elif n%2==0 and 6<=n<=20:
    print('Weird')
elif n%2==0 and n>20:
    print('Not Weird')

Output:
Enter any number: 3
Weird
Enter any number: 5
Weird
Enter any number: 6
Weird
'''

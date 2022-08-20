#1>Calculate income tax for the given income by adhering to the below rules
#Taxable Income    Rate (in %)
#First $10,000    0
#Next $10,000    10
#The remaining    20
#Expected Output:

#For example, suppose the taxable income is 45000 the income tax payable is
#10000*0% + 10000*10%  + 25000*20% = $6000.

'''
n=int(input('Enter the amount: '))
print((10000*0/100)+(10000*10/100)+((n-20000)*(20/100)))

Output:Enter the amount: 45000
6000.0
'''

#2> Count the length of list with out using any inbuilt function.

'''
count=0
lst=[1,2,3,4,5,6]
for i in lst:
    count=count+1
print(i)

Output: 6
'''


#3> Write a Python program to create a histogram from a given list of integers.

'''
lst=[1,2,3,4,5]
for i in lst:
    print(i*'*')
Output:
*
**
***
****
*****
'''

#4> Take input from user and if input is string print String
#if input is integer/float print integer
#if input is mix of string and integer print Error
#HINT Can be done using ASCII code

'''
inpt=input("Enter the string: ")
int_count=0
str_count=0
for i in inpt:
    if (ord(i)>48 and ord(i)<57):
        int_count=int_count+1
    elif (ord(i)>97 and ord(i)<122) or (ord(i)>65 and ord(i)<90) :
        str_count=str_count+1
if int_count>0 and str_count ==0:
    print("Integer")
elif int_count== 0 and str_count >0:
    print("String")
else:
    print("Error")

Output:
Enter the string: raju
String
'''


#5> Python program to check if a string is palindrome or not

'''
st=input('Enter any string: ')
if (st==st[::-1]):
    print('Palindrome')
else:
    print('Not Palindrome')

Output: 
Enter any string: wow
Palindrome
Enter any string: hello
Not Palindrome
'''


#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

#Example
#marks key:value pairs are
#'alpha':[20,30,40]
#'beta':[30,50,70]
#query_name='beta'
#2<=n<=10
#0<=marks[i]<=100
#length of marks arrys=3
#The query_name is 'beta'. beta's average score is .

#Input Format
#The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

#Constraints
#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
#Sample Input 0
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output 0
#56.00
#Explanation 0
#marks for Mallika are{52,56,60} whose average is ((52+56+60)/3)=56
#Marks for Malika are  whose average is 
#Sample Input 1
#2
#Harsh 25 26.5 28
#Anurag 26 28 30
#Harsh
#Sample Output 1
#26.50
#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

'''
krishna=[67,68,69]
Arjun =[70,98,63]
Malika=[52,56,60]
krishna_sum=sum(krishna)
krishna_avg=krishna_sum/3
print(round(krishna_avg))
Arjun_sum=sum(Arjun)
Arjun_avg=Arjun_sum/3
print(round(Arjun_avg))
Malika_sum=sum(Malika)
Malika_avg=Malika_sum/3
print(round(Malika_avg))

if((krishna_avg<Arjun_avg) and (krishna_avg<Malika_avg)):
    print('The Minimal avg of krishna is: ', Krishna_avg)
elif ((Arjun_avg<krishna_avg) and (Arjun_avg<Malika_avg)):
    print('The Minimal avg of Arjun is: ', Arjun_avg)
elif ((Malika_avg<krishna_avg) and (Malika_avg<Arjun_avg)):
    print('The Minimal avg of Malika is: ', Malika_avg)
else:
    print('The avg of all members is equal')

Output:
68
77
56
The Minimal avg of Malika is:  56.0
'''


#1> How would you confirm that 2 strings have the same identity?

'''
a='string'
b='string'
print(id(a)==id(b))

Output: True
'''
#2>How would you check if each word in a string begins with a capital letter?

'''
st='ojas innovative'
print(st.capitalize())

Output:
Ojas innovative
'''
#3> Check if a string contains a specific substring

'''
st='Hyderabad HYD'
st1='HYD'
if st1 in st:
    print('Yes')
else:
    print('No')
Output: Yes
'''

#4> Find the index of the first occurrence of a substring in a string

'''
st='Hyderabad hYD'
st1='hYD'

print(st.index('h'))

Output:10
'''

#5> Count the total number of characters in a string

'''
string='Good morning'
count=0
for i in string:
    count=count+1
print(count)

Output: 12
'''

#6> Count the number of a specific character in a string

'''
string='Good morning'
count=0
for i in string:
    if  'o' in i:
        count=count+1
print(count)

Output: 3
'''

#7> Capitalize the first character of a string

'''
string='good morning'
print(string.capitalize())

Output: Good morning
'''
#8> What is an f-string and how do you use it?

'''
f-string make string interpolation really easy
f-string is similar to using format()
'''

#9> Search a specific part of a string for a substring

'''
a='formating'
b='ing'
print(b in a)

Output:True
'''
#10> Interpolate a variable into a string using format()
'''
a='Team'
b='How are you'
print('Hello {} good morning {} '.format(a,b))

Output:
Hello Team good morning How are you
'''
#11> Check if a string contains only numbers

'''
st='full123stack456'
for i in st:
    if i.isnumeric():
        print(i, end=' ')
Output:1 2 3 4 5 6
'''

'''
st='123789'
if st.isnumeric():
    print('Yes')
else:
    print('No')
Output: Yes
'''
#12> Split a string on a specific character

'''
st='Good Morning'
st=st.split('o')
print(st)

Output:
['G', '', 'd M', 'rning']
'''
#13> Check if a string is composed of all lower case characters

'''
a='Fullstack Developer'
print(a.islower())

Output: False
'''
#14> Check if the first character in a string is lowercase

'''
a='Fullstack'
print(a[0].islower())

Output: False
'''

#15> Can an integer be added to a string in Python?
'''
NO
'''

#16> Reverse the string “hello world”

'''
st='hello world'
print(st[::-1])

Output: dlrow olleh
'''
#17> Join a list of strings into a single string, delimited by hyphens

'''
st1='Good'
st2='Morning'
st3='Hyd'
st3=st1+st2+st3
print(st3)

Output:
GoodMorningHyd
'''
#18> Check if all characters in a string conform to ASCI

'''
st='developer'
st1=st.isascii()
print(st1)

Output:True
'''
#19> Uppercase or lowercase an entire string
'''
st='Python Fullstack'
st1=st.upper()
print(st1)

Output:
PYTHON FULLSTACK
'''

#20> Uppercase first and last character of a string

'''
st='developer'
print(st[0].upper()+st[1:8]+st[-1].upper())

Output:
DevelopeR
'''

#21> Check if a string is all uppercase

'''
st='Hello world'
print(st.isupper())
Output:False
'''
#22> When would you use splitlines()?

'''
Representation        Description



\n                Line Feed
\r                Carriage Return
\r\n                Carriage Return + Line Feed
\x1c                File Separator
\x1d                Group Separator
\x1e                Record Separator
\x85               Next Line (C1 Control Code)
\v or \x0b       Line Tabulation
\f or \x0c       Form Feed
\u2028               Line Separator
\u2029              Paragraph Separator
'''

#23> Give an example of string slicing

'''
st='string lines'
st1=st[1:10:2]
print(st1)
Output:tigln
'''
#24> Convert an integer to a string

'''
a=25
b=str(25)
print(b)
print(type(b))
Output:
25
<class 'str'>
'''

#25> Check if a string contains only characters of the alphabet

'''
a='engineer123'
print(a.isalpha())
Output: False
'''
#26> Replace all instances of a substring in a string

'''
st='Python'
st1='developer'
print(st+'  '+st1)

Output:Python  developer
'''

#27> Return the minimum character in a string

'''
st='abcde'
print(min(st))
Output:a
'''

#28> Check if all characters in a string are alphanumeric

'''
st='abcdefg1456'
print(st.isalnum())
Output:True
'''


#29> Remove whitespace from the left, right or both sides of a string

'''
st='    Good morning hyd    '
print(st.strip())
Output:Good morning hyd
'''

#30> Check if a string begins with or ends with a specific character?

'''
st='Engineering'
print(st.startswith('E') and st.endswith('g'))
print(st.startswith('h') and st.endswith('g'))
Output:
True
False
'''





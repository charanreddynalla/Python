
#1>what is a variable in and describe the role of variable in python memory management?

'''
Variables are nothing but reserved memory locations to store values.
This means that when you create a variable you reserve some space in memory.
Based on the data type of a variable,
the interpreter allocates memory and decides what can be stored in the reserved memory.
'''

#2>what are the advantages and disadvantages of type casting?
'''
Advantages:
1)With the help of type casting, you can convert character data type to an int data type.
2)If you are performing conversion between int and character data types then the value of the result will be integer type.
3)Because it is a bigger data type between int and char data types

Disadvantages:
More complex type system.
Source of bugs due to unexpected casts
'''

#3>what is the difference between while loop and for loop?
'''
In a computer programming language,
iteration statements like for loop and while loop and more are used for repeated execution of the instruction in a program.
Both for loop and while loop is used to execute the statements again and again while the program is running.
The major difference between for loop and while loop is that for loop is used when the number of iterations is known whereas,
in the while loop,execution is done until the statement in the program is proved wrong.
'''
#4>write 5 string method with example?

'''
st='good Morning'
st1=st.split()
print(st1)
print(st.startswith('G'))
print(st.isupper())
print(st.index('M'))
print(st.capitalize())

Output:
['good', 'Morning']
False
False
5
Good morning
'''

#5>write the Precedence rule of python with example?
'''
The combination of values, variables, operators,
and function calls is termed as an expression.
The Python interpreter can evaluate a valid expression
>>> 7 - 10
-3
'''

# problem solving
#Write a program to check whether the given password is valid or not .
#conisder the password to be valid if it contain at least one digit ands one capital.

#input:it will be a single line containng string
#output: valid password or invalid password

#ex:GJ22191gopi
#ouput:valid password

'''
password = input("enter the password: ")
number_pass = False
upper_pass = False
for i in password:
    if i.isupper():
        upper_pass = True
    elif i.isnumeric():
        number_pass = True
    if number_pass and upper_pass:
        print("valid password")
        break
else:
    print("not valid password")

#output:enter the password: GJ22191gopi
valid password
enter the password: raju
not valid password
'''





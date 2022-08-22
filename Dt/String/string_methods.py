
#capitalize()  coverts only first character of string to uppercase.
'''
st='fullstack development'
print(st.capitalize())
Output: Fullstack development
'''
#count()
'''
st='fullstack development'
print(st.count('e'))
Output: 3
'''
#startswith()  method returns True if the string starts with the specified value, otherwise False.
'''
st='fullstack development'
print(st.startswith('F'))
Output: False
'''
#endswith()   method returns True if the string ends with the specified value, otherwise False.
'''
st='fullstack development'
print(st.endswith('t'))
Output: True
'''
#index()
'''
st='fullstack development'
print(st.index('e'))
Output: 11
'''
#len()
'''
st='fullstack development'
print(len(st))
Output: 21
'''
#isalpha()  Returns True if all characters in the string are in the alphabet
'''
st='fullstack development'
print(st.isalpha())
Output: False
'''

#isdigit()  Returns True if all characters in the string are digits.
'''
st='Good morning123'
print(st.isdigit())
Output: False
'''
#isalnum()  Returns True if all characters in the string are alphanumeric
'''
st='technology123'
print(st.isalnum())
Output: True
'''

#isascii()
'''
st='string123'
st1='morning'
print(st.isascii())
print(st1.isascii())
Output:
True
True
'''
#upper()   convert whole string to upper.
'''
st='innovative technology'
print(st.upper())
Output: INNOVATIVE TECHNOLOGY
'''
#lower()  coverts whole string to lower.
'''
st='InnovatiVe Technology'
print(st.lower())
Output: innovative technology
'''
#isupper()  if all characters in the string are upper then it returns true.
'''
st='InnovatiVe Technology'
print(st.isupper())
Output: False
'''
#islower()  if all characters in the string are lower then it return False.
'''
st='innovative technology'
print(st.islower())
Output: True
'''
#isspace()
'''
st='innovative technology'
st1='    '
print(st.isspace())
print(st1.isspace())
Output:
False
True
'''
#istitle()  returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
'''
st='innovative technology'
print(st.istitle())
Output: False
'''
#.join()  The join() method takes all items in an iterable and joins them into one string.
'''
st='123'
st1='HYD'
st2=st.join(st1)
print(st2)
Output: H123Y123D
'''
#strip()  method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
'''
st='   good morning   '
print(st.strip())
Output: good morning
'''
#lstrip()  removes left spcaes(begining of spaces)
'''
st='   good morning   '
print(st.lstrip())
Output:
good morning   
'''
#rstrip()  removes right spcaes(ending of spaces)

'''
st='   good morning   '
print(st.rstrip())
Output:
   good morning
'''
#replace()  Returns a string where a specified value is replaced with a specified value
'''
st='good morning'
print(st.replace('o','@'))
Output: g@@d m@rning
'''
#split()  Splits the string at the specified separator, and returns a list
'''
st='good morning'
print(st.split('o'))
Output: ['g', '', 'd m', 'rning']
'''
#swapcase
'''
st='Hyderabad HYD'
print(st.swapcase())
Output: hYDERABAD hyd
'''







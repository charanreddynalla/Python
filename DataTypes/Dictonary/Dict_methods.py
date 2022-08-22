#keys() Returns a list containing the dictionary's keys
'''
dict={'name':'sai', 'age':25,'year':1998}
a=dict.keys()
print(a)
print(dict.keys())

Output:
dict_keys(['name', 'age', 'year'])
dict_keys(['name', 'age', 'year'])
'''
#values()  Returns a list of all the values in the dictionary
'''
dict={'name':'sai', 'age':25,'year':1998}
print(dict.values())

Output:
dict_values(['sai', 25, 1998])
'''
#fromkeys()  Returns a dictionary with the specified keys and value
'''
dict={'name':'sai', 'age':25,'year':1998}
b={}.fromkeys(dict)
print(b)

lst=[10,20,30,40,50]
lst2={}.fromkeys(lst)
print(lst2)

t=(10,20,'sai',60,70)
t1={}.fromkeys(t)
print(t1)

st='python'
st1={}.fromkeys(st)
print(st1)

Output:
{'name': None, 'age': None, 'year': None}
{10: None, 20: None, 30: None, 40: None, 50: None}
{10: None, 20: None, 'sai': None, 60: None, 70: None}
{'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
'''

#get()  Returns the value of the specified key
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
print(dict.get('name'))

Output: sai
'''
#items()  Returns a list containing a tuple for each key value pair
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
print(dict.items())

Output: dict_items([('name', 'sai'), ('age', 25), ('Address', 'Hyd')])
'''
#copy()  copies one  tuple to other tuple
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
print(dict.copy())

Output: {'name': 'sai', 'age': 25, 'Address': 'Hyd'}
'''
#pop()  Removes the element with the specified key
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
print(dict.pop('name'))

Output: sai
'''
#popitem()  Removes the last inserted key-value pair
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
print(dict.popitem())

Output: ('Address', 'Hyd')
'''
#update()  Updates the dictionary with the specified key-value pairs
'''
dict={'name':'sai','age':25,'Address':'Hyd'}
dict.update({'year':1998})
print(dict)

Output:
{'name': 'sai', 'age': 25, 'Address': 'Hyd', 'year': 1998}
'''
#clear()  Removes all the elements from the dictionary
'''
dict={'name': 'sai', 'age': 25, 'Address': 'Hyd', 'year': 1998}
dict.clear()
print(dict)

Output: {}
'''
#setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
'''
dict={'name': 'sai', 'age': 25, 'Address': 'Hyd', 'year': 1998}
print(dict.setdefault('Address'))
Output: Hyd
'''






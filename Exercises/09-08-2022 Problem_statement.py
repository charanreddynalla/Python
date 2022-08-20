#1.Python Program to Print the Natural Numbers Summation Pattern
#Python Program to Print the Natural Numbers Summation Pattern
#Output:
#Case 1:
#Enter a number: 4
#1 = 1
#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 = 10
#Output:
#Case 2:
#Enter a number: 5
#1 = 1
#1 + 2 = 3
#1 + 2 + 3 = 6
#1 + 2 + 3 + 4 = 10
#1 + 2 + 3 + 4 + 5 = 15
'''
n=int(input("Enter a number: "))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep=" ",end=" ")
        if(i<j):
            print("+",sep=" ",end=" ")
        a.append(i)
    print("=",sum(a))
print()

#output:Enter a number: 5
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
1 + 2 + 3 + 4 + 5 = 15
'''




#dict
#keys
'''
dict={'name':'sai', 'age':25,'year':1998}
a=dict.keys()
print(a)
'''
#values
'''
dict={'name':'sai', 'age':25,'year':1998}
b=dict.values()
print(b)
'''
#fromkeys
'''
dict={'name':'sai', 'age':25,'year':1998}
c={}.fromkeys(dict)
print(c)

lst=[10,20,30,40,50]
d={}.fromkeys(lst)
print(d)
'''
#get
'''
dict={'name':'sai', 'age':25,'year':1998}
a=dict.get('age')
print(a)
'''
#items
'''
dict={'name':'sai', 'age':25,'year':1998}
b=dict.items()
print(b)
'''
#pop

'''
dict={'name':'sai', 'age':25,'year':1998}
d=dict.pop('name')
print(d)
print(dict)
'''
#popitem
'''
dict={'name':'sai', 'age':25,'year':1998}
c=dict.popitem()
print(c)
'''
#update
'''
dict={'name':'sai', 'age':25,'year':1998}
dict.update({'Loc':'Hyd'})
print(dict)
'''
#setdefault
'''
dict={'name':'sai', 'age':25,'year':1998}
print(dict.setdefault('year'))
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#string
#2 sets same or not
'''
a='hello'
b='hello'
print(id(a)==id(b))
'''
#string begins with capital
#capitalize
'''
st='good morning'
print(st.capitalize())
'''
#Check if a string contains a specific substring
'''
st='good morning'
st1='good'
if st1 in st:
    print('yes')
'''
#Find the index of the first occurrence of a substring in a string
st='good morning'
st1='hello'
if st1[0] in st:
    print('yes')
else:
    print('no')





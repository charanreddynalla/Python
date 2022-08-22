#append()  Adds an element at the end of the list
'''
lst=[1,2,3,'raju',12.0]
lst1=lst.append(15)
print(lst)
Output: [1, 2, 3, 'raju', 12.0, 15]
'''
#clear()  Removes all the elements from the list
'''
lst=[1,2,3,'raju',12.0]
lst1=lst.clear()
print(lst1)
Output: None
'''
#count()  Returns the number of elements with the specified value
'''
lst=[4,5,6,7,8,9,5,4]
print(lst.count(5))
Output: 2
'''
#extend()  Add the elements of a list (or any iterable), to the end of the current list
'''
lst=[1,2,3,4,5]
lst1=[6,7,8]
lst.extend(lst1)
print(lst)
Output: [1, 2, 3, 4, 5, 6, 7, 8]
'''
#index()  return the position of the element in a given list
'''
lst=[1, 2, 3, 'raju', 12.0, 15]
print(lst.index('raju'))
Output: 3
'''
#insert()  adding the element at specified position
'''
lst=[1, 2, 3, 'raju', 12.0, 15]
lst.insert(2,16)
print(lst)
Output:
[1, 2, 16, 3, 'raju', 12.0, 15]
'''
#pop()  Removes the element at the specified position,if pop()-->removes last element of string,if pop(2)-->removes the specific postion of elements removed in list
'''
lst=[25,35,45,50]
b=lst.pop(2)
print(lst)
print(b)
#Output:
[25, 35, 50]
45
'''
#remove()  Removes specific element in the list
'''
lst=[1, 2, 3, 4, 5, 6, 7, 8]
lst.remove(8)
print(lst)
Output: [1, 2, 3, 4, 5, 6, 7]
'''
#reverse() Reverses the order of the list
'''
lst=[1, 2, 3, 4, 5, 6, 7]
lst.reverse()
print(lst)
Output: [7, 6, 5, 4, 3, 2, 1]
'''
#sort() Sorts the list from ascending to decending
'''
lst=[4,5,6,7,8,9,5,4]
lst1=lst.sort()
print(lst)
'''
#it will come asending order

#del
'''
lst=[4,5,6,7,8,9,5,4]
del(lst)
print(lst)

NameError: name 'lst' is not defined. Did you mean: 'list'?
'''




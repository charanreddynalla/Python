#1>Add a list of elements to a given set
'''
set1={'nani','sai','raju','rajesh'}
set2={60,50,'raju',40}
for i in set1:
    set2.add(i)
print(set2)
Output:
{40, 'raju', 50, 'sai', 'nani', 60, 'rajesh'}
'''



#2> Return a set of identical items from a given two Python
'''
x={20,50,60,80,90,100}
y={30,50,40,90,80,120}
print(x&y)
Output:
{80, 50, 90}
'''

#3> Returns a new set with all items from both sets by removing duplicates

'''
a={10,20,30,40,50}
b={20,50,'sai',40}
print(a.union(b))
Output:
{40, 10, 50, 20, 'sai', 30}
'''


#4> Given two Python sets, update first set with items that exist only in the first set and not in the second set.

'''
a={10,20,30,40,50}
b={20,50,'sai',20.0}
print(a-b)

Output:
{40, 10, 30}
'''


#5> Remove 10, 20, 30 elements from a following set at once

'''
a={10,20,30,40,50,80}
b={10,30,50,40}
a.symmetric_difference_update(b)
print(a)
Output: {80, 20}
'''

#6> Return a set of all elements in either A or B, but not both

'''
a={10,20,30,40,50}
b={20,50,'sai',80}
print(a^b)
Output: {40, 10, 80, 'sai', 30}
'''

#7> Determines whether or not the following two sets have any elements in common. If yes display the common elements

'''
a={10,20,30,40,50}
b={20,50,60,70,20.0}
for i in a:
    if i in b:
        print(i)
Output:
50
20
'''

#8> Update set1 by adding items from set2, except common items

'''
a={10,20,30,40,50}
b={20,50,60,70,20.0}
a.update(b)
print(a)

Output:
{70, 40, 10, 50, 20, 60, 30}
'''

#9> Remove items from set1 that are not common to both set1 and set2

'''
a={10,20,30,40,50}
b={20,50,60,70,20.0}
a.intersection_update(b)
print(a)
Output: {50, 20}
'''

#10> Write a Python program to check if a given set is superset of itself and superset of another given set
'''
a={10,20,30,40,50}
b={20,50,60,70,20.0}
print(a.issuperset(a))
print(a.issuperset(b))
Output:
True
False
'''

#11> Write a Python program to check a given set has no elements in common with other given set

'''
a={10,20,30,40,50}
b={20,50,60,70,20.0}
for i in a:
    if i not in b:
        print(i)
Output:
40
10
30
'''
#12> Write a Python program to remove the intersection of a 2nd set from the 1st set.
'''
a={10,20,30,40,50}
b={20,50,60,70,80}
print(b-a)
Output: {80, 60, 70}
'''

#13> Perform all sets methods by taking an example of your own.

#add()          Adds an element to the set
'''
a={10,20,30,40,50,60}
a.add(70)
print(a)
Output: {50, 20, 70, 40, 10, 60, 30}
'''
#clear()    Removes all the elements from the set
'''
a={10,20,30,40,50,60}
a.clear()
print(a)
Output: set()
'''
#copy()     Returns a copy of the set
'''
a={10,20,30,40,50,60}
a.copy()
print(a)
Output:
{50, 20, 40, 10, 60, 30}
'''
#difference()       Returns a set containing the difference between two or more sets
'''
a={1,2,5,6,7,8}
b={5,4,9,3,5,21}
c=a.difference(b)
print(c)
Output: {1, 2, 6, 7, 8}
'''
#difference_update()    Removes the items in this set that are also included in another, specified set
'''
a={1,2,5,6,7,8,4}
b={5,4,9,3,5,21}
a.difference_update(b)
print(a)
Output: {1, 2, 6, 7, 8}
'''
#discard()  Remove the specified item
'''
a={10,2,30,40,80}
a.discard(80)
print(a)
Output:
{2, 40, 10, 30}
'''
#intersection()   Returns a set, that is the intersection of two or more sets
'''
a={20,30,50,90,80}
b={40,50,80,70}
print(a&b)
Output: {80, 50}
'''
#intersection_update()    Removes the items in this set that are not present in other, specified set(s)
'''
a={20,30,50,90,80}
b={40,50,80,70}
a.intersection_update(b)
print(a)
Output: {80, 50}
'''
#isdisjoint()    Returns whether two sets have a intersection or not

'''
a={20,30,50,90,80}
b={40,50,80,70}
print(a.isdisjoint(b))
Output: False
'''
#issubset()   Returns whether another set contains this set or not
'''
a={20,30,50,90,80}
b={40,50,80,70}
print(a.issubset(b))
print(b.issubset(a))

Output:
False
False
'''
#issuperset()   Returns whether this set contains another set or not

'''
a={20,40,60,70,80}
b={20,40,60,70,80}
print(a.issuperset(b))
print(b.issuperset(a))

Output:
True
True
'''
#pop()	Removes an element from the set
'''
a={20,40,60,70,80}
print(a.pop())
Output: 80
'''
#remove()      Removes the specified element
'''
a={20,40,60,70,80}
a.remove(20)
print(a)
Output:
{80, 70, 40, 60}
'''

#symmetric_difference()     Returns a set with the symmetric differences of two sets
'''
a={10,20,30,'raju',50.0}
b={20,30,True,'nani'}
print(a.symmetric_difference(b))
Output:
{True, 'raju', 10, 50.0, 'nani'}
'''

#symmetric_difference_update()      inserts the symmetric differences from this set and another
'''
a={10,20,30,'raju',50.0}
b={20,30,True,'nani'}
a.symmetric_difference_update(b)
print(a)

Output:
{True, 50.0, 'raju', 'nani', 10}
'''
#union()	Return a set containing the union of sets
'''
a={10,20,30,'raju',50.0}
b={20,30,True,'nani'}
print(a.union(b))
Output:
{True, 'raju', 'nani', 10, 50.0, 20, 30}
'''

#update()	Update the set with another set, or any other iterable

'''
b={20,30,True,'nani'}
b.update({50,60})
print(b)
Output:
{True, 50, 20, 60, 'nani', 30}
'''




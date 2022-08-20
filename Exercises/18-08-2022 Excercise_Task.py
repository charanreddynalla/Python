#1>Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. 
#Input: [19, 19, 15, 5, 3, 5, 5, 2] 
#Output: True 
'''
lst=[19, 19, 15, 5, 3, 5, 5, 2]
if (lst.count(19)==2 and lst.count(5)>=3):
    print('True')
else:
    print('False')
Output: True
'''

#2>WAPP to check a given list of integers where the sum of the integers is equal to length of list. 
'''
lst=[10,20,30,40,50]
print(sum(lst)==len(lst))
Output: False
'''

#3>WAPP to add two integers without using arithmetic operator
'''
a=int(input('Enter any number: '))
b=int(input('Enter any number: '))
count=0
count1=0
sum=0
for i in range(a):
    count=count+1
for j in range(b):
    count1=count1+1
sum=sum+count+count1
print(sum)
Output:
Enter any number: 10
Enter any number: 20
30
'''

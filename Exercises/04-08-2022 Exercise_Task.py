#1.write a python program to print the pattern
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        *

'''
a = int(input("enter the value: "))
for i in range(1,a+1):
    if i == a:
        print("* "*a)
    else:
        spaces = " "*(a-i)
        stars = "* "*i
        print(spaces+stars)
for i in range(2,a+1):
    if i == 2:
        print(" "+"* "*(a-1))
    else:
        spaces = " "*(i-1)
        stars = "* "*(a-i+1)
        print(spaces+stars)
'''
        
#2> How would you check if each word in a string begins with a capital letter?

'''
st='hello good morning'
print(st.title())

Output:
Hello Good Morning
'''
        
#3> Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.

'''
for i in range(0,7):
    if i==4:
        continue
    elif i==5:
        continue
    print(i, end=' ')

Output: 0 1 2 3 6 
'''
      
#4> Print list of elements and store in a another list and print  reverse order of list

'''
lst=[1,2,3,4,5,6,7,8]
lst1=lst
print(lst1[::-1])

Output: [8, 7, 6, 5, 4, 3, 2, 1]
'''
        
#5> write a python program to print the pattern
#            A  
#           B C  
#          D E F  
#         G H I J  
#        K L M N O  
#       P Q R S T U

'''
a = int(input("enter the number: "))
count = 65
k = 2*(a)-2
for i in range(0,a):
    for j in range(0,k):
        print(end = " ")
    k = k-1
    for j in range(0,i+1):
        alpha = chr(count)
        print(alpha,end =" ")
        count += 1
    print(" ")
Output:
enter the number: 6
          A  
         B C  
        D E F  
       G H I J  
      K L M N O  
     P Q R S T U  
'''

#Problem statement
#Write a Python program to find the strings in a given list, starting with a given prefix.
#Input:
#[( ca,('cat', 'car', 'fear', 'center'))]
#Output:
#['cat', 'car']
#Input:
#[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
#Output:
#['dog', 'donut']

'''
lst=['cat', 'car', 'fear', 'center']
lst1=[]
for i in lst:
    if (i[0]=='c' and i[1]=='a'):
        lst1.append(i)
print(lst1)

Output: ['cat', 'car']
'''




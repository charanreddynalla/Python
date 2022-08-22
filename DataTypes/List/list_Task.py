#1>Take 10 integer inputs from user and store them in a list and print them on screen.

'''
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        lst.append(a)
print(lst)

Output:
Enter any number: 10
Enter any number: 20
Enter any number: 30
Enter any number: 40
Enter any number: 50
Enter any number: 60
Enter any number: 70
Enter any number: 80
Enter any number: 90
Enter any number: 100
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''

#2>Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.( Iterate over list using while loop ).

'''
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        lst.append(a)
print(lst)
b=int(input('Enter any number: '))
if b in lst:
    print('Number in list')
else:
    print('Not in list')

Output:
Enter any number: 10
Enter any number: 20
Enter any number: 30
Enter any number: 40
Enter any number: 30
Enter any number: 20
Enter any number: 80
Enter any number: 90
Enter any number: 70
Enter any number: 50
[10, 20, 30, 40, 30, 20, 80, 90, 70, 50]
Enter any number: 50
Number in list
'''

#3> #Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.

'''
positive=0
negitive=0
odd=0
even=0
equal=0
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        lst.append(a)
for b in lst:
    if b>0:
        positive=positive+1
for b in lst:
    if b<0:
        negitive=negitive+1
for b in lst:
    if b%2==0:
        even=even+1
for b in lst:
    if b%2!=0:
        odd=odd+1
for b in lst:
    if equal==0:
        equal=equal+1
            
print('positive:',  positive, 'negitive:' , negitive, 'even:', even, 'odd:' , odd, 'equal:' , equal)

Output:
Enter any number: -20
Enter any number: -41
Enter any number: 20
Enter any number: 11
Enter any number: 99
Enter any number: 60
Enter any number: 50
Enter any number: -22
Enter any number: 23
Enter any number: 40
positive: 7 negitive: 3 even: 6 odd: 4 equal: 1
'''
#4>Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

'''
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        lst.append(a)
print(lst)
lst2=lst
print(lst2[::-1])

Output:
Enter any number: 10
Enter any number: 20
Enter any number: 30
Enter any number: 40
Enter any number: 50
Enter any number: 60
Enter any number: 70
Enter any number: 80
Enter any number: 90
Enter any number: 32
[10, 20, 30, 40, 50, 60, 70, 80, 90, 32]
[32, 90, 80, 70, 60, 50, 40, 30, 20, 10]
'''

#5>Write a program to find the sum of all elements of a list.

'''
lst=[2,3,5,6,7,8,9]
print(sum(lst))

Output:40
'''
#6>Write a program to find the product of all elements of a list.

'''
lst=[2,3,4,5,6]
count=1
for i in lst:
    count=count*i
print(count)

Output: 720
'''

#7> Initialize and print each element in new line of a list inside list.

'''
a=[1,2,3,4,5,6]
b=str(a)
c=b.split(',')
for i in c:
    print(i,"\n")
Output:
[1 

 2 

 3 

 4 

 5 

 6] 
'''

#8>Find largest and smallest elements of a list.

'''
lst=[2,5,8,9,6,3,10]
print(min(lst))
print(max(lst))

Output:
2
10
'''

#9>Write a program to print sum, average of all numbers, smallest and largest element of a list.

'''
lst=[10,20,53,60,70,88,11]
sum=sum(lst)
print(sum)
avg=sum/7
print(avg)
print(min(lst))
print(max(lst))

Output:
312
44.57142857142857
10
88
'''
#10>Write a program to check if elements of a list are same or not it read from front or back.
#E.g: 2	3	15	15	3	2

'''
lst=[2,3,15,15,3,2]
reverse=lst[::-1]
if reverse==lst:
    print('Same')
else:
    print('No')

Output:Same
'''

#11> Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
#INITIAL list :
#58	24	13	15	63	9	8	81	1	78

#After spliting :
#58	24	13	15	63
#9	8	81	1	78

'''
lst=[58,24,13,15,63,9,8,81,1,78]
lst1=lst[0:5]
lst2=lst[5:]
print(lst1)
print(lst2)

Output:
 [58, 24, 13, 15, 63]
[9, 8, 81, 1, 78]
'''
#12>Ask user to give integer inputs to make a list. Store only even values given and print the list.

'''
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        if a%2==0:
            lst.append(a)
print(lst)

Output:
Enter any number: 12
Enter any number: 57
Enter any number: 62
Enter any number: 35
Enter any number: 67
Enter any number: 59
Enter any number: 52
Enter any number: 20
Enter any number: 30
Enter any number: 50
[12, 62, 52, 20, 30, 50]
'''




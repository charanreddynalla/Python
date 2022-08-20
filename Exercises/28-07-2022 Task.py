#1>WAP in python arrange string characters such that lowercase letters should come first

'''
st='PythonFullStack'
lower=[]
upper=[]
for i in st:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
st1=' '.join(lower+upper)
print(st1)

Output:
y t h o n u l l t a c k P F S
'''

#2>WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17

'''
lst=[2,4,5,6,7,3,8]
sum=0
for i in lst:
    prime=0
    for j in range(2,i-1):
        if i%j==0:
            prime=prime+1
    if prime==0 and i!=1:
        sum=sum+i
print(sum)

Output:17
'''

#3>when do we use nested for loop.Write an example.

'''
The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''   


#4>WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )

'''
st='H56U1E9JIG3l4w2'
b=' '
for i in st:
    if i.isdigit():
        b=b+i
print(b)
    
Output:
5619342
'''

#5>WAP to take a list and find the possition of the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)

'''
lst=[45,12,66,2,33]
print('The index of  66 is: ',lst.index(66))

Output:
The index of  66 is:  2
'''

#Problem statement

#Python Program to accept three distinct digits and print all possible combinations from the digits.

#Case 1:
#Enter first number:1
#Enter second number:2
#Enter third number:3
#1 2 3
#1 3 2
#2 1 3
#2 3 1
#3 1 2
#3 2 1

#Case 2:
#Enter first number:5
#Enter second number:7
#Enter third number:3
#5 7 3
#5 3 7
#7 5 3
#7 3 5
#3 5 7
#3 7 5

'''
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

Enter first number:3
Enter second number:7
Enter third number:5
3 7 5
3 5 7
7 3 5
7 5 3
5 3 7
5 7 3
'''





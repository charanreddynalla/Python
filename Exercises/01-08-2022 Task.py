#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?
'''
a = [1,5,7,8,90,6,23]
if 5 in a:
    print("yes")
else:
    print("No")
#output: yes
'''

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?

'''
a = [1,5,7,8,90,6,23]
b = []
while a:
    min = a[0]
    for i in a:
        if i<min:
            min = i
    b.append(min)
    a.remove(min)
print(b)
#output:[1, 5, 6, 7, 8, 23, 90]
'''




#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum.
#  and display the total amount to pay on  the end of the year.?

'''
p=10000
r=5
t=3
ci=10000*((1+5/100)**3)
print(ci)

Output:
11576.250
'''

#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]], where x1,x2....x9 values must take from command-line
#   arguments?
# 1 2 3
#    4 5 6  
#    7 8 9   

'''
'a = []
for i in range(1,10):
    a.append(i)
s = 0
for i in a:
    s = s+i
print("sum of matrix: ",s)
#output:45
'''


#5. WAP pattern program

'''
  * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *
     a = int(input("enter the value: "))
for i in range(1,a+1):
    if i == 1:
        print("* "*a)
    else:
        space = " "*(i-1)
        print(space+"* "*(a-(i-1)))
for i in range(2,a+1):
    if i ==a:
        print("* "*a)
    else:
        space= " "*(a-i)
        print(space+"* "*(i))
'''


#1>WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?
'''
lst=[23,67,45,89,65,12,15,19]
lst1=[]
for i in lst:
    if i>=65:
        lst1.append(i)
        lst1.sort()
print(lst1)
Output:
[65, 67, 89]
'''

#2> WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#                   7   9  3
#                   12   5  67
#result:=>53
'''
a = [[1,2,3],[7,9,3],[12,5,67]]
i = 0
j = 0
leftdig_sum = 0
rightdig_sum = 0
while(i<len(a)):
    leftdig_sum +=a[i][j]
    i += 1
    j += 1
    
i = 0
j = len(a)-1
while(i<len(a)):
    rightdig_sum += a[i][j]
    i += 1
    j -= 1
print(abs(leftdig_sum-rightdig_sum))
'''

#3> WAP to solve this pattern
#     A
#     A B
#     A B C
#     A B C D
#     A B C D E
#     A B C D
#     A B C
#     A B
#     A   

'''
a=int(input('Enter any value: '))
k=65
for i in range(a):
    for j in range(i+1):
        print(chr(k+j), end=' ')
    print()
for i in range(a):
    for j in range(a-i-1):
        print(chr(k+j), end=' ')
    print()
'''






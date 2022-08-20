#1>Python Program to Return the Length of the Longest Word from the List of Words
#Problem Description:
#The program takes a list of words and returns the word with the longest length.
#Runtime Test Cases:
#Case 1:
#Enter the number of elements in list:4
#Enter element1:"Apple"
#Enter element2:"Ball"
#Enter element3:"Cat"
#Enter element4:"Dinosaur"
#The word with the longest length is:
#Dinosaur
 
#Case 2:
#Enter the number of elements in list:3
#Enter element1:"Bangalore"
#Enter element2:"Mumbai"
#Enter element3:"Delhi"
#The word with the longest length is:
#Bangalore

'''
lst = ["Apple","ball","cat","dinosar"]
max = len(lst[0])
temp = lst[0]
for i in lst:
    if(len(i)>max):
        max=len(i)
        temp = i
print(temp)
    
Output: dinosar
'''

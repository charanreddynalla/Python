#1> WAP to print middle charactor of the string
'''
st='Fullstack'
print(st[5])

Output: t
'''
#2>WAP to print half reverse of the string
#Input: KNOWLEDGE
#Output: EGDELKNOW

'''
st='KNOWLEDGE'
st1=st[-1:-6:-1]
st2=st[0:4]
print(st1+st2)
'''
#3>WAP to remove all the vowels from the given string
'''
a='Hyderabad'
a1='AEIOUaeiou'
for i in a:
    if i not in a1:
        print(i, end=' ')

Output: H y d r b d
'''
#4>WAP to insert * in front of every vouels in the string.
#Input: BANANA
#Output: B*AN*AN*A

'''
string='BANANA'
v='AEIOU'
for i in string:
    if i in v:
        print('*'+i, end=' ')
    else:
        print(i, end=' ')
Output:
B *A N *A N *A
'''

#5>WAP to count number of words in the string.

'''
st='python fullstack developer'
st=st.split()
print(len(st))

Output: 3
'''
#6>WAP to remove extra space from the given string 

'''
a='   Good morning hyd   '
print(a.strip())

Output:Good morning hyd
'''
#7>WAP to insert string in between the given string
#Input: Ojas technologies 
#Output: Ojas innovative technologies

'''
st='Ojas technologies '
st=st.split()
st1='innovative'
print(st[0]+'  '+st1+'  '+st[1])

Output:
Ojas  innovative  technologies
'''

#8>WAP to find the ascci value of given char

'''
st='b'
print(ord(st))
st1='A'
print(ord(st1))

Output:
98
65
'''
#9>insert ojas in front of every string

'''
st='Good morning hyd'
st=st.split()
st1='ojas'
print(st1+st[0]+' '+st1+st[1]+' '+st1+st[2])

Output:
ojasGood ojasmorning ojashyd
'''

#10>insert ojas in every extra space in the string

'''
a='   Good morning  '
b='ojas'
print(a.replace(' ',b))

Output:
ojasojasojasGoodojasmorningojasojas
'''


















        

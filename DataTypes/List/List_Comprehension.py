#1>Find all of the numbers from 1-1000 that are divisible by 7
'''
print([i for i in range(1000) if i%7==0])
Output:
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308,
315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595,
602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700,707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882,
889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]
'''

#2>Find all of the numbers from 1-1000 that have a 3 in them
'''
print([i for i in range(1000) if '3' in str(i)])

Output:
[3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93, 103, 113, 123, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 143, 153, 163, 173, 183, 193, 203, 213, 223, 230, 231, 232, 233, 234, 235,
 236, 237, 238, 239, 243, 253, 263, 273, 283, 293, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331,
 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373,
 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 403, 413, 423, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 443, 453,
 463, 473, 483, 493, 503, 513, 523, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 553, 563, 573, 583, 593, 603, 613, 623, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 643, 653, 663, 673, 683, 693,
 703, 713, 723, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 743, 753, 763, 773, 783, 793, 803, 813, 823, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 843, 853, 863, 873, 883, 893, 903, 913, 923, 930,
 931, 932, 933, 934, 935, 936, 937, 938, 939, 943, 953, 963, 973, 983, 993]
'''

#3>Count the number of spaces in a string
'''
st='hi hello good morning hope doing good'
st1=[i for i in st if i==' ']
print(len(st1))
Output: 6
'''

#4>Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
'''
st='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'
v='aeiouAEIOU'
print([i for i in st if i not in v if i!=' '])
Output:
['Y', 'l', 'l', 'w', 'Y', 'k', 's', 'l', 'k', 'y', 'l', 'l', 'n', 'g', 'n', 'd', 'y', 'w', 'n', 'n', 'g', 'n', 'd', 'y', 's', 't', 'r', 'd', 'y', 't', 'h', 'y', 'y', 'd', 'l', 'd', 'w', 'h', 'l', 't', 'n', 'g', 'y', 'k', 'y', 'y', 'm', 's']
'''
#5>Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
'''
lst=['hi', 4,8.99, 'apple', ('t,b','n')]
print([(i,j)for i,j in enumerate(lst)])
Output:
[(0, 'hi'), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t,b', 'n'))]
'''
#6>Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
'''
lst1=[1,2,3,4]
lst2=[2,3,4,5]
print([i for i in lst1 for j in lst2 if i==j])

Output:
[2, 3, 4]
'''

#7>Get only the numbers in a sentence like ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
'''
st='In 1984 there were 13 instances of a protest with over 1000 people attending'
num='0-9'
print([i for i in st.split()  if i.isdigit()])
print([i for i in st if i.isdigit()])
Output:
['1984', '13', '1000']
['1', '9', '8', '4', '1', '3', '1', '0', '0', '0']
'''

#8>Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
'''
print(['even' if i%2==0 else 'odd' for i in range(20)])
Output:
['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
'''

#9>Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
'''
a=[1,2,3,4,5,6,7,8,9]
b=[2,7,1,12]
print(tuple((i,j) for i in a for j in b if i==j))
Output:
((1, 1), (2, 2), (7, 7))
'''

#10>Find all of the words in a string that are less than 4 letters
'''
st='hi hello good mgr how are you'
print([i for i in st.split() if len(i)<4])
Output:
['hi', 'mgr', 'how', 'are', 'you']
'''
#11>Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
'''
print([i for i in range(1,1000) for j in range(12,20) if i%j==0])

Output:
[12, 13, 14, 15, 16, 17, 18, 19, 24, 26, 28, 30, 32, 34, 36, 36, 38, 39, 42, 45, 48, 48, 51, 52, 54, 56, 57, 60, 60, 64, 65, 68, 70, 72, 72, 75, 76, 78, 80, 84, 84, 85, 90, 90, 91, 95, 96, 96, 98, 102, 104, 105, 108,
 108, 112, 112, 114, 117, 119, 120, 120, 126, 126, 128, 130, 132, 133, 135, 136, 140, 143, 144, 144, 144, 150, 152, 153, 154, 156, 156, 160, 162, 165, 168, 168, 169, 170, 171, 176, 180, 180, 180, 182, 182,
 187, 190, 192, 192, 195, 195, 196, 198, 204, 204, 208, 208, 209, 210, 210, 216, 216, 221, 221, 224, 224, 225, 228, 228, 234, 234, 238, 238, 240, 240, 240, 247, 247, 252, 252, 252, 255, 255, 256, 260,
 264, 266, 266, 270, 270, 272, 272, 273, 276, 280, 285, 285, 286, 288, 288, 288, 289, 294, 299, 300, 300, 304, 304, 306, 306, 308, 312, 312, 315, 320, 322, 323, 323, 324, 324, 325, 330, 336, 336, 336, 338,
 340, 342, 342, 345, 348, 350, 351, 352, 357, 360, 360, 360, 361, 364, 364, 368, 372, 374, 375, 377, 378, 378, 380, 384, 384, 390, 390, 391, 392, 396, 396, 399, 400, 403, 405, 406, 408, 408, 414, 416, 416,
 418, 420, 420, 420, 425, 429, 432, 432, 432, 434, 435, 437, 442, 442, 444, 448, 448, 450, 450, 455, 456, 456, 459, 462, 464, 465, 468, 468, 468, 475, 476, 476, 480, 480, 480, 481, 486, 490, 492, 493,
 494, 494, 495, 496, 504, 504, 504, 507, 510, 510, 512, 513, 516, 518, 520, 522, 525, 527, 528, 528, 532, 532, 533, 540, 540, 540, 544, 544, 546, 546, 551, 552, 555, 558, 559, 560, 560, 561, 564, 570, 570,
 572, 574, 576, 576, 576, 578, 585, 585, 588, 588, 589, 592, 594, 595, 598, 600, 600, 602, 608, 608, 611, 612, 612, 612, 615, 616, 624, 624, 624, 627, 629, 630, 630, 630, 636, 637, 640, 644, 645, 646, 646,
 648, 648, 650, 656, 658, 660, 660, 663, 663, 665, 666, 672, 672, 672, 675, 676, 680, 684, 684, 684, 686, 688, 689, 690, 696, 697, 700, 702, 702, 703, 704, 705, 708, 714, 714, 715, 720, 720, 720, 720, 722,
 728, 728, 731, 732, 735, 736, 738, 741, 741, 742, 744, 748, 750, 752, 754, 756, 756, 756, 760, 765, 765, 767, 768, 768, 770, 774, 779, 780, 780, 780, 782, 784, 784, 792, 792, 793, 795, 798, 798, 799, 800, 804,
 806, 810, 810, 812, 816, 816, 816, 817, 819, 825, 826, 828, 828, 832, 832, 833, 836, 840, 840, 840, 845, 846, 848, 850, 852, 854, 855, 855, 858, 864, 864, 864, 867, 868, 870, 871, 874, 876, 880, 882, 882,
 884, 884, 885, 888, 893, 896, 896, 897, 900, 900, 900, 901, 910, 910, 912, 912, 912, 915, 918, 918, 923, 924, 924, 928, 930, 931, 935, 936, 936, 936, 938, 944, 945, 948, 949, 950, 952, 952, 954, 960,
 960, 960, 962, 966, 969, 969, 972, 972, 975, 975, 976,980, 984, 986, 988, 988, 990, 990, 992, 994, 996]
'''
#12>Turn every item of a list into its square 
#Concatenate two lists index-wise list1 = ["M", "na", "i", "Ke"] 
#list2 = ["y", "me", "s", "lly"] 
#Expected output: ['My', 'name', 'is', 'Kelly'] 
#['My', 'name', 'is', 'Kelly'] list1 = ["Hello ", "take "] 
#list2 = ["Dear", "Sir"] 
#Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''
ls1 = ["Hello ", "take "] 
ls2 = ["Dear", "Sir"] 

print([ls1[i]+ls2[j] for i in range(len(ls1)) for j in range(len(ls1)) ])
Output:
['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
'''

#13>Extend nested list by adding the sublist 
#list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
# sub list to add 
#sub_list = ["h", "i", "j"] 
#Expected Output: 
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)
Output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''
#14>Finding Transpose of a Matrix using List Comprehension matrix = [[1, 2], [3,4], [5,6], [7,8]] o/p: [[1, 3, 5, 7], [2, 4, 6, 8]]
'''
m = [[1, 2], [3,4], [5,6], [7,8]] 
print([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])
Output:
[[1, 3, 5, 7], [2, 4, 6, 8]]
'''
#15>Reverse each String in a Tuple
'''
t=('animal','dog','hello',4,5)
print([i[::-1] for i in t if type(i) is str])
Output:
['lamina', 'god', 'olleh']
'''





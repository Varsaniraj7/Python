list1 = [1, "hi", "Python", 2]
#Checking type of given list
print(type(list1))
#Printing the list1
print (list1)
# List slicing
print (list1[3:])
# List slicing
print (list1[0:2])
# List Concatenation using + operator
print (list1 + list1)
# List repetation using * operator
print (list1 * 3)

tup = ("hi", "Python", 2)
# Checking type of tup
print (type(tup))
#Printing the tuple
print (tup)
# Tuple slicing
print (tup[1:])
print (tup[0:1])
# Tuple concatenation using + operator
print (tup + tup)
# Tuple repatation using * operator
print (tup * 3)
# Adding value to tup. It will throw an error.
# t[2] = "hi"





d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}
# Printing dictionary
print (d)
# Accesing value using keys
print("1st name is "+d[1])
print("2nd name is "+ d[4])
print (d.keys())
print (d.values())






print(type(True))
print(type(False))
print(False)








# Creating Empty set
set1 = set()
set2 = {'James', 2, 3,'Python'}
#Printing Set value
print(set2)
# Adding element to the set
set2.add(10)
print(set2)
#Removing element from the set
set2.remove(2)
print(set2)





k = [1, 3, 4, 6] # all values true
print(all(k))
k = [0, False] # all values false
print(all(k))
k = [1, 3, 7, 0] # one false value
print(all(k))
k = [0, False, 5] # one true value
print(all(k))
k = [] # empty iterable
print(all(k))



x = 10
y = bin(x)
print (y)





test1 = []
print(test1,'is',bool(test1))
test1 = [0]
print(test1,'is',bool(test1))
test1 = 0.0
print(test1,'is',bool(test1))
test1 = None




s = sum([1, 2,4 ])
print(s)
s = sum([1, 2, 4], 10)
print(s)





x = 8
print(eval('x + 1'))





# for integers
print(float(9))
# for floats
print(float(8.19))




age = 22
globals()['age'] = 22
print('The age is:', age)




# list of numbers
list = [1,2,3]
listIter = iter(list)
# prints '1'
print(next(listIter))
# prints '2'
print(next(listIter))
# prints '3'
print(next(listIter))





strA = 'Python'
print(len(strA))


# List = [1,2,3,4,5]
# print(list(List))



python = object()
print(type(python))
print(dir(python))




# # opens python.text file of the current directory
# f = open("python.txt")
# # specifying full path
# f = open("C:/Python33/README.txt")






# Python program to show how to access tuple elements
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Collection")
print(tuple_[0])
print(tuple_[1])
# trying to access element index more than the length of a tuple
try:
    print(tuple_[5])
except Exception as e:
    print(e)
# trying to access elements through the index of floating data type
try:
    print(tuple_[1.0])
except Exception as e:
    print(e)
# Creating a nested tuple
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))
# Accessing the index of a nested tuple
print(nested_tuple[0][3])
print(nested_tuple[1][1])





# Python program to show how negative indexing works in Python tuples
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Collection")
# Printing elements using negative indices
print("Element at -1 index: ", tuple_[-1])
print("Elements between -4 and -1 are: ", tuple_[-4:-1])






# Python program to show how slicing works in Python tuples
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")
# Using slicing to access elements of the tuple
print("Elements between indices 1 and 3: ", tuple_[1:3])
# Using negative indexing in slicing
print("Elements between indices 0 and -4: ", tuple_[:-4])
# Printing the entire tuple by using the default start and end values.
print("Entire tuple: ", tuple_[:])






# repetition in tuples
tuple_ = ('Python',"Tuples")
print("Original tuple is: ", tuple_)
# Repeting the tuple elements
tuple_ = tuple_ * 3
print("New tuple is: ", tuple_)






# Creating tuples
T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
T2 = ('python', 'java', 'python', 'Tpoint', 'python', 'java')
# counting the appearance of 3
res = T1.count(2)
print('Count of 2 in T1 is:', res)
# counting the appearance of java
res = T2.count('java')
print('Count of Java in T2 is:', res)






# Creating tuples
Tuple_data = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# getting the index of 3
res = Tuple_data.index(3)
print('First occurrence of 1 is', res)
# getting the index of 3 after 4th
# index
res = Tuple_data.index(3, 4)
print('First occurrence of 1 after 4th index is:', res)






# membership test for tuples
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")
print('Tuple' in tuple_) # In operator
print('Items' in tuple_)
print('Immutable' not in tuple_) # Not in operator
print('Items' not in tuple_)








# iterate over tuple elements
# Creating a tuple
tuple_ = ("Python", "Tuple", "Ordered", "Immutable")
# Iterating over tuple elements using a for loop
for item in tuple_:
    print(item)










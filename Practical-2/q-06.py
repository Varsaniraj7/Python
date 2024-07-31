# Write a program to find maximum from 3 given nnumber
n1 = int(input("Enter num 1 : "))
n2 = int(input("Enter num 2 : "))
n3 = int(input("Enter num 3 : "))

if n1 > n2 and n1 > n3:
    maximum = n1
if n2>n1 and n2>n3:
    maximum = n2
if n3>n1 and n3>n2:
    maximum = n3
print ("Maximum: " , maximum)
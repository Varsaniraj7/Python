# swapping operations between two numbers without using any variables

a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
print("Before swapping a =", a, "and b =", b)
a,b=b,a
print("After swapping a =", a, "and b =", b)





# Swapping operations between two numbers using the temp variable

a=int(input("Enter a number : "))
b=int(input("Enter b number : "))
print("Before swapping a =", a, "and b =", b)
temp = a
a = b   
b = temp
print("After swapping a =", a, "and b =", b)
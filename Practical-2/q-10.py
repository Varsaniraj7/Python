#   1
#  22
# 333
for i in range(1,4):
    for l in range(i,4):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#   *
#  **
# ***
for i in range(1,4):
    for l in range(i,4):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#   1
#  12
# 123

for i in range(1,4):
    for j in range(i,3):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()





# Practice Program 


# *
# * *
# * * *
# * * * *
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()



#       * 
#     *   *
#   *   *   *
# *   *   *   *
for i in range(1,5):
    for j in range(4-i):
        print("  ",end=" ")
    for k in range(i):
        print("  *  ",end=" ")
    print()
print()


# * * * *
# * * *
# * *
# *
for i in range(5):
    for j in range(i,4):
        print("*",end=" ")
    print()


# *   *   *   *
#   *   *   *
#     *   *
#       * 
for i in range(5):
    for j in range(i):
        print("  ",end=" ")
    for k in range(i,4):
        print("  *  ",end=" ")
    print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num = 1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num += 1
    print()
print()


# 1
# 1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print()


# 1 2 3 4
# 1 2 3
# 1 2 
# 1

for i in range(4,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()



#         1
#       2 1 
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1

for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i,0,-1):
        print(k,end=" ")
    print()
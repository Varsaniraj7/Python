# Create List
Branch = ["computer", "mechanical", "Electrical", "Civil", "Automobile"]
print (Branch)
print (type(Branch))

# Access Elements
print (Branch[3])
print (Branch[-3])

# Append Elements
Branch.append("IT")
print (Branch)

# Update Elements
Branch[5] = "ITI"
print (Branch)

# Delete Elements
Branch.remove("ITI")
print (Branch)

# Length of List
print (len(Branch))

# Iterate Elements
for k in Branch:
    print (k)
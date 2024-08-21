# Set Program
s = {"computer", "mechanical", "civil", "eletrical", "automobile"}
print (s)
print (type(s))

# Add element
s.add("Metatronic")
print (s)

# Update element 
s.update(["Plastic", "ITI"])
print (s)

# Traverse elements
for i in s:
    print (i)

# Remove element
s.discard("Metatronic")
s.discard("ITI")
print (s)

# Clear all elements
s.clear()
print (s)


# union & intersection
set1 = {1,2,3,4}
set2 = {5,4,6}
print ("Union of set1 and set2: ", set1|set2)
print ("Intersection of set1 and set2: ", set1&set2)
# This code demonstrates how to manipulate strings in Python.
name = "HARRY"
nameshort = name[0:2] #it can also be written as name[-4:-3]
print(nameshort)
# For printing a specific character from the string
# A string value is 0,1,2,3,4....n or -5,-4,-3,-2,-1...n
character = name[1] 
print(character)
# For printing a specific character from the string using negative indexing
character = name[-1]
print(character)
# String Functions
name = "harry"
print(len(name)) # Length of the string
print(name.endswith("rry")) # Check if the string ends with "rry"
print(name.startswith("ha")) # Check if the string starts with "Ha"
print(name.capitalize()) # Capitalize the first letter of the string

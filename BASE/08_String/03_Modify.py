# Upper Case
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# Lower Case
print(a.lower())
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, 
# and very often you want to remove this space.
a = "    Hello, World!   "
print(a) 
print(a.strip()) # returns "Hello, World!"

# Replace String
# The replace() method replaces a string with another string:
print(a.replace("H", "J"))
a = "Hello, World!"

# Split String
# The split() method returns a list where the 
# text between the specified separator becomes the list items.
print(a.split(",")) # returns ['Hello', ' World!']
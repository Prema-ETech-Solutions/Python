"""
Strings in python are surrounded by either single quotation marks, 
or double quotation marks.

'hello' is the same as "hello".  
"""
print("Hello")
print("Hello")

# Assigning a string to a variable is done with
# the variable name followed by an equal sign and the string:
a = "Hello"
print(a)
print("\n")

"""
Multiline Strings
You can assign a multiline string to a variable by using three quotes:  
"""
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n")

# Or three single quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
print("\n\n")

"""
Strings are Arrays
Like many other popular programming languages, 
strings in Python are arrays of bytes representing unicode characters.

However, 
Python does not have a character data type, 
a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string  
"""
a = "Hello, World!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])
print(a[11])
print(a[12])
print("\n\n")

"""
Looping Through a String
Since strings are arrays, 
we can loop through the characters in a string, 
with a for loop.
"""

for x in "Apple":
    print(x)

print("\n\n")
# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))
print("\n")



"""
Check String
To check if a certain phrase or character is present in a string, 
we can use the keyword in. 
"""
txt = "The best things in life are free!"
print("free" in txt)

# To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword not in.
print("expensive" not in txt)

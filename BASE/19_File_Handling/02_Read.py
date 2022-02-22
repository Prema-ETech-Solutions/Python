# To open the file, use the built-in open() function.
# The open() function returns a file object, 
# which has a read() method for reading the content of the file:
f = open("Sample.txt", "r")

# print(f.read(),"\n")

"""

Read Only Parts of the File
By default the read() method returns the whole text,
but you can also specify how many characters you want to return:
"""
# print(f.read(5))


# Read Lines
# You can return one line by using the readline() method:
# print(f.readline())



# By looping through the lines of the file, 
# you can read the whole file, line by line:
for x in f:
  print(x)
f.close() #It is a good practice to always close the file when you are done with it.

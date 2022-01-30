"""  
Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print("\n\n")

"""
Negative Indexing
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.  
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print("\n\n")

""" 
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items. """
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print("\n\n")


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
print("\n\n")



"""
Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the tuple:  
"""
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
print("\n\n")

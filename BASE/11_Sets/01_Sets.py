my_set= {"Hello","World","!"}
"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and un-indexed.  
"""
print(my_set)


"""
Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.  
"""
""" 
Duplicates Not Allowed
Sets cannot have two items with the same value.
"""
my_set1= {"Hello","World","!","Hello","World","!"}
print(my_set)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
print(len(my_set))


"""
type()
From Python's perspective, sets are defined as objects with the data type 'set':

<class 'set'>  
"""
print(type(my_set))

"""  
The set() Constructor
It is also possible to use the set() constructor to make a set.
"""
new_Set= set(("H","E","L","L","O"))
print(new_Set)

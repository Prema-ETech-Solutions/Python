"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, 
the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
"""
mytuple = ("apple", "banana", "cherry")
"""
Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:  
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)

"""
Tuple Length
To determine how many items a tuple has, use the len() function:  
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

"""
Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, 
otherwise Python will not recognize it as a tuple.  
"""
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# From Python's perspective, tuples are defined as objects with the data type 'tuple':
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
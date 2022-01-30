"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python 
used to store collections of data, the other 3 are Tuple, 
Set, and Dictionary, all with different qualities 
and usage.

Lists are created using square brackets:  
"""
Fruits = ["apple", "banana", "cherry"]
print(Fruits)
"""
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, 
the first item has index [0], 
the second item has index [1] etc.  
"""

"""
Ordered
When we say that lists are ordered, 
it means that the items have a defined order, 
and that order will not change.

If you add new items to a list, 
the new items will be placed at the end of the list. 

Changeable
The list is changeable, meaning that we can change, add, 
and remove items in a list after it has been created.
"""


"""
Allow Duplicates
Since lists are indexed, lists can have items with the same value:  
"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

"""
List Length
To determine how many items a list has, use the len() function: 
"""
thislist = ["L1", "L2", "L3","L4"]
print(len(thislist))
print(thislist)
print("\n\n")



# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)


# type()
print(type(list1))





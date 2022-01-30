"""
Append Items
To add an item to the end of the list, use the append() method:  
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.append("orange")
print(thislist)
print("\n\n")

"""
Extend List
To append elements from another list to the current list, use the extend() method.
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print("\n\n")

"""
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).  
"""
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

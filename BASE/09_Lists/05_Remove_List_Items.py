"""
Remove Specified Item
The remove() method removes the specified item. 
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)
print("\n\n")


"""
Remove Specified Index
The pop() method removes the specified index.
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print("\n\n")
# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
print("\n\n")



"""
Clear the List
The clear() method empties the list.

The list still remains, but it has no content.  
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


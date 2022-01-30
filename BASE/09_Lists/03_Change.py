"""
Change Item Value
To change the value of a specific item, refer to the index number:  
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
print("\n\n")


"""
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where you want to insert the new values:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

""" 
If you insert more items than you replace, the new items will be inserted where you specified, 
and the remaining items will move accordingly: 
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print("\n\n")


"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

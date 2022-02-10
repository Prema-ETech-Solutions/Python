# Add Items
# To add one item to a set use the add() method.
from tokenize import String


thisset = {"apple", "banana", "cherry"}
print("BEFORE")
print(thisset)

thisset.add("orange")

print("AFTER")
print(thisset)


"""
Add Sets
To add items from another set into the current set, use the update() method.  
"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

"""
Add Any Iterable
The object in the update() method does not have to be a set, 
it can be any iterable object (tuples, lists, dictionaries etc.).  
"""
thisset = {"apple", "banana", "cherry"}
my_list = ["kiwi", "orange"]

thisset.update(my_list)

print(thisset)
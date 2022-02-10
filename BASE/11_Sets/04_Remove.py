# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# You can also use the pop() method to remove an item, 
# but this method will remove the last item. 
# Remember that sets are unordered, 
# so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

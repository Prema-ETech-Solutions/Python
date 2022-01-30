""" 
Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
"""
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print("\n\n")

"""
Sort Descending
To sort descending, use the keyword argument reverse = True:  
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
print("\n\n")


"""
Case Insensitive Sort
By default the sort() method is case sensitive, 
resulting in all capital letters being sorted before lower case letters:  
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function: 
"""
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print("\n\n")

"""
Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.  
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

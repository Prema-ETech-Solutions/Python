thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, 
# changeable and do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

print(thisdict)

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, 
# and can be referred to by using the key name.
print(thisdict["brand"])

# Ordered or Unordered ?

"""
When we say that dictionaries are ordered, 
it means that the items have a defined order, 
and that order will not change.

Unordered means that the items does not have a defined order, 
you cannot refer to an item by using an index.
"""

"""
Changeable
Dictionaries are changeable, meaning that we can change, 
add or remove items after the dictionary has been created.
"""

"""
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:  
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


"""
Dictionary Length
To determine how many items a dictionary has, use the len() function:  
"""
print(len(thisdict))

"""
Dictionary Items - Data Types
The values in dictionary items can be of any data type:  
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# type()
# From Python's perspective, 
# dictionaries are defined as objects with the data type 'dict':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

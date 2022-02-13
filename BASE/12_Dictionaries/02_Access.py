# Accessing Items
# You can access the items of a dictionary by referring to its key name, 
# inside square brackets:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# There is also a method called get() that will give you the same result:

x = thisdict.get("model")
print(x)

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

# The list of the keys is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected 
# in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

# Get Values
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

# Get Items
# The items() method will return each item in a dictionary, 
# as tuples in a list.
x = thisdict.items()

print(x)

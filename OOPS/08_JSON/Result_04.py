"""
Format the Result
The example above prints a JSON string, but it is not very easy to read, with no 
indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result:  
"""
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))


# You can also define the separators, default value is (", ", ": "), 
# which means using a comma and a space to separate each object, 
# and a colon and a space to separate keys from values:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print("\n\n\n")
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


print("\n\n\n")
# Order the Result
# The json.dumps() method has parameters to order the keys in the result:
print(json.dumps(x, indent=4, sort_keys=True))

"""
If you need to create a global variable, 
but are stuck in the local scope, 
you can use the global keyword.

The global keyword makes the variable global.  
"""
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Also, use the global keyword if you want to make a 
# change to a global variable inside a function.

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

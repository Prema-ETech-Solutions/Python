def myfunc():
  x = 10
  print(x)

myfunc()

"""
Function Inside Function
As explained in the example above, 
the variable x is not available outside the function, 
but it is available for any function inside the function:  
"""

def myfunc():
  x = 300
  def my_inner_func():
    print(x)
  my_inner_func()

myfunc()
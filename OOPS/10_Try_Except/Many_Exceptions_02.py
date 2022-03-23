# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

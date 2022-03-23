# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

try:
  print(x)
except:
  print("An exception occurred")


# Since the try block raises an error, the except block will be executed.

# Without the try block, the program will crash and raise an error:

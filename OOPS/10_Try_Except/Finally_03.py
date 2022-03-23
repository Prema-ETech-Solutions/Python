# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
#   print("Hello")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# This can be useful to close objects and clean up resources:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  


# The program can continue, without leaving the file object open.
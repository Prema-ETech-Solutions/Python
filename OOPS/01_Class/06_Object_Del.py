""" 
Delete Object Properties
You can delete properties on objects by using the del keyword:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

# del p1.age
# del p1
print(p1.age)


"""
To create an object/class as an iterator you have to implement the methods 
__iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, 
all classes have a function called __init__(), 
which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, 
you can do operations (initializing etc.), 
but must always return the iterator object itself.

The __next__() method also allows you to do operations, 
and must return the next item in the sequence. 
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
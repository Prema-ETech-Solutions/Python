"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, 
meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the 
iterator protocol, which consist of the methods __iter__() and __next__().  
"""

"""
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:  
"""

my_tuple = ("apple", "banana", "cherry")
my_it = iter(my_tuple)

print(next(my_it))
print(next(my_it))
print(next(my_it))

"""
Even strings are iterable objects, and can return an iterator:
"""
my_str = "banana"
my_it = iter(my_str)

print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
print(next(my_it))
# Index Numbers
# You can use index numbers 
# (a number inside the curly brackets {0}) to be sure the 
# values are placed in the correct placeholders:

quantity = 3
item_no = 567
price = 49
my_order = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(my_order.format(quantity, item_no, price))

# Also, if you want to refer to the same value 
# more than once, use the index number:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



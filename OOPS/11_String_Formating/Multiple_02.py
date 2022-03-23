# If you want to use more values, 
# just add more values to the format() method:


# And add more placeholders:

quantity = 3
item_no = 567
price = 49
my_order = "I want {} pieces of item number {} for {:.2f} dollars."
print(my_order.format(quantity, item_no, price))



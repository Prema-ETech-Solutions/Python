# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets 
# {carname}, but then you must use names when you pass the parameter 
# values txt.format(carname = "Ford"):

my_order = "I have a {carname}, it is a {model}."
print(my_order.format(carname = "Ford", model = "Mustang"))

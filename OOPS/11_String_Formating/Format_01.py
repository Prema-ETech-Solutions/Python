"""
String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, 
maybe they come from a database, or user input?

To control such values, add placeholders 
(curly brackets {}) in the text, 
and run the values through the format() method:  
"""
Data = "Hello"
txt = "{} World !"
print(txt.format(Data))
price = 1000
# You can add parameters inside the curly 
# brackets to specify how to convert the value:
txt = "The price is {:.2f} dollars"
print(txt.format(price))
# Check out all formatting types in our String format() Reference.



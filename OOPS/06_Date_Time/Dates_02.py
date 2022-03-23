
"""
Date Output
When we execute the code from the example above the result will be:

2022-03-22 18:00:16.098296
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date 
object.

Here are a few examples, you will learn more about them later in this chapter:  
"""
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

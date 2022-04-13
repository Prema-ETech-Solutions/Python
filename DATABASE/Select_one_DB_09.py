"""
Using the fetchone() Method
If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:  
"""
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123",
#   database="my"
)

my_cursor = my_db.cursor()

my_cursor.execute("SELECT * FROM my.login")

my_result = my_cursor.fetchone()

print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)
my_result = my_cursor.fetchone()
print(my_result)



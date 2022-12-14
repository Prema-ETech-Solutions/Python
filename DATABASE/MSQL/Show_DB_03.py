# Check if Database Exists
# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:

import string
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123"
)

my_cursor = my_db.cursor()

my_cursor.execute("SHOW DATABASES")

for x in my_cursor:
  # x=str(x)
  print(x)
  print(type(x))



# Or you can try to access the database when making the connection:
my_db01 = mysql.connector.connect(
   host="localhost",
  user="root",
  password="@123",
  database="my"
)
# print(str(x))
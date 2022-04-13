"""
Select From a Table
To select from a table in MySQL, use the "SELECT" statement:  
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

my_result = my_cursor.fetchall()
print(type(my_result))
for x in my_result:
  print(x)

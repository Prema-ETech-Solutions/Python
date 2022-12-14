import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123"
)

print(my_db)
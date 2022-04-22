import mysql.connector

# Import module
import sqlite3

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123"
)

print(my_db)

cursor = my_db.cursor()

print('\nColumns in EMPLOYEE table:')
data=cursor.execute('''SELECT * FROM contact.contact''')
for column in data.description:
    print(column[0])
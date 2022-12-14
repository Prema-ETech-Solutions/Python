""" 
Update Table
You can update existing records in a table by using the "UPDATE" statement: 
"""

import mysql.connector

my_db = mysql.connector.connect(
 host="localhost",
  user="root",
  password="@123",
#   database="my"
)

my_cursor = my_db.cursor()

sql = "UPDATE my.login SET COMPANY_ID = 'Main Road' WHERE COMPANY_ID = 'Valley'"

my_cursor.execute(sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) affected")
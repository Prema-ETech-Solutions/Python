"""
Delete Record
You can delete records from an existing table by using the "DELETE FROM" statement:  
"""
import mysql.connector

my_db = mysql.connector.connect(
   host="localhost",
  user="root",
  password="@123",
#   database="my"
)

my_cursor = my_db.cursor()

sql = "DELETE FROM my.login WHERE COMPANY_NAME = 'FCS'"

my_cursor.execute(sql)

my_db.commit()

print(my_cursor.rowcount, "record(s) deleted")

"""
Insert Into Table
To fill a table in MySQL, use the "INSERT INTO" statement.  
"""
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123",
  database="my"
)

my_cursor = my_db.cursor()

sql = "INSERT INTO my.login (COMPANY_NAME, COMPANY_ID, COMPANY_PASSWORD) VALUES (%s,%s,%s);"
val = ("FCS", "FCS_01","Hello")
print(type(val))
# my_cursor.execute(sql, val)

# my_db.commit()

print(my_cursor.rowcount, "record inserted.")
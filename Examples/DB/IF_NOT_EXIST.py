import mysql.connector


my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123"
)
db=my_db.cursor()
db.execute("show databases")
lst=db.fetchall()
data_name="Contact"
# db.execute("CREATE SCHEMA  {}".format(data_name))
db.execute("CREATE SCHEMA IF NOT EXISTS {}".format(data_name))
print("database created")

     
""" 
Creating a Table
To create a table in MySQL, use the "CREATE TABLE" statement.

Make sure you define the name of the database when you create the connection 
"""
import mysql.connector

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123",
  database="my"
)
my_cursor = my_db.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS login(ID int NOT NULL AUTO_INCREMENT,COMPANY_NAME varchar(100),COMPANY_ID varchar(100),COMPANY_PASSWORD varchar(100),PRIMARY KEY (ID))")
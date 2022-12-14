"""
Insert Multiple Rows
To insert multiple rows into a table, use the executemany() method.

The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:  
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
val = [
  ('Peter', 'Lowstreet ','4'),
  ('Amy', 'Apple st',' 652'),
  ('Hannah', 'Mountain',' 21'),
  ('Michael', 'Valley',' 345'),
  ('Sandy', 'Ocean blvd ','2'),
  ('Betty', 'Green Grass',' 1'),
  ('Richard', 'Sky st',' 331'),
  ('Susan', 'One way ','98'),
  ('Vicky', 'Yellow Garden ','2'),
  ('Ben', 'Park Lane ','38'),
  ('William', 'Central st ','954'),
  ('Chuck', 'Main Road ','989'),
  ('Viola', 'Sideway ','1633')
]
my_cursor.executemany(sql, val)

my_db.commit()

print(my_cursor.rowcount, "record inserted.")
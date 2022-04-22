import mysql.connector
from faker import Faker
fake=Faker() 
from random import randint
import names

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

my_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@123",
  database="contact"
)

my_cursor = my_db.cursor()

sql = "INSERT INTO contact.contact (First_Name, Middle_Name, Last_Name, Nickname, Mobile_Number, Work_Number, Company, Birthday, Address) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s);"

a = 0
while True:
    data=[]
    data.append(names.get_first_name())
    data.append("NOT AVAILABLE")
    data.append("NOT AVAILABLE")
    data.append("NOT AVAILABLE")
    data.append(random_with_N_digits(10))
    data.append("NOT AVAILABLE")
    data.append("NOT AVAILABLE")
    data.append("NOT AVAILABLE")
    data.append("NOT AVAILABLE")
    val = tuple(data)
    # print(type(val))
    my_cursor.execute(sql, val)
    my_db.commit()
    a=a+1
    if a == 400:
        break


print(my_cursor.rowcount, "record inserted.")

# print(fake.first_name_male())
# n = random.randint(1)

# print(random_with_N_digits(10))

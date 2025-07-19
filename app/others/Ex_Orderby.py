#importing sqlite module
import sqlite3

#create connection to the database
#geeks database
connection = sqlite3.connect('geeks_database.db')

#create table named address of customerss
#with 4 columns id,name age and address
connection.execute('''CREATE TABLE IF NOT EXISTS customer_address(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,AGE TEXT NOT NULL,ADDRESS CHAR(50));''')
connection.commit()
#insert records into table
connection.execute(
    "INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad' )")
connection.execute(
    "INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam')")
connection.execute(
    "INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur' )")
connection.execute(
    "INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu' )")
connection.execute(
    "INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida')")
# SQL query to display all details from table in ascending order based on address
cursor = connection.execute("SELECT * FROM customer_address ORDER BY ADDRESS ASC")

# Display data row by row
for i in cursor:
    print(i)
# SQL query to display address and id
# #bases on address in desccending order
cursor = connection.execute("SELECT ADDRESS, ID FROM customer_address ORDER BY ADDRESS DESC")
#display data row by row
for i in cursor:
    print(i)

#sql query to display name and id based
# on name in ascending order
cursor = connection.execute("SELECT NAME, ID FROM customer_address ORDER BY NAME DESC")
#display data row by row
for i in cursor:
    print(i)
        
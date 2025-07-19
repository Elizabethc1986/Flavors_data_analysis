#importing sqlite module
import sqlite3

#create connection to the database
#geeks_database
connection = sqlite3.connect('geeks_database.db')

#create table named address of customers
#with 4 columns id,name and address
connection.execute('''CREATE TABLE IF NOT EXISTS customer_address (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50));''')
# insert records into table
#connection.execute( "INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad' )")
#connection.execute( "INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam' )")
#connection.execute( "INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur' )")
#connection.execute( "INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu')")
#connection.execute( "INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida' )")
cursor = connection.execute("SELECT * FROM customer_address LIMIT 4")
#display data row by row
for i in cursor:
    print(i)

#Import SQLite
import sqlite3
print("Welcome to onlinefoods!")

# Connect with our database
connection = sqlite3.connect("data/onlinefood.db")
cursor = connection.cursor()
# create some queries:
#1.Top of family size preference for online food
#2.Which place in the world has the highest preference for online food?
#3.


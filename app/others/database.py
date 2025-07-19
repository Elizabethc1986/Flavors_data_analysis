import sqlite3
print("database test")
connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('samy', 'shark', 1)")
cursor.execute("INSERT INTO fish Values('jaime', 'cuttlefish', 7)")
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)
connection.close()


import sqlite3
connection = sqlite3.connect("cafe.db")
cursor = connection.cursor()

#cursor.execute("CREATE TABLE cafe (name TEXT, type TEXT, price INTEGER)")
cursor.execute("INSERT INTO cafe VALUES ('antioquia', 'descafeinado', 120)")
cursor.execute("INSERT INTO cafe Values('tolima', 'regular', 35)")
rows = cursor.execute("SELECT name, type, price FROM cafe").fetchall()
print(rows)
connection.commit()
data = [
    ("caribe", "cafeina", 50),
    ("Valle", "choclate", 45),
    ("Amazonas", "vanilla", 37),
]
cursor.executemany("INSERT INTO cafe VALUES(?, ?, ?)", data)
rows = cursor.execute("SELECT name, type, price FROM cafe").fetchall()
print(rows)
connection.commit()
for rows in cursor.execute("SELECT name, type  FROM cafe ORDER BY name"):
    print(rows)
connection.close()
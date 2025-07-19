import sqlite3

# Conectarse a SQLite (creará la base de datos si no existe)
connection_obj = sqlite3.connect('geek.db')

# Crear un cursor
cursor_obj = connection_obj.cursor()

# Crear la tabla GEEK si no existe
create_table_query = """
CREATE TABLE IF NOT EXISTS GEEK (
    Email TEXT NOT NULL,
    Name TEXT NOT NULL,
    Score INTEGER
);
"""
cursor_obj.execute(create_table_query)

# Limpiar la tabla (opcional, para evitar duplicados en cada ejecución)
cursor_obj.execute("DELETE FROM GEEK")

# Insertar datos en la tabla GEEK
insert_query = "INSERT INTO GEEK (Email, Name, Score) VALUES (?, ?, ?)"
data = [
    ("geekk1@gmail.com", "Geek1", 25),
    ("geekk2@gmail.com", "Geek2", 15),
    ("geekk3@gmail.com", "Geek3", 36),
    ("geekk4@gmail.com", "Geek4", 27),
    ("geekk5@gmail.com", "Geek5", 40),
    ("geekk6@gmail.com", "Geek6", 14),
    ("geekk7@gmail.com", "Geek7", 10)
]

cursor_obj.executemany(insert_query, data)

# Eliminar registros con Score < 15
cursor_obj.execute("DELETE FROM GEEK WHERE Score < 15")

# Consultar y mostrar los datos restantes
cursor_obj.execute("SELECT * FROM GEEK")
rows = cursor_obj.fetchall()

print("Registros restantes en la tabla GEEK:")
for row in rows:
    print(row)
#delete data 
'''It will delete all rows from
   the table
'''
cursor_obj.execute("DELETE FROM GEEK")
print()
print("After deleting all rows")
cursor_obj.execute("SELECT * FROM GEEK")
print(cursor_obj.fetchall())    
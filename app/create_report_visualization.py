# Titulo: Exploracion de sabores__
# Proposito: Cuantificar las preferencias_y mostrarlas en una forma grafica_ 
# Actualizacion: 2025-07-06
# Autores: Liz y JRO

#-------------
# METAS: 
#-------------
# La idea es usando uno base de datos para create_report_visualization
# - Un reporte
# - Una visualizacion de los datos

# Importar SQLite
import sqlite3

print("Bienvenida a la exploracion de sabores!")

# Connectar a nuestra base de datos / archivo
connection = sqlite3.connect("data/flavors.db")
cursor = connection.cursor()
# Correr algunos queries:
# (1) Que tipo de sabor preferido tienen las personas con exposicion culinaria Mediterraneo.Top preferred taste for mediterranean people

# Filter only on historical quisine of Mediterranan
# Question: In SQL, how to filter on a text value within column of data?
# SELECT *
# FROM table_name
# WHERE column_name = 'desired_text';

# select * from flavors where historical_cuisine_exposure = 'Mediterranean';

# select preferred_taste, COUNT(*) as taste_count
# FROM flavors 
# WHERE historical_cuisine_exposure = 'Mediterranean'
# GROUP BY preferred_taste
# ORDER BY taste_count DESC;

# # Question: How to sort data in SQL?
# ORDER BY column_name [ASC|DESC];

# Do a count on the preferred tastes
# Question: How can I count the occurences of data in SQL
# SELECT column_name, COUNT(*) AS occurrence_count
# FROM table_name
# GROUP BY column_name;
# Sort by highest count to lowests

rows = cursor.execute("SELECT preferred_taste, COUNT(*) AS taste_count FROM flavors WHERE historical_cuisine_exposure = 'Mediterranean' GROUP BY preferred_taste ORDER BY taste_count DESC;").fetchall()
print(rows)
# (2) Cual es en promedio de edad para personas con ciclo de sueño early Bird.What is the average of the age  for people with a sleep "early sleep"
rows = cursor.execute("SELECT AVG(age) AS ave_age FROM flavors WHERE sleep_cycle = 'night' ;").fetchall()
print(rows)

# (3) Cuantas personas que viven en clima frio hacen ejercicio fuerte.How many people in the cold climate zone practice heavy excericise habits
rows = cursor.execute("""SELECT count(*) AS count_climate_zone FROM flavors WHERE exercise_habits = 'Heavy' AND climate_zone = 'Cold' ;""").fetchall()
print(rows)

# (4) Cuales es el sabor que menos le gusta a las personas de 25 años
rows = cursor.execute("""SELECT preferred_taste FROM flavors WHERE age = 25 GROUP BY preferred_taste ORDER BY preferred_taste ASC;""").fetchall()
print(rows)

#(5)Cuantas personas entre 18 -50 años les gusta ejercicio fuerte,viven en un clima seco y es gusta el sabor sour
total = cursor.execute("""SELECT COUNT(*) AS total_personas FROM flavors WHERE age > 18 AND age < 50 AND exercise_habits = 'Heavy' AND climate_zone = 'Dry' AND preferred_taste = 'Sour';""").fetchone()
print(f"Total de personas: {total[0]}")

# Mostrar la informacion en la pantalla

# Usar una libreria de visualizacion (por ejemplo: Apache ECharts, o D3.JS) 
# para hacer una exploracion de visualizacion de los datos

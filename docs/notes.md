---
titulo: "Notas del Proyecto"
actualizacion: 2025-07-06
---

# Notas del Proyecto
## 2025-07-18
-problem: each time we load the database Flavors.Maybe the data run two or three times.
-Load csv into dtabase and rename the file 
-Rename the project with somethin informative(Medellin-cafe-eventos)
-
How to type a back tick:`
Install Git init on windows
```
echo "# Flavors_data_analysis" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Elizabethc1986/Flavors_data_analysis.git
git push -u origin main
```


## 2025-07-06
- Vision:cientifico de datos.Porque quiero aprender a entender la infomacion y poder generar nuevas ideas y estrategias en la compañia o para mi vida personal.Me ayuda porque puede tener mas conocimiento en programacion y me puede generar nuevas oportunidades laborales /de forma independiente.
- Metas:
    -utilizar la estadistica:We counted how many times flavors preferrences occurred for mediterranean people.
    -Crear un grafico : Next mission
    -
- Planes de Accion
    -Buscar fuentes de informacion de como usar la estadistica en sqlite3.We researched on website
    - Tenemos la aplicaicon e-chart, D3.js:Next mission
-Preguntas
    -Tengo dudas en como funciona el FOR en este caso:next time
    -Meta: Tener confianza utilizando la estructura Para(for):next time

Plan next time
-I will complete the two questions of queries
-We will create visualization according with those questions
-we will explore how to analyze data
- Question: How to run SQLite3 : sqlite3 .\data\flavors.db, and how can I experiment with queries
- Question: How to quit SQlite : .exit or .help


## Useful information


# 2025-07-04
Accomplishments
-create a databse table and instert information from the csv.We did a query in the data.
-Confusing:sql and python at the same time
-More time to practice
-Frustration: Keyboard.Programming characteres


## 2025-06-26
### Metas
- Load a CSV file into a database
- Query the data base for information
    - Examples:
        - How many people prefer salty?

### Processo
- Clean data (CSV)-later
- Open the CSV file_completed
    - Loop through the data and print it_completed
- Create / open a database_later
    - Create a table_later
    - Join table?_later
    - Determine the key
- Loop over the CSV data, and add it to the database_later
- Query the database & see statistics_later
- Predictions_later
- Infographics!!!_later
https://echarts.apache.org/examples/en/index.html#chart-type-line
https://observablehq.com/@d3/gallery






## 2025-06-18
Accomplishments
- Sent WhatsApp message using Python - good job!


## Python
pip install (package)

## Databases
```
# Import database into Python file
import sqlite3
connection = sqlite3.connect("aquarium.db")

# Connect to database
cursor = connection.cursor()
cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, tank_number INTEGER)")

# Import data into database table
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")

# Read data from database table
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

# Close database
connection.close()
```
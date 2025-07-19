# - Clean data (CSV)
# - Open the CSV file
#     - Loop through the data and print it
# - Create / open a database
#     - Create a table
#     - Join table?
#     - Determine the key
# - Loop over the CSV data, and add it to the database

import csv
import sqlite3
print("csv reader")
connection = sqlite3.connect("data/flavors.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS flavors (age REAL, sleep_cycle TEXT, exercise_habits TEXT, climate_zone TEXT,  historical_cuisine_exposure TEXT, preferred_taste TEXT)")
with open('data/FlavorSense.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',')
    line_count = 0

    # TO-DO: Research how For Loops work in 
    # For loops look like:
    #
    # for ...
    #
    for row in csv_reader:
        if line_count == 0:
            print(f' Column names are {", ".join(row)}')
            line_count += 1
        else:
            # 0 age,	1 sleep_cycle,	2 exercise_habits,	climate_zone,	historical_cuisine_exposure,	preferred_taste

            age = row[0]
            sleep_cycle = row[1]
            exercise_habits = row[2]
            climate_zone = row[3]
            historical_cuisine_exposure = row[4] 
            preferred_taste = row[5]

            print(f'Age: {age} \t Sleep cycle: {sleep_cycle} \t exercise_habits: {exercise_habits} \t climate_zone: {climate_zone} \t historical_cuisine_exposure: {historical_cuisine_exposure} \t preferred_taste: {preferred_taste}')

            # TO-DO: Don't add data if its a duplicate
            cursor.execute(f"INSERT INTO flavors VALUES ('{age}', '{sleep_cycle}', '{exercise_habits}', '{climate_zone}', '{historical_cuisine_exposure}', '{preferred_taste}')")

            connection.commit()



            line_count += 1
    print(f'Processed {line_count} lines.')
    print("query the database and print on the screen")
rows = cursor.execute("SELECT age, sleep_cycle, exercise_habits,  climate_zone, historical_cuisine_exposure, preferred_taste FROM flavors").fetchall()
print(rows)
#loop through databse and print the data nicely
#lets do some analytics: count how many birds we have? 
connection.close()